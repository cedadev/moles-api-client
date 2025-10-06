from enum import Enum


class CurationCategoryEnum(str, Enum):
    A = "A"
    B = "B"
    C = "C"

    def __str__(self) -> str:
        return str(self.value)
