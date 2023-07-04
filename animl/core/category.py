import sdRDM

from typing import Optional, Union, List
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime as Datetime

from .siunit import SIUnit
from .series import Series
from .seriesset import SeriesSet
from .category import Category
from .parameter import Parameter


@forge_signature
class Category(sdRDM.DataModel):

    """Defines a category of Parameters and SeriesSets. Used to model hierarchies."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("categoryINDEX"),
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

    parameter: List[Parameter] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Name/Value Pair.",
        xml="Parameter",
    )

    series_set: List[SeriesSet] = Field(
        default_factory=ListPlus,
        multiple=True,
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

    def add_to_parameter(
        self,
        name: str,
        parameter_type: str,
        value: Union[int, float, str, bool, Datetime, bytes],
        id: Optional[str] = None,
        unit: Optional[SIUnit] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Parameter' to attribute parameter

        Args:
            id (str): Unique identifier of the 'Parameter' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            parameter_type (): Data type of this parameter.
            value (): I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value. DateTime: Individual ISO date/time value. PNG: Base 64 encoded PNG image. EmbeddedXML: Value governed by a different XML Schema. SVG: Value governed by the SVG DTD. Used to represent vector graphic images..
            id (): Anchor point for digital signature. This identifier is referred to from the 'Reference' element in a Signature. Unique per document.. Defaults to None
            unit (): SIUnit: Combination of SI Units used to represent Scientific unit. Defaults to None
        """

        params = {
            "name": name,
            "parameter_type": parameter_type,
            "value": value,
            "id": id,
            "unit": unit,
        }

        if id is not None:
            params["id"] = id

        self.parameter.append(Parameter(**params))

        return self.parameter[-1]

    def add_to_series_set(
        self,
        name: str,
        length: str,
        series: List[Series] = ListPlus(),
        id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'SeriesSet' to attribute series_set

        Args:
            id (str): Unique identifier of the 'SeriesSet' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            length (): Number of data points each Series contains..
            series (): Container for multiple Values.. Defaults to ListPlus()
            id (): Anchor point for digital signature. This identifier is referred to from the 'Reference' element in a Signature. Unique per document.. Defaults to None
        """

        params = {
            "name": name,
            "length": length,
            "series": series,
            "id": id,
        }

        if id is not None:
            params["id"] = id

        self.series_set.append(SeriesSet(**params))

        return self.series_set[-1]

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
