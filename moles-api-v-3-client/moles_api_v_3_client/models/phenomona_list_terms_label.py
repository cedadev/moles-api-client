from enum import Enum


class PhenomonaListTermsLabel(str, Enum):
    ALT_NAMES = "alt_names"
    GCMD_KEYWORD = "gcmd_keyword"
    GCMD_NAME = "gcmd_name"
    GCMD_URL = "gcmd_url"
    LONG_NAME = "long_name"
    NAMES = "names"
    STANDARD_NAME = "standard_name"
    UNITS = "units"
    VAR_ID = "var_id"

    def __str__(self) -> str:
        return str(self.value)
