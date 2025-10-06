from enum import Enum


class ObservationcollectionsListPublicationState(str, Enum):
    CITABLE = "citable"
    OLD = "old"
    PREVIEW = "preview"
    PUBLISHED = "published"
    REMOVED = "removed"
    WORKING = "working"

    def __str__(self) -> str:
        return str(self.value)
