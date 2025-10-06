from enum import Enum


class OnlineresourcesListFunction(str, Enum):
    APPLYFORACCESS = "applyForAccess"
    DATASERVICE = "dataService"
    DOCUMENTATION = "documentation"
    DOWNLOAD = "download"
    EXTERNALCITATION = "externalCitation"
    IMAGE = "image"
    LOGO = "logo"
    METADATA = "metadata"
    OFFLINEACCESS = "offlineAccess"
    SEARCH = "search"

    def __str__(self) -> str:
        return str(self.value)
