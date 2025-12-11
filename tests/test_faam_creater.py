import unittest
from unittest.mock import patch, MagicMock

from scripts.faam_record_creater import (_check_api_response, 
                                         poppy_organisation_mappings, 
                                         party_check_create_faam,
                                         get_faam_project,
                                         proj_maker
                                         )


class TestCatalogueTools(unittest.TestCase):
    
    def setUp(self):
        self.logger_patch = patch('scripts.faam_record_creater.log')
        self.mock_log = self.logger_patch.start()

        self.client_patch = patch('scripts.faam_record_creater.CLIENT', MagicMock())
        self.mock_client = self.client_patch.start()

    def tearDown(self):
        patch.stopall()

    @patch('scripts.faam_record_creater.parties_list.sync_detailed')
    def test_poppy_organisation_mappings_valid_name_successful_response(self, mock_sync):
        mock_response = MagicMock()
        mock_response.status_code.value = 200
        mock_response.parsed.count = 1
        mock_response.parsed.results = [{'id': 15, 'name': 'FAAM'}]
        mock_sync.return_value = mock_response

        result = poppy_organisation_mappings('FAAM')
        
        self.assertEqual(result, {'id': 15, 'name': 'FAAM'})
        mock_sync.assert_called_once()


    @patch('scripts.faam_record_creater.parties_list.sync_detailed')
    def test_poppy_organisation_mappings_name_not_in_dict_returns_none(self, mock_sync):
        """Test when organisation name is not in dictionary."""
        result = poppy_organisation_mappings('UNKNOWN_ORG')
        self.assertIsNone(result)
        mock_sync.assert_not_called()

    
    @patch('scripts.faam_record_creater.parties_list.sync_detailed')
    def test_poppy_organisation_mappings_api_error_raises_exception(self, mock_sync):
        """Test when API response is not 200, should raise Exception."""
        mock_response = MagicMock()
        mock_response.status_code.value = 500
        mock_sync.return_value = mock_response

        with self.assertRaises(Exception) as context:
            poppy_organisation_mappings('FAAM')

        self.assertIn("API:", str(context.exception))



    @patch('scripts.faam_record_creater.parties_list.sync_detailed')
    def test_poppy_organisation_mappings_no_results_logs_and_returns_none(self, mock_sync):
        mock_response = MagicMock()
        mock_response.status_code.value = 200
        mock_response.parsed.count = 0
        mock_response.parsed.results = []
        mock_sync.return_value = mock_response

        result = poppy_organisation_mappings('FAAM')
        
        self.assertIsNone(result)
        self.mock_log.error.assert_called_with('NOT FOUND! > %r %r', 'FAAM', 15)

    @patch('scripts.faam_record_creater.poppy_organisation_mappings')
    def test_party_check_create_faam_organization(self, mock_poppy):
        mock_poppy.return_value = 123
        
        result = party_check_create_faam(['ORG123'])
        
        self.assertEqual(result, 123)
        
    @patch('scripts.faam_record_creater.parties_list.sync_detailed')
    def test_party_check_create_faam_first_name_exact(self, mock_sync):
        mock_result = MagicMock()
        mock_result.parsed.count = 1
        mock_result.parsed.results = [MagicMock(ob_id=123)]
        mock_sync.return_value = mock_result
        
        result = party_check_create_faam(['Doe', 'John'])
        
        mock_sync.assert_called_once()
        self.assertEqual(result.ob_id, 123)
    
    @patch('scripts.faam_record_creater.parties_list.sync_detailed')
    def test_party_check_create_faam_first_name_exact(self, mock_sync):
        mock_result = MagicMock()
        mock_result.parsed.count = 1
        mock_result.parsed.results = [MagicMock(ob_id=123)]
        mock_sync.return_value = mock_result
        
        result = party_check_create_faam(['Doe', 'John'])
        
        mock_sync.assert_called_once()
        self.assertEqual(result.ob_id, 123)
        
    
    def test_check_api_response_valid_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code.value = 200
        try:
            _check_api_response(mock_response, expected_status_code=200)
        except Exception:
            self.fail("_check_api_response raised Exception unexpectedly!")

    def test_check_api_response_invalid_status_code_raises_exception(self):
        mock_response = MagicMock()
        mock_response.status_code.value = 500
        with self.assertRaises(Exception) as context:
            _check_api_response(mock_response, expected_status_code=200)
        self.assertIn("API:", str(context.exception))

    @patch('builtins.print')
    def test_check_api_response_prints_message_on_error(self, mock_print):
        mock_response = MagicMock()
        mock_response.status_code.value = 404
        message = "Custom error message"
        with self.assertRaises(Exception):
            _check_api_response(mock_response, expected_status_code=200, message=message)
        mock_print.assert_called_once_with(message)

    def test_check_api_response_missing_status_code_value(self):
        mock_response = MagicMock()
        mock_response.status_code = None
        with self.assertRaises(AttributeError):
            _check_api_response(mock_response, expected_status_code=200)
            
    
    @patch('scripts.faam_record_creater.identifiers_list.sync_detailed')
    def test_get_faam_project_existing_project_single_match(self, mock_identifiers):
        """Should return existing project when one match is found."""
        mock_response = MagicMock()
        mock_response.parsed.count = 1
        mock_response.parsed.results = [MagicMock(uuid='existing-uuid')]
        mock_identifiers.return_value = mock_response

        result = get_faam_project('TESTPROJ')
        
        self.assertEqual(result.uuid, 'existing-uuid')
        mock_identifiers.assert_called_once()


    @patch('scripts.faam_record_creater.identifiers_list.sync_detailed')
    def test_get_faam_project_existing_project_multiple_matches_raises(self, mock_identifiers):
        """Should raise Exception when multiple matches are found."""
        mock_response = MagicMock()
        mock_response.parsed.count = 2
        mock_identifiers.return_value = mock_response

        with self.assertRaises(Exception) as context:
            get_faam_project('TESTPROJ')
        self.assertIn('too many matches', str(context.exception))


    @patch('scripts.faam_record_creater.identifiers_list.sync_detailed')
    @patch('scripts.faam_record_creater.projects_create.sync_detailed')
    @patch('scripts.faam_record_creater.projects_list.sync_detailed')
    @patch('scripts.faam_record_creater.identifiers_create.sync_detailed')
    @patch('scripts.faam_record_creater.mbt.add_parties')
    @patch('scripts.faam_record_creater.mbt._get_value_enum')
    @patch('scripts.faam_record_creater._check_api_response')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_get_faam_project_creates_new_project_success(
        self, mock_open, mock_check_api, mock_get_enum, mock_add_parties,
        mock_identifiers_create, mock_projects_list, mock_projects_create, mock_identifiers
    ):
        """Should create new project when no existing match is found."""
        # identifiers_list returns no match
        mock_identifiers.return_value.parsed.count = 0

        # projects_create returns new project
        new_proj = MagicMock(uuid='new-uuid', title='New Project')
        mock_projects_create.return_value.parsed = new_proj

        # identifiers_create returns success
        mock_identifiers_create.return_value.status_code.value = 201

        # projects_list returns final project record
        mock_projects_list.return_value.parsed.results = [new_proj]

        mock_get_enum.return_value = 'ceda_abbreviation'

        result = get_faam_project('TESTPROJ')

        # Assertions
        self.assertEqual(result.uuid, 'new-uuid')
        mock_projects_create.assert_called_once()
        mock_add_parties.assert_called_once()
        mock_identifiers_create.assert_called_once()
        mock_check_api.assert_any_call(mock_identifiers_create.return_value, 201, "Error while creating identifier record")
        mock_check_api.assert_any_call(mock_projects_list.return_value, 200)
        mock_open.assert_called_once_with('new_proj_list', 'a')


    
    

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('scripts.faam_record_creater._check_api_response', side_effect=Exception("API Error"))
    @patch('scripts.faam_record_creater.mbt._get_value_enum')
    @patch('scripts.faam_record_creater.mbt.add_parties')
    @patch('scripts.faam_record_creater.projects_list.sync_detailed')
    @patch('scripts.faam_record_creater.identifiers_create.sync_detailed')
    @patch('scripts.faam_record_creater.projects_create.sync_detailed')
    @patch('scripts.faam_record_creater.identifiers_list.sync_detailed')
    def test_get_faam_project_identifier_api_error_raises(
        self,
        mock_identifiers,         
        mock_projects_create,
        mock_identifiers_create,
        mock_projects_list,
        mock_add_parties,
        mock_get_enum,
        mock_check_api,
        mock_open                
    ):
        """Should raise Exception if identifier creation API check fails."""
        mock_identifiers.return_value.parsed.count = 0
        mock_projects_create.return_value.parsed = MagicMock(uuid='new-uuid')
        mock_identifiers_create.return_value.status_code.value = 201
        mock_get_enum.return_value = 'ceda_abbreviation'

        with self.assertRaises(Exception) as context:
            get_faam_project('TESTPROJ')

    
    
if __name__ == '__main__':
    unittest.main()
