import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime as Datetime

from .samplereferenceset import SampleReferenceSet
from .parentdatapointreferenceset import ParentDataPointReferenceSet
from .experimentdatareferenceset import ExperimentDataReferenceSet


@forge_signature
class Infrastructure(sdRDM.DataModel):

    """Contains references to the context of this Experiment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("infrastructureINDEX"),
        xml="@id",
    )

    sample_reference_set: Optional[SampleReferenceSet] = Field(
        default=None,
        description="Set of Samples used in this Experiment.",
        xml="SampleReferenceSet",
    )

    parent_data_point_reference_set: Optional[ParentDataPointReferenceSet] = Field(
        default=None,
        description="Contains references to the parent Result.",
        xml="ParentDataPointReferenceSet",
    )

    experiment_data_reference_set: Optional[ExperimentDataReferenceSet] = Field(
        default=None,
        description="Set of Experiment Steps consumed by this Experiment Step.",
        xml="ExperimentDataReferenceSet",
    )

    timestamp: Optional[Datetime] = Field(
        default=None,
        description="Date and time of modification.",
        xml="Timestamp",
    )
