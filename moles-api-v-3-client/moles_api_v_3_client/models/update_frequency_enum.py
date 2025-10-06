from enum import Enum


class UpdateFrequencyEnum(str, Enum):
    ANNUALLY = "annually"
    ASNEEDED = "asNeeded"
    BIANNUALLY = "biannually"
    CONTINUAL = "continual"
    DAILY = "daily"
    FORTNIGHTLY = "fortnightly"
    IRREGULAR = "irregular"
    MONTHLY = "monthly"
    NOTPLANNED = "notPlanned"
    QUARTERLY = "quarterly"
    UNKNOWN = "unknown"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
