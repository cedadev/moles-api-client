from enum import Enum


class ObservationsListStorageLocation(str, Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
