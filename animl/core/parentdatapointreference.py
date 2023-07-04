import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


from .endvalue import EndValue
from .startvalue import StartValue


@forge_signature
class ParentDataPointReference(sdRDM.DataModel):

    """Reference to a data point or value range in an independent Series in the parent Result."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("parentdatapointreferenceINDEX"),
        xml="@id",
    )

    series_id: str = Field(
        ...,
        description="Contains the ID of the Series referenced.",
        xml="@seriesID",
    )

    start_value: StartValue = Field(
        ...,
        description="Lower boundary of an interval or ValueSet.",
        xml="StartValue",
    )

    id: Optional[str] = Field(
        default=None,
        description=(
            "Anchor point for digital signature. This identifier is referred to from"
            " the 'Reference' element in a Signature. Unique per document."
        ),
        xml="@id",
    )

    end_value: Optional[EndValue] = Field(
        default=None,
        description="Upper boundary of an interval.",
        xml="EndValue",
    )
