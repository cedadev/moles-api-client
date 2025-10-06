from enum import Enum


class InstrumentTypeEnum(str, Enum):
    ANEMOMETER = "anemometer"
    ASOZ = "asoz"
    FAGE = "fage"
    FILTER = "filter"
    GAS_CHROMATOGRAPH = "gas_chromatograph"
    IMAGER = "imager"
    INSTRUMENT = "instrument"
    LIDAR = "lidar"
    MASS_SPECTROMETER = "mass_spectrometer"
    MET_SENSOR = "met_sensor"
    MODEL = "model"
    NAVIGATION = "navigation"
    OTHER_INSTRUMENT_TYPE = "other_instrument_type"
    PARTICLE_COUNTER = "particle_counter"
    RADAR = "radar"
    RADIOMETER = "radiometer"
    RAINGUAGE = "rainguage"
    SAMPLER = "sampler"
    SONDE = "sonde"
    SPECTROMETER = "spectrometer"
    UNDEFINED = "UNDEFINED"

    def __str__(self) -> str:
        return str(self.value)
