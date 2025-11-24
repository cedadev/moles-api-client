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
        
        id_type = mbt._get_value_enum('doi', IdentifierTypeEnum)
        mock_sync.assert_called_once_with(
            client=self.mock_client,
            identifier_type=id_type,
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
        
        id_type = mbt._get_value_enum('doi', IdentifierTypeEnum)
        mock_sync.assert_called_once_with(
            client=self.mock_client,
            identifier_type=id_type,
            related_to_uuid='exampleuuid'
        )
        self.assertFalse(result)  
            
    @patch('scripts.moles_basic_tools.get_endpoint_by_shortcode')
    @patch('scripts.moles_basic_tools.referenceables_list.sync_detailed')
    def test_uuid_to_obj_no_short_code_record_exists(self, mock_referenceable_sync, mock_get_endpoint):
        """uuid_to_obj should look up the short_code, then call the mapped endpoint."""
        
        # First API response
        mock_referenceable_response = MagicMock()
        mock_referenceable_response.parsed.count = 1

        mock_referenceable = MagicMock()
        mock_referenceable.short_code = "proj"
        mock_referenceable_response.parsed.results = [mock_referenceable]
        mock_referenceable_sync.return_value = mock_referenceable_response

        # Second API response
        mock_endpoint_list_response = MagicMock()
        mock_record = MagicMock()
        mock_endpoint_list_response.parsed.results = [mock_record]
        
        
        mock_endpoint_list = MagicMock()
        mock_endpoint_list.sync_detailed = MagicMock(return_value = mock_endpoint_list_response)
        
        mock_get_endpoint.return_value = mock_endpoint_list
        
        result = mbt.uuid_to_obj("exampleuuid")

        # referenceables_list called
        mock_referenceable_sync.assert_called_once_with(
            client=self.mock_client,
            uuid="exampleuuid"
        )

        # get_endpoint_by_shortcode called correctly
        mock_get_endpoint.assert_called_once_with("proj")

        # mapped endpoint called
        mock_endpoint_list.sync_detailed.assert_called_once_with(
            client=self.mock_client,
            uuid="exampleuuid"
        )

        self.assertEqual(result, mock_record)
        
    @patch('scripts.moles_basic_tools.referenceables_list.sync_detailed')
    def test_uuid_to_obj_no_short_code_not_found(self, mock_referenceable_sync):
        """uuid_to_obj returns None if referenceables_list count != 1"""
        
        mock_response = MagicMock()
        mock_response.parsed.count = 0
        mock_referenceable_sync.return_value = mock_response

        result = mbt.uuid_to_obj("exampleuuid")

        mock_referenceable_sync.assert_called_once_with(
            client=self.mock_client,
            uuid="exampleuuid"
        )

        self.assertIsNone(result)
        
    @patch("scripts.moles_basic_tools.get_endpoint_by_shortcode")
    @patch("scripts.moles_basic_tools.referenceables_list.sync_detailed")
    def test_uuid_to_obj_with_short_code(self, mock_referenceable_sync, mock_get_endpoint):
        """When short_code is passed, skip the first lookup and go straight to endpoint."""
        
        mock_referenceable_sync.return_value = MagicMock()  # not used

        mock_endpoint_response = MagicMock()
        mock_record = MagicMock()
        mock_endpoint_response.parsed.results = [mock_record]

        mock_endpoint_list = MagicMock()
        mock_endpoint_list.sync_detailed = MagicMock(return_value=mock_endpoint_response)

        mock_get_endpoint.return_value = mock_endpoint_list

        result = mbt.uuid_to_obj("exampleuuid", short_code="proj")

        mock_referenceable_sync.assert_not_called()

        mock_get_endpoint.assert_called_once_with("proj")

        mock_endpoint_list.sync_detailed.assert_called_once_with(
            client=self.mock_client,
            uuid="exampleuuid"
        )

        self.assertEqual(result, mock_record)
        
        
    def _run_get_procedure_test(self, attr, short_code, mock_uuid_to_obj):
        mock_obs = MagicMock()
        mock_proc = MagicMock(uuid="example_uuid", short_code=short_code)

        # Clear all 3, set only the one being tested
        mock_obs.procedureAcquisition = None
        mock_obs.procedureComputation = None
        mock_obs.procedureCompositeProcess = None
        setattr(mock_obs, attr, mock_proc)

        mock_result = MagicMock()
        mock_uuid_to_obj.return_value = mock_result

        result = mbt.get_procedure(mock_obs)

        mock_uuid_to_obj.assert_called_once_with("example_uuid", short_code)
        self.assertEqual(result, mock_result)
    
    
    @patch("scripts.moles_basic_tools.uuid_to_obj")
    def test_get_procedure_acquisition(self, mock_uuid_to_obj):
        self._run_get_procedure_test("procedureAcquisition", "acq", mock_uuid_to_obj)

    @patch("scripts.moles_basic_tools.uuid_to_obj")
    def test_get_procedure_computation(self, mock_uuid_to_obj):
        self._run_get_procedure_test("procedureComputation", "comp", mock_uuid_to_obj)

    @patch("scripts.moles_basic_tools.uuid_to_obj")
    def test_get_procedure_composite(self, mock_uuid_to_obj):
        self._run_get_procedure_test("procedureCompositeProcess", "cmppr", mock_uuid_to_obj)


    @patch('scripts.moles_basic_tools.onlineresources_create.sync_detailed')
    @patch('scripts.moles_basic_tools.onlineresources_list.sync_detailed')
    def test_copy_online_resources_copies_missing(self, mock_list_sync, mock_create_sync):
        # ----- Setup source and target objects -----
        source_object = MagicMock()
        source_object.onlineresource_set = "SRC_SET"
        target_object = MagicMock()
        target_object.onlineresource_set = "TGT_SET"
        target_object.uuid = "target-uuid"

        # ----- Source resources -----
        s_res1 = MagicMock()
        s_res1.linkage = "http://A"
        s_res1.name = "A"

        s_res2 = MagicMock()
        s_res2.linkage = "http://B"
        s_res2.name = "B"


        s_list_resp = MagicMock()
        s_list_resp.parsed.results = [s_res1, s_res2]

        # ----- Target has ONLY resource A -----
        t_res1 = MagicMock(linkage="http://A", name="A")
        
        t_list_resp = MagicMock()
        t_list_resp.parsed.results = [t_res1]

        # mock listing calls for source & target
        mock_list_sync.side_effect = [s_list_resp, t_list_resp]

        # mock create call success
        mock_create_response = MagicMock()
        mock_create_response.status_code.value = 201
        mock_create_sync.return_value = mock_create_response

        # ----- Call -----
        mbt.copy_online_resources(source_object, target_object)

        # ----- Assertions -----

        # 2 list calls: first source, then target
        self.assertEqual(mock_list_sync.call_count, 2)

        # Create should be called ONCE for http://B
        mock_create_sync.assert_called_once()
        args, kwargs = mock_create_sync.call_args
        model_passed = kwargs["body"]

        self.assertEqual(model_passed.linkage, "http://B")
        self.assertEqual(model_passed.name, "B")
        self.assertEqual(model_passed.related_to, "target-uuid")


    @patch('scripts.moles_basic_tools.onlineresources_create.sync_detailed')
    @patch('scripts.moles_basic_tools.onlineresources_list.sync_detailed')
    def test_copy_online_resources_no_duplicates(self, mock_list_sync, mock_create_sync):
        source = MagicMock()
        source.onlineresource_set = "SRC_SET"
        target = MagicMock()
        target.onlineresource_set = "TGT_SET"
        target.uuid = "target-uuid"

        # Source has A, B — but target also has A, B
        s_res1 = MagicMock(linkage="http://A")
        s_res2 = MagicMock(linkage="http://B")

        t_res1 = MagicMock(linkage="http://A")
        t_res2 = MagicMock(linkage="http://B")

        s_list_resp = MagicMock()
        s_list_resp.parsed.results = [s_res1, s_res2]

        t_list_resp = MagicMock()
        t_list_resp.parsed.results = [t_res1, t_res2]

        mock_list_sync.side_effect = [s_list_resp, t_list_resp]

        # ----- Call -----
        mbt.copy_online_resources(source, target)

        # No call to create because nothing missing
        mock_create_sync.assert_not_called()

    @patch('scripts.moles_basic_tools.onlineresources_create.sync_detailed')
    @patch('scripts.moles_basic_tools.onlineresources_list.sync_detailed')
    def test_copy_online_resources_raises_on_failure(self, mock_list_sync, mock_create_sync):
        source = MagicMock()
        source.onlineresource_set = "SRC_SET"
        target = MagicMock()
        target.onlineresource_set = "TGT_SET"
        target.uuid = "target-uuid"

        # One resource in source, none in target
        s_res = MagicMock(linkage="http://X", name="X")
        s_list_resp = MagicMock()
        s_list_resp.parsed.results = [s_res]

        t_list_resp = MagicMock()
        t_list_resp.parsed.results = []

        mock_list_sync.side_effect = [s_list_resp, t_list_resp]

        # Create call FAILS
        failure_response = MagicMock()
        failure_response.status_code.value = 500
        mock_create_sync.return_value = failure_response

        # Expect exception
        with self.assertRaises(RuntimeError) as ctx:
            mbt.copy_online_resources(source, target)

        self.assertIn("API: 500", str(ctx.exception))

    @patch("scripts.moles_basic_tools.parties_list.sync_detailed")
    @patch("scripts.moles_basic_tools.parties_create.sync_detailed")
    def test_party_maker_individual(self, mock_create_sync, mock_list_sync):
        # Mock CREATE response (201 created)
        mock_create_res = MagicMock()
        mock_create_res.status_code = MagicMock()
        mock_create_res.status_code.value = 201
        
        # return an object containing ob_id
        mock_create_res.parsed.ob_id = "1"
        mock_create_sync.return_value = mock_create_res

        # Mock LIST response
        mock_party = MagicMock()
        mock_list_res = MagicMock()
        mock_list_res.parsed.results = [mock_party]
        mock_list_sync.return_value = mock_list_res

        # Call function
        result = mbt.party_maker("Alice", "Smith")

        # CREATE called with correct model
        args, kwargs = mock_create_sync.call_args
        model_passed = kwargs["body"]
        self.assertEqual(model_passed.first_name, "Alice")
        self.assertEqual(model_passed.last_name, "Smith")
        self.assertEqual(model_passed.party_type, "individual")

        # LIST called based on returned ob_id
        mock_list_sync.assert_called_once_with(client=self.mock_client, ob_id="1")

        # Final returned object
        self.assertEqual(result, mock_party)
        
    @patch("scripts.moles_basic_tools.parties_list.sync_detailed")
    @patch("scripts.moles_basic_tools.parties_create.sync_detailed")
    def test_party_maker_organisation(self, mock_create_sync, mock_list_sync):
        # Mock CREATE success
        mock_create_res = MagicMock()
        mock_create_res.status_code = MagicMock()
        mock_create_res.status_code.value = 201
        mock_create_res.parsed.ob_id = "org-id"
        mock_create_sync.return_value = mock_create_res

        # Mock LIST response
        mock_party = MagicMock()
        mock_list_res = MagicMock()
        mock_list_res.parsed.results = [mock_party]
        mock_list_sync.return_value = mock_list_res

        # Call with NO first name → organisation
        result = mbt.party_maker("", "Department X")

        args, kwargs = mock_create_sync.call_args
        model_passed = kwargs["body"]
        self.assertEqual(model_passed.first_name, "")
        self.assertEqual(model_passed.last_name, "Department X")
        self.assertEqual(model_passed.party_type, "organisation")

        # Final returned object
        self.assertEqual(result, mock_party)


    @patch("scripts.moles_basic_tools.parties_create.sync_detailed")
    def test_party_maker_raises_on_failure(self, mock_create_sync):
        # API create fails
        mock_fail_res = MagicMock()
        mock_fail_res.status_code = MagicMock()
        mock_fail_res.status_code.value = 500
        mock_create_sync.return_value = mock_fail_res

        with self.assertRaises(RuntimeError) as ctx:
            mbt.party_maker("John", "Doe")

        self.assertIn("API: 500", str(ctx.exception))

    @patch("scripts.moles_basic_tools.rpis_list.sync_detailed")
    @patch("scripts.moles_basic_tools.rpis_create.sync_detailed")
    def test_rpi_maker_default_priority(self, mock_create_sync, mock_list_sync):
        # Mock CREATE response
        mock_create_res = MagicMock()
        mock_create_res.parsed.ob_id = "rpi-id-123"
        mock_create_sync.return_value = mock_create_res

        # Mock LIST response
        mock_rpi = MagicMock()
        mock_list_res = MagicMock()
        mock_list_res.parsed.results = [mock_rpi]
        mock_list_sync.return_value = mock_list_res

        # Call function
        result = mbt.rpi_maker("author", 42, related_to="record-uuid")

        # Check that _get_value_enum translated role
        args, kwargs = mock_create_sync.call_args
        model_passed = kwargs["body"]
        self.assertEqual(model_passed.party, 42)
        self.assertEqual(model_passed.role, mbt._get_value_enum("author", mbt.RoleEnum))
        self.assertEqual(model_passed.priority, 1)
        self.assertEqual(model_passed.related_to, "record-uuid")

        # Check LIST call
        mock_list_sync.assert_called_once_with(client=self.mock_client, ob_id="rpi-id-123")

        # Final returned object
        self.assertEqual(result, mock_rpi)

    @patch("scripts.moles_basic_tools.rpis_list.sync_detailed")
    @patch("scripts.moles_basic_tools.rpis_create.sync_detailed")
    def test_rpi_maker_custom_priority(self, mock_create_sync, mock_list_sync):
        # Mock CREATE
        mock_create_res = MagicMock()
        mock_create_res.parsed.ob_id = "rpi-id-456"
        mock_create_sync.return_value = mock_create_res

        # Mock LIST
        mock_rpi = MagicMock()
        mock_list_res = MagicMock()
        mock_list_res.parsed.results = [mock_rpi]
        mock_list_sync.return_value = mock_list_res

        # Call with priority=5
        result = mbt.rpi_maker("curator", 99, related_to="rec-uuid", priority=5)

        # Check model
        model_passed = mock_create_sync.call_args.kwargs["body"]
        self.assertEqual(model_passed.priority, 5)
        self.assertEqual(model_passed.role, mbt._get_value_enum("curator", mbt.RoleEnum))
        self.assertEqual(model_passed.party, 99)
        self.assertEqual(model_passed.related_to, "rec-uuid")

        # Final result
        self.assertEqual(result, mock_rpi)
        
    @patch("scripts.moles_basic_tools.parties_list.sync_detailed")
    def test_party_check_create_found_exact(self, mock_list_sync):
        # Party input: [last_name, first_name]
        party_name = ["Smith", "Alice"]

        # First API call returns a result
        mock_party = MagicMock()
        mock_res = MagicMock()
        mock_res.parsed.count = 1
        mock_res.parsed.results = [mock_party]
        mock_list_sync.return_value = mock_res

        result = mbt.party_check_create(party_name)

        # Should call parties_list with last_name + first_name
        mock_list_sync.assert_called_once_with(
            client=mbt.CLIENT,
            last_name="Smith",
            first_name="Alice"
        )

        self.assertEqual(result, mock_party)

    
    @patch("scripts.moles_basic_tools.party_maker")
    @patch("scripts.moles_basic_tools.parties_list.sync_detailed")
    def test_party_check_create_found_startswith(self, mock_list_sync, mock_party_maker):
        # Input: only last name (no first name)
        party_name = ["Smith"]

        # First call returns 0 → triggers startswith call
        mock_res1 = MagicMock()
        mock_res1.parsed.count = 0

        # Second call returns 1 → found
        mock_party = MagicMock()
        mock_res2 = MagicMock()
        mock_res2.parsed.count = 1
        mock_res2.parsed.results = [mock_party]

        mock_list_sync.side_effect = [mock_res1, mock_res2]

        result = mbt.party_check_create(party_name)

        # First call: last_name, first_name=""
        first_call = mock_list_sync.call_args_list[0]
        self.assertEqual(first_call.kwargs["last_name"], "Smith")
        self.assertEqual(first_call.kwargs["first_name"], "")

        # Second call: last_name, first_name_startswith=""
        second_call = mock_list_sync.call_args_list[1]
        self.assertEqual(second_call.kwargs["last_name"], "Smith")
        self.assertEqual(second_call.kwargs["first_name_startswith"], "")

        self.assertEqual(result, mock_party)
        mock_party_maker.assert_not_called()
        
    
    @patch("scripts.moles_basic_tools.party_maker")
    @patch("scripts.moles_basic_tools.parties_list.sync_detailed")
    def test_party_check_create_not_found_calls_maker(self, mock_list_sync, mock_party_maker):
        party_name = ["Smith", "Alice"]

        # Both API calls return 0
        mock_res = MagicMock()
        mock_res.parsed.count = 0
        mock_list_sync.side_effect = [mock_res, mock_res]

        # Mock party_maker return
        mock_created_party = MagicMock()
        mock_party_maker.return_value = mock_created_party

        result = mbt.party_check_create(party_name)

        # party_maker called with first/last
        mock_party_maker.assert_called_once_with("Alice", "Smith")
        self.assertEqual(result, mock_created_party)



    @patch("scripts.moles_basic_tools.rpis_create.sync_detailed")
    @patch("scripts.moles_basic_tools.rpis_list.sync_detailed")
    def test_add_parties_creates_new(self, mock_list_sync, mock_create_sync):
        # Target record
        target_uuid = "record-uuid"
        
        # Party dictionary: role → list of PartyRead mocks
        party1 = MagicMock(ob_id=101)
        party2 = MagicMock(ob_id=102)
        party_dict = {"author": [party1, party2]}
        
        # Existing RPIs: empty list
        mock_list_res = MagicMock()
        mock_list_res.parsed.results = []
        mock_list_res.parsed.count = 0
        mock_list_sync.return_value = mock_list_res
        
        # Mock rpis_create response
        mock_create_resp = MagicMock()
        mock_create_sync.return_value = mock_create_resp
        
        # Call function
        mbt.add_parties(party_dict, target_uuid)
        
        # rpis_list called once per role
        mock_list_sync.assert_called_once_with(client=mbt.CLIENT, related_to_uuid=target_uuid, role="author")
        
        # rpis_create called for both parties
        self.assertEqual(mock_create_sync.call_count, 2)
        
        # Check first call priority
        model1 = mock_create_sync.call_args_list[0].kwargs["body"]
        self.assertEqual(model1.party, 101)
        self.assertEqual(model1.priority, 1)
        
        # Check second call priority
        model2 = mock_create_sync.call_args_list[1].kwargs["body"]
        self.assertEqual(model2.party, 102)
        self.assertEqual(model2.priority, 2)
        
    @patch("scripts.moles_basic_tools.rpis_create.sync_detailed")
    @patch("scripts.moles_basic_tools.rpis_list.sync_detailed")
    def test_add_parties_skips_existing(self, mock_list_sync, mock_create_sync):
        target_uuid = "record-uuid"
        
        # Party dictionary
        party1 = MagicMock(ob_id=101)
        party2 = MagicMock(ob_id=102)
        party_dict = {"author": [party1, party2]}
        
        # Existing RPI already has party1
        existing_rpi = MagicMock()
        existing_rpi.party.ob_id = 101
        mock_list_res = MagicMock()
        mock_list_res.parsed.results = [existing_rpi]
        mock_list_res.parsed.count = 1
        mock_list_sync.return_value = mock_list_res
        
        # Mock create response
        mock_create_sync.return_value = MagicMock()
        
        # Call function
        mbt.add_parties(party_dict, target_uuid)
        
        # Only party2 should be created
        mock_create_sync.assert_called_once()
        model = mock_create_sync.call_args.kwargs["body"]
        self.assertEqual(model.party, 102)
        # Priority should start from existing count + 1 = 2
        self.assertEqual(model.priority, 2)


    @patch("scripts.moles_basic_tools.rpis_create.sync_detailed")
    @patch("scripts.moles_basic_tools.rpis_list.sync_detailed")
    def test_add_parties_multiple_roles(self, mock_list_sync, mock_create_sync):
        target_uuid = "record-uuid"
        
        # Two roles
        party_a1 = MagicMock(ob_id=1)
        party_a2 = MagicMock(ob_id=2)
        party_b1 = MagicMock(ob_id=3)
        party_dict = {"author": [party_a1, party_a2], "curator": [party_b1]}
        
        # Existing RPIs: empty for both roles
        mock_list_res = MagicMock()
        mock_list_res.parsed.results = []
        mock_list_res.parsed.count = 0
        mock_list_sync.return_value = mock_list_res
        
        # Mock create
        mock_create_sync.return_value = MagicMock()
        
        mbt.add_parties(party_dict, target_uuid)
        
        # Total calls: 3 parties
        self.assertEqual(mock_create_sync.call_count, 3)
        
        # Check first role priority
        model_a1 = mock_create_sync.call_args_list[0].kwargs["body"]
        self.assertEqual(model_a1.party, 1)
        self.assertEqual(model_a1.priority, 1)
        
        model_a2 = mock_create_sync.call_args_list[1].kwargs["body"]
        self.assertEqual(model_a2.party, 2)
        self.assertEqual(model_a2.priority, 2)
        
        # Second role starts with priority 1
        model_b1 = mock_create_sync.call_args_list[2].kwargs["body"]
        self.assertEqual(model_b1.party, 3)
        self.assertEqual(model_b1.priority, 1)


    @patch("scripts.moles_basic_tools.add_parties")
    @patch("scripts.moles_basic_tools.rpis_list.sync_detailed")
    def test_copy_party_by_role(self, mock_list_sync, mock_add_parties):
        # Setup source and target objects
        source = MagicMock()
        source.uuid = "source-uuid"
        target = MagicMock()
        target.uuid = "target-uuid"

        # Role
        role = "author"

        # Mock rpis_list returning two RPIs
        rpi1 = MagicMock()
        rpi1.party = MagicMock(ob_id=101)
        rpi2 = MagicMock()
        rpi2.party = MagicMock(ob_id=102)

        mock_res = MagicMock()
        mock_res.parsed.results = [rpi1, rpi2]
        mock_list_sync.return_value = mock_res

        # Call function
        mbt.copy_party_by_role(source, target, role)

        # Assert rpis_list called with correct arguments
        mock_list_sync.assert_called_once_with(
            client=mbt.CLIENT,
            role=mbt._get_value_enum(role, mbt.RoleEnum),
            related_to_uuid="source-uuid"
        )

        # Assert add_parties called with correct dict and target UUID
        mock_add_parties.assert_called_once()
        args, kwargs = mock_add_parties.call_args
        party_dict_arg, target_uuid_arg = args
        self.assertEqual(list(party_dict_arg.keys()), [role])
        self.assertEqual([p.ob_id for p in party_dict_arg[role]], [101, 102])
        self.assertEqual(target_uuid_arg, "target-uuid")

    
    @patch("scripts.moles_basic_tools.add_parties")
    @patch("scripts.moles_basic_tools.rpis_list.sync_detailed")
    def test_copy_party_by_role_no_parties(self, mock_list_sync, mock_add_parties):
        source = MagicMock()
        source.uuid = "source-uuid"
        target = MagicMock()
        target.uuid = "target-uuid"
        role = "curator"

        # Mock rpis_list returns no parties
        mock_res = MagicMock()
        mock_res.parsed.results = []
        mock_list_sync.return_value = mock_res

        mbt.copy_party_by_role(source, target, role)

        # add_parties should still be called with empty list
        mock_add_parties.assert_called_once()
        args, _ = mock_add_parties.call_args
        party_dict_arg = args[0]
        self.assertEqual(party_dict_arg[role], [])

    
    @patch("scripts.moles_basic_tools.identifiers_partial_update.sync_detailed")
    @patch("scripts.moles_basic_tools.identifiers_list.sync_detailed")
    def test_move_identifiers_copies_all(self, mock_list_sync, mock_partial_update_sync):
        # Setup source and target objects
        source = MagicMock()
        source.uuid = "source-uuid"
        target = MagicMock()
        target.uuid = "target-uuid"

        # Mock identifiers_list returning two identifiers
        identifier1 = MagicMock(ob_id=101)
        identifier2 = MagicMock(ob_id=102)
        mock_res = MagicMock()
        mock_res.parsed.results = [identifier1, identifier2]
        mock_list_sync.return_value = mock_res

        # Mock partial update response
        mock_partial_update_sync.return_value = MagicMock()

        # Call function
        mbt.move_identifiers(source, target)

        # identifiers_list called with source UUID
        mock_list_sync.assert_called_once_with(client=mbt.CLIENT, related_to_uuid="source-uuid")

        # partial_update called twice, once for each identifier
        self.assertEqual(mock_partial_update_sync.call_count, 2)

        # Check arguments of first call
        first_call_args = mock_partial_update_sync.call_args_list[0].kwargs
        self.assertEqual(first_call_args["ob_id"], 101)
        self.assertEqual(first_call_args["body"].related_to, "target-uuid")

        # Check arguments of second call
        second_call_args = mock_partial_update_sync.call_args_list[1].kwargs
        self.assertEqual(second_call_args["ob_id"], 102)
        self.assertEqual(second_call_args["body"].related_to, "target-uuid")

    
    @patch("scripts.moles_basic_tools.identifiers_partial_update.sync_detailed")
    @patch("scripts.moles_basic_tools.identifiers_list.sync_detailed")
    def test_move_identifiers_no_identifiers(self, mock_list_sync, mock_partial_update_sync):
        source = MagicMock()
        source.uuid = "source-uuid"
        target = MagicMock()
        target.uuid = "target-uuid"

        # identifiers_list returns empty list
        mock_res = MagicMock()
        mock_res.parsed.results = []
        mock_list_sync.return_value = mock_res

        # Call function
        mbt.move_identifiers(source, target)

        # identifiers_list called
        mock_list_sync.assert_called_once_with(client=mbt.CLIENT, related_to_uuid="source-uuid")

        # partial_update should never be called
        mock_partial_update_sync.assert_not_called()
        

    def test_get_primary_obs_no_project_set(self):
        obs_col = MagicMock()
        obs_col.project_set = []
        obs_col.uuid = "obscol-uuid"

        result = mbt.get_primary_obs_for_collection(obs_col)
        self.assertEqual(result, [])


    @patch("scripts.moles_basic_tools.results_list.sync_detailed")
    @patch("scripts.moles_basic_tools.observations_list.sync_detailed")
    def test_get_primary_obs_filters_by_project(self, mock_obs_list, mock_results_list):
        obs_col = MagicMock()
        obs_col.project_set = [1, 2]
        obs_col.member = ["ob1", "ob2"]

        # Observation in project set
        ob1 = MagicMock()
        ob1.projects = [MagicMock(ob_id=1)]
        ob1.publicationState = "published"
        ob1.result_field.data_path = "path1"

        # Observation not in project set
        ob2 = MagicMock()
        ob2.projects = [MagicMock(ob_id=99)]
        ob2.publicationState = "published"
        ob2.result_field.data_path = "path2"

        mock_obs_list.return_value = MagicMock(parsed=MagicMock(results=[ob1, ob2]))
        
        # results_list returns count=1 for unique check
        mock_results_list.return_value = MagicMock(parsed=MagicMock(count=1))

        result = mbt.get_primary_obs_for_collection(obs_col)

        # Only ob1 should be included
        self.assertEqual(result, [ob1])


    @patch("scripts.moles_basic_tools.results_list.sync_detailed")
    @patch("scripts.moles_basic_tools.observations_list.sync_detailed")
    def test_get_primary_obs_filters_by_pub_status(self, mock_obs_list, mock_results_list):
        obs_col = MagicMock()
        obs_col.project_set = [1]
        obs_col.member = [1]

        # Observation with wrong publication state
        ob = MagicMock()
        ob.projects = [MagicMock(ob_id=1)]
        ob.publicationState = "working"  # not in default publication_status
        ob.result_field.data_path = "path"

        mock_obs_list.return_value = MagicMock(parsed=MagicMock(results=[ob]))
        mock_results_list.return_value = MagicMock(parsed=MagicMock(count=1))

        result = mbt.get_primary_obs_for_collection(obs_col, pub_level=1)
        self.assertEqual(result, [])  # filtered out

        # With pub_level != 1, working should be included
        result2 = mbt.get_primary_obs_for_collection(obs_col, pub_level=2)
        self.assertEqual(result2, [ob])

    
    @patch("scripts.moles_basic_tools.results_list.sync_detailed")
    @patch("scripts.moles_basic_tools.observations_list.sync_detailed")
    def test_get_primary_obs_unique_check(self, mock_obs_list, mock_results_list):
        obs_col = MagicMock()
        obs_col.project_set = [1]
        obs_col.member = ["ob1"]

        # Observation passing project & publication checks
        ob = MagicMock()
        ob.projects = [MagicMock(ob_id=1)]
        ob.publicationState = "published"
        ob.result_field.data_path = "path1"
        ob.result_field.internalPath = "internal_path1"

        mock_obs_list.return_value = MagicMock(parsed=MagicMock(results=[ob]))
        
        # results_list returns count != 1 → filtered out
        mock_results_list.return_value = MagicMock(parsed=MagicMock(count=0))

        result = mbt.get_primary_obs_for_collection(obs_col)
        self.assertEqual(result, [])

        # results_list returns count=1 → included
        mock_results_list.return_value = MagicMock(parsed=MagicMock(count=1))
        result2 = mbt.get_primary_obs_for_collection(obs_col)
        self.assertEqual(result2, [ob])

    @patch("scripts.moles_basic_tools.observations_list.sync_detailed")
    def test_get_primary_obs_unique_false(self, mock_obs_list):
        obs_col = MagicMock()
        obs_col.project_set = [1]
        obs_col.member = ["ob1"]

        # Observation passes project & publication checks
        ob = MagicMock()
        ob.projects = [MagicMock(ob_id=1)]
        ob.publicationState = "published"

        mock_obs_list.return_value = MagicMock(parsed=MagicMock(results=[ob]))

        result = mbt.get_primary_obs_for_collection(obs_col, unique=False)
        self.assertEqual(result, [ob])
