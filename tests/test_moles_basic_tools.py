import unittest
from unittest.mock import patch, MagicMock

import scripts.moles_basic_tools as mbt

from moles_api_v_3_client.models.role_enum import RoleEnum
from moles_api_v_3_client.models.identifier_type_enum import IdentifierTypeEnum


ROLES = {
    RoleEnum.AUTHOR: "author",
    RoleEnum.CEDA_OFFICER: "ceda_officer",
    RoleEnum.CO_INVESTIGATOR: "co_investigator",
    RoleEnum.CURATOR: "curator",
}


class TestMolesBasicTools(unittest.TestCase):
    
    def setUp(self):
        self.logger_patch = patch('scripts.moles_basic_tools.log')
        self.mock_log = self.logger_patch.start()

        self.client_patch = patch('scripts.moles_basic_tools.CLIENT', MagicMock())
        self.mock_client = self.client_patch.start()

    def tearDown(self):
        patch.stopall()

    def test_get_value_enum(self):
        enum_class = RoleEnum
        for k, v in ROLES.items():
            self.assertEqual(mbt._get_value_enum(v, enum_class), k)
    
    @patch('scripts.moles_basic_tools.identifiers_list.sync_detailed')
    def test_doi_id_checker_doi_true(self, mock_sync):
        mock_record = MagicMock()
        mock_record.uuid = "exampleuuid"
        
        mock_response = MagicMock()
        mock_response.parsed.count = 1
        mock_sync.return_value = mock_response


        result = mbt.doi_id_checker(mock_record)
        
        mock_sync.assert_called_once_with(
            client=self.mock_client,
            identifier_type=mbt._get_value_enum('doi', IdentifierTypeEnum),
            related_to_uuid='exampleuuid'
        )
        self.assertTrue(result)
        
    @patch('scripts.moles_basic_tools.identifiers_list.sync_detailed')
    def test_doi_id_checker_doi_false(self, mock_sync):
        mock_record = MagicMock()
        mock_record.uuid = "exampleuuid"
        
        mock_response = MagicMock()
        mock_response.parsed.count = 0
        mock_sync.return_value = mock_response


        result = mbt.doi_id_checker(mock_record)
        
        mock_sync.assert_called_once_with(
            client=self.mock_client,
            identifier_type='doi',
            related_to_uuid='exampleuuid'
        )
        self.assertFalse(result)   
            
    