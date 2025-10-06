from enum import Enum


class ObservationsListLanguage(str, Enum):
    ENGLISH = "English"

    def __str__(self) -> str:
        return str(self.value)
