from enum import Enum


class VocabularytermsListVocabularyService(str, Enum):
    CLIPC_SKOS_VOCAB = "clipc_skos_vocab"
    NERC_SKOS_VOCAB = "nerc_skos_vocab"

    def __str__(self) -> str:
        return str(self.value)
