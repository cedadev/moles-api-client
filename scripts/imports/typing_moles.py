from scripts.imports.models import *
from typing import Protocol, Union
from moles_api_v_3_client.types import Response, UNSET


PartyObj = Union[
    PartyRead,
    PartyWrite
]

WriteObj = Union[
    ObservationWriteRequest,
    ResultWriteRequest,
    VerticalExtentWriteRequest,
    DQConformanceResultWriteRequest,
    TimePeriodRequest,
    GeographicBoundingBoxWriteRequest,
    OnlineResourceWriteRequest,
    ProjectWriteRequest,
    ResponsiblePartyInfoWriteRequest,
    PartyWriteRequest,
    ProcedureAcquisitionWriteRequest,
    InstrumentWriteRequest,
    ProcedureComputationWriteRequest,
    ProcedureCompositeProcessWriteRequest
]

class CreateModule(Protocol):
    def sync_detailed(self, body: object) -> Response:
        pass

class APIWriteResponse(Protocol):
    '''
    Generic typing class for objects like ObservationWrite, ProjectWrite...
    '''
    ob_id: int

class RecordCreationError(Exception):
    pass
