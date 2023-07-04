import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .infrastructure import Infrastructure
from .method import Method
from .technique import Technique
from .tagset import TagSet
from .seriesset import SeriesSet
from .result import Result
from .category import Category


@forge_signature
class Template(sdRDM.DataModel):

    """Represents a template for an ExperimentStep."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("templateINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    template_id: str = Field(
        ...,
        description="None",
        xml="@templateID",
    )

    id: Optional[str] = Field(
        default=None,
        description=(
            "Anchor point for digital signature. This identifier is referred to from"
            " the 'Reference' element in a Signature. Unique per document."
        ),
        xml="@id",
    )

    source_data_location: Optional[str] = Field(
        default=None,
        description=(
            "Points to the original data source. May be a file name, uri, database ID,"
            " etc."
        ),
        xml="@sourceDataLocation",
    )

    tag_set: Optional[TagSet] = Field(
        default=None,
        description="Set of Tag elements.",
        xml="TagSet",
    )

    technique: Optional[Technique] = Field(
        default=None,
        description="Reference to Technique Definition used in this Experiment.",
        xml="Technique",
    )

    infrastructure: Optional[Infrastructure] = Field(
        default=None,
        description="Contains references to the context of this Experiment.",
        xml="Infrastructure",
    )

    method: Optional[Method] = Field(
        default=None,
        description="Describes how this Experiment was performed.",
        xml="Method",
    )

    result: List[Result] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Container for Data derived from Experiment.",
        xml="Result",
    )

    def add_to_result(
        self,
        name: str,
        id: Optional[str] = None,
        series_set: Optional[SeriesSet] = None,
        category: List[Category] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Result' to attribute result

        Args:
            id (str): Unique identifier of the 'Result' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            id (): Anchor point for digital signature. This identifier is referred to from the 'Reference' element in a Signature. Unique per document.. Defaults to None
            series_set (): Container for n-dimensional Data.. Defaults to None
            category (): Defines a category of Parameters and SeriesSets. Used to model hierarchies.. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "id": id,
            "series_set": series_set,
            "category": category,
        }

        if id is not None:
            params["id"] = id

        self.result.append(Result(**params))

        return self.result[-1]
