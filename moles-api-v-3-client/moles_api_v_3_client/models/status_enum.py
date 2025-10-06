from enum import Enum


class StatusEnum(str, Enum):
    COMPLETED = "completed"
    DEPRECATED = "deprecated"
    FINAL = "final"
    HISTORICALARCHIVE = "historicalArchive"
    OBSOLETE = "obsolete"
    ONGOING = "ongoing"
    PENDING = "pending"
    PLANNED = "planned"
    REQUIRED = "required"
    RETIRED = "retired"
    SUPERSEDED = "superseded"
    TENTATIVE = "tentative"
    UNDERDEVELOPMENT = "underDevelopment"
    WITHDRAWN = "withdrawn"

    def __str__(self) -> str:
        return str(self.value)
