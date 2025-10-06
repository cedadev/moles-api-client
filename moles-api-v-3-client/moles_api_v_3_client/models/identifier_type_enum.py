from enum import Enum


class IdentifierTypeEnum(str, Enum):
    CEDA_ABBREVIATION = "ceda_abbreviation"
    DOI = "doi"
    MOLES1_URL = "moles1_url"
    MOLES2_URL = "moles2_url"
    MOLES3_URL = "moles3_url"

    def __str__(self) -> str:
        return str(self.value)
