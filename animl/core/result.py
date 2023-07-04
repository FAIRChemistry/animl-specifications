import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .seriesset import SeriesSet
from .category import Category
from .parameter import Parameter


@forge_signature
class Result(sdRDM.DataModel):

    """Container for Data derived from Experiment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("resultINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    id: Optional[str] = Field(
        default=None,
        description=(
            "Anchor point for digital signature. This identifier is referred to from"
            " the 'Reference' element in a Signature. Unique per document."
        ),
        xml="@id",
    )

    series_set: Optional[SeriesSet] = Field(
        default=None,
        description="Container for n-dimensional Data.",
        xml="SeriesSet",
    )

    category: List[Category] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Defines a category of Parameters and SeriesSets. Used to model"
            " hierarchies."
        ),
        xml="Category",
    )

    def add_to_category(
        self,
        name: str,
        id: Optional[str] = None,
        parameter: List[Parameter] = ListPlus(),
        series_set: List[SeriesSet] = ListPlus(),
        category: List[Category] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Category' to attribute category

        Args:
            id (str): Unique identifier of the 'Category' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            id (): Anchor point for digital signature. This identifier is referred to from the 'Reference' element in a Signature. Unique per document.. Defaults to None
            parameter (): Name/Value Pair.. Defaults to ListPlus()
            series_set (): Container for n-dimensional Data.. Defaults to ListPlus()
            category (): Defines a category of Parameters and SeriesSets. Used to model hierarchies.. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "id": id,
            "parameter": parameter,
            "series_set": series_set,
            "category": category,
        }

        if id is not None:
            params["id"] = id

        self.category.append(Category(**params))

        return self.category[-1]
