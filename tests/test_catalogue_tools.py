import unittest
from unittest.mock import patch, MagicMock

from scripts.catalogue_tools import *


class TestCatalogueTools(unittest.TestCase):
    
    def setUp(self):
        self.logger_patch = patch('scripts.catalogue_tools.log')
        self.mock_log = self.logger_patch.start()

        self.client_patch = patch('scripts.catalogue_tools.CLIENT', MagicMock())
        self.mock_client = self.client_patch.start()

    def tearDown(self):
        patch.stopall()

    @patch('scripts.catalogue_tools.parties_list.sync_detailed')
    def test_poppy_organisation_mappings_valid_name_successful_response(self, mock_sync):
        mock_response = MagicMock()
        mock_response.status_code.value = 200
        mock_response.parsed.count = 1
        mock_response.parsed.results = [{'id': 15, 'name': 'FAAM'}]
        mock_sync.return_value = mock_response

        result = poppy_organisation_mappings('FAAM')
        self.assertEqual(result, {'id': 15, 'name': 'FAAM'})
        mock_sync.assert_called_once()


    @patch('scripts.catalogue_tools.parties_list.sync_detailed')
    def test_poppy_organisation_mappings_name_not_in_dict_returns_none(self, mock_sync):
        """Test when organisation name is not in dictionary."""
        result = poppy_organisation_mappings('UNKNOWN_ORG')
        self.assertIsNone(result)
        mock_sync.assert_not_called()

    @patch('scripts.catalogue_tools.parties_list.sync_detailed')
    def test_poppy_organisation_mappings_api_error_returns_none_and_logs(self, mock_sync):
        """Test when API response is not 200."""
        mock_response = MagicMock()
        mock_response.status_code = MagicMock(value=500)
        mock_sync.return_value = mock_response

        result = poppy_organisation_mappings('FAAM')
        self.assertIsNone(result)
        self.mock_log.error.assert_called_with(
        'API ERROR > %r', mock_sync.return_value.status_code
    )


    @patch('scripts.catalogue_tools.parties_list.sync_detailed')
    def test_poppy_organisation_mappings_no_results_logs_and_returns_none(self, mock_sync):
        mock_response = MagicMock()
        mock_response.status_code.value = 200
        mock_response.parsed.count = 0
        mock_response.parsed.results = []
        mock_sync.return_value = mock_response

        result = poppy_organisation_mappings('FAAM')
        self.assertIsNone(result)
        self.mock_log.error.assert_called_with('NOT FOUND! > %r %r', 'FAAM', 15)

    @patch('scripts.catalogue_tools.poppy_organisation_mappings')
    def test_party_check_create_faam_organization(self, mock_poppy):
        mock_poppy.return_value = 123
        result = party_check_create_faam(['ORG123'])
        
        self.assertEqual(result, 123)
        
    @patch('scripts.catalogue_tools.parties_list.sync_detailed')
    def test_party_check_create_faam_first_name_exact(self, mock_sync):
        mock_result = MagicMock()
        mock_result.parsed.count = 1
        mock_result.parsed.results = [MagicMock(ob_id=123)]
        mock_sync.return_value = mock_result
        
        result = party_check_create_faam(['Doe', 'John'])
        
        mock_sync.assert_called_once()
        self.assertEqual(result.ob_id, 123)
    
    @patch('scripts.catalogue_tools.parties_list.sync_detailed')
    def test_party_check_create_faam_first_name_exact(self, mock_sync):
        mock_result = MagicMock()
        mock_result.parsed.count = 1
        mock_result.parsed.results = [MagicMock(ob_id=123)]
        mock_sync.return_value = mock_result
        
        result = party_check_create_faam(['Doe', 'John'])
        
        mock_sync.assert_called_once()
        self.assertEqual(result.ob_id, 123)
        
    
    
    
if __name__ == '__main__':
    unittest.main()
