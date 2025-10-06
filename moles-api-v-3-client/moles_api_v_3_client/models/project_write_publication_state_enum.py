from enum import Enum


class ProjectWritePublicationStateEnum(str, Enum):
    OLD = "old"
    PREVIEW = "preview"
    PUBLISHED = "published"
    REMOVED = "removed"
    WORKING = "working"

    def __str__(self) -> str:
        return str(self.value)
