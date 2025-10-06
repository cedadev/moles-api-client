from enum import Enum


class PlatformTypeEnum(str, Enum):
    AIRCRAFT = "aircraft"
    BALLOON = "balloon"
    COMPUTER = "computer"
    LAND_STATION = "land_station"
    MOORING = "mooring"
    MOVING_PLATFORM = "moving_platform"
    SATELLITE = "satellite"
    SHIP = "ship"
    STATIONARY_PLATFORM = "stationary_platform"
    STATION_GROUP = "station_group"
    UAS = "uas"
    UNDEFINED = "UNDEFINED"

    def __str__(self) -> str:
        return str(self.value)
