from enum import Enum


class ProjectsListPublicationState(str, Enum):
    OLD = "old"
    PREVIEW = "preview"
    PUBLISHED = "published"
    REMOVED = "removed"
    WORKING = "working"

    def __str__(self) -> str:
        return str(self.value)
