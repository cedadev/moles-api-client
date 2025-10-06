from enum import Enum


class LanguageEnum(str, Enum):
    ENGLISH = "English"

    def __str__(self) -> str:
        return str(self.value)
