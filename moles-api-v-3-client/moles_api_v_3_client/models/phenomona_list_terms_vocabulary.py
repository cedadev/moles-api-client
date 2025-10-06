from enum import Enum


class PhenomonaListTermsVocabulary(str, Enum):
    CF_STANDARD_NAMES = "cf_standard_names"
    GCMD_KEYWORD = "gcmd_keyword"

    def __str__(self) -> str:
        return str(self.value)
