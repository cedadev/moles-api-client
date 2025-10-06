from enum import Enum


class RoleEnum(str, Enum):
    AUTHOR = "author"
    CEDA_OFFICER = "ceda_officer"
    CO_INVESTIGATOR = "co_investigator"
    CURATOR = "curator"
    CUSTODIAN = "custodian"
    DATA_OWNER = "data_owner"
    DISTRIBUTOR = "distributor"
    FUNDER = "funder"
    METADATA_OWNER = "metadata_owner"
    OPERATOR = "operator"
    POINT_OF_CONTACT = "point_of_contact"
    PRINCIPAL_INVESTIGATOR = "principal_investigator"
    PUBLISHER = "publisher"

    def __str__(self) -> str:
        return str(self.value)
