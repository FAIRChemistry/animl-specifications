import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .endvalue import EndValue
from .startvalue import StartValue
from .parentdatapointreference import ParentDataPointReference


@forge_signature
class ParentDataPointReferenceSet(sdRDM.DataModel):

    """Contains references to the parent Result."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("parentdatapointreferencesetINDEX"),
        xml="@id",
    )

    parent_data_point_reference: List[ParentDataPointReference] = Field(
        multiple=True,
        description=(
            "Reference to a data point or value range in an independent Series in the"
            " parent Result."
        ),
        xml="ParentDataPointReference",
        default_factory=ListPlus,
    )

    def add_to_parent_data_point_reference(
        self,
        series_id: str,
        start_value: StartValue,
        id: Optional[str] = None,
        end_value: Optional[EndValue] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ParentDataPointReference' to attribute parent_data_point_reference

        Args:
            id (str): Unique identifier of the 'ParentDataPointReference' object. Defaults to 'None'.
            series_id (): Contains the ID of the Series referenced..
            start_value (): Lower boundary of an interval or ValueSet..
            id (): Anchor point for digital signature. This identifier is referred to from the 'Reference' element in a Signature. Unique per document.. Defaults to None
            end_value (): Upper boundary of an interval.. Defaults to None
        """

        params = {
            "series_id": series_id,
            "start_value": start_value,
            "id": id,
            "end_value": end_value,
        }

        if id is not None:
            params["id"] = id

        self.parent_data_point_reference.append(ParentDataPointReference(**params))

        return self.parent_data_point_reference[-1]
