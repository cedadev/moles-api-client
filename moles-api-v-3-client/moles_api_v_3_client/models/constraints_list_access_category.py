from enum import Enum


class ConstraintsListAccessCategory(str, Enum):
    PUBLIC = "public"
    REGISTERED = "registered"
    RESTRICTED = "restricted"

    def __str__(self) -> str:
        return str(self.value)
