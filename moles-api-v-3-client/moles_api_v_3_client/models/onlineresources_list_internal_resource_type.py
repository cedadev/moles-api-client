from enum import Enum


class OnlineresourcesListInternalResourceType(str, Enum):
    DATAMANAGEMENTPLAN = "dataManagementPlan"
    FATCAT = "fatCat"
    SAMPLEDATALINK = "sampleDataLink"

    def __str__(self) -> str:
        return str(self.value)
