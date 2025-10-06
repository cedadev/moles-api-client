from enum import Enum


class OnlineresourcesListApplicationProfileFileFormat(str, Enum):
    CERIF = "cerif"
    CSML = "csml"
    CSV = "csv"
    GEOSCIML = "geosciml"
    NASA_AMES = "nasa_ames"
    NETCDF = "netcdf"
    VIVO = "vivo"

    def __str__(self) -> str:
        return str(self.value)
