import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .infrastructure import Infrastructure
from .method import Method
from .technique import Technique
from .experimentstep import ExperimentStep
from .tagset import TagSet
from .template import Template
from .result import Result


@forge_signature
class ExperimentStepSet(sdRDM.DataModel):

    """Container for multiple ExperimentSteps that describe the process and results."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimentstepsetINDEX"),
        xml="@id",
    )

    experiment_step: List[ExperimentStep] = Field(
        multiple=True,
        description=(
            "Container that documents a step in an experiment. Use one ExperimentStep"
            " per application of a Technique."
        ),
        xml="ExperimentStep",
        default_factory=ListPlus,
    )

    id: Optional[str] = Field(
        default=None,
        description=(
            "Anchor point for digital signature. This identifier is referred to from"
            " the 'Reference' element in a Signature. Unique per document."
        ),
        xml="@id",
    )

    template: List[Template] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Represents a template for an ExperimentStep.",
        xml="Template",
    )

    def add_to_experiment_step(
        self,
        name: str,
        experiment_step_id: str,
        id: Optional[str] = None,
        template_used: Optional[str] = None,
        comment: Optional[str] = None,
        source_data_location: Optional[str] = None,
        tag_set: Optional[TagSet] = None,
        technique: Optional[Technique] = None,
        infrastructure: Optional[Infrastructure] = None,
        method: Optional[Method] = None,
        result: List[Result] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ExperimentStep' to attribute experiment_step

        Args:
            id (str): Unique identifier of the 'ExperimentStep' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            experiment_step_id (): Unique identifier for this ExperimentStep. Used to point to this step from an ExperimentDataReference..
            id (): Anchor point for digital signature. This identifier is referred to from the 'Reference' element in a Signature. Unique per document.. Defaults to None
            template_used (): None. Defaults to None
            comment (): Unstructured text comment to further describe the ExperimentStep.. Defaults to None
            source_data_location (): Points to the original data source. May be a file name, uri, database ID, etc.. Defaults to None
            tag_set (): Set of Tag elements.. Defaults to None
            technique (): Reference to Technique Definition used in this Experiment.. Defaults to None
            infrastructure (): Contains references to the context of this Experiment.. Defaults to None
            method (): Describes how this Experiment was performed.. Defaults to None
            result (): Container for Data derived from Experiment.. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "experiment_step_id": experiment_step_id,
            "id": id,
            "template_used": template_used,
            "comment": comment,
            "source_data_location": source_data_location,
            "tag_set": tag_set,
            "technique": technique,
            "infrastructure": infrastructure,
            "method": method,
            "result": result,
        }

        if id is not None:
            params["id"] = id

        self.experiment_step.append(ExperimentStep(**params))

        return self.experiment_step[-1]

    def add_to_template(
        self,
        name: str,
        template_id: str,
        id: Optional[str] = None,
        source_data_location: Optional[str] = None,
        tag_set: Optional[TagSet] = None,
        technique: Optional[Technique] = None,
        infrastructure: Optional[Infrastructure] = None,
        method: Optional[Method] = None,
        result: List[Result] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Template' to attribute template

        Args:
            id (str): Unique identifier of the 'Template' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            template_id (): None.
            id (): Anchor point for digital signature. This identifier is referred to from the 'Reference' element in a Signature. Unique per document.. Defaults to None
            source_data_location (): Points to the original data source. May be a file name, uri, database ID, etc.. Defaults to None
            tag_set (): Set of Tag elements.. Defaults to None
            technique (): Reference to Technique Definition used in this Experiment.. Defaults to None
            infrastructure (): Contains references to the context of this Experiment.. Defaults to None
            method (): Describes how this Experiment was performed.. Defaults to None
            result (): Container for Data derived from Experiment.. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "template_id": template_id,
            "id": id,
            "source_data_location": source_data_location,
            "tag_set": tag_set,
            "technique": technique,
            "infrastructure": infrastructure,
            "method": method,
            "result": result,
        }

        if id is not None:
            params["id"] = id

        self.template.append(Template(**params))

        return self.template[-1]
