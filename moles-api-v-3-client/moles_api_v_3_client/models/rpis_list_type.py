from enum import Enum


class RpisListType(str, Enum):
    INDIVIDUAL = "individual"
    ORGANISATION = "organisation"

    def __str__(self) -> str:
        return str(self.value)
