## This is a generated file. Do not modify it manually!

from __future__ import annotations
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Generic, TypeVar
from enum import Enum
from uuid import uuid4
from datetime import date, datetime

# Filter Wrapper definition used to filter a list of objects
# based on their attributes
Cls = TypeVar("Cls")

class FilterWrapper(Generic[Cls]):
    """Wrapper class to filter a list of objects based on their attributes"""

    def __init__(self, collection: list[Cls], **kwargs):
        self.collection = collection
        self.kwargs = kwargs

    def filter(self) -> list[Cls]:
        for key, value in self.kwargs.items():
            self.collection = [
                item for item in self.collection if self._fetch_attr(key, item) == value
            ]
        return self.collection

    def _fetch_attr(self, name: str, item: Cls):
        try:
            return getattr(item, name)
        except AttributeError:
            raise AttributeError(f"{item} does not have attribute {name}")


# JSON-LD Helper Functions
def add_namespace(obj, prefix: str | None, iri: str | None):
    """Adds a namespace to the JSON-LD context

    Args:
        prefix (str): The prefix to add
        iri (str): The IRI to add
    """
    if prefix is None and iri is None:
        return
    elif prefix and iri is None:
        raise ValueError("If prefix is provided, iri must also be provided")
    elif iri and prefix is None:
        raise ValueError("If iri is provided, prefix must also be provided")

    obj.ld_context[prefix] = iri # type: ignore

def validate_prefix(term: str | dict, prefix: str):
    """Validates that a term is prefixed with a given prefix

    Args:
        term (str): The term to validate
        prefix (str): The prefix to validate against

    Returns:
        bool: True if the term is prefixed with the prefix, False otherwise
    """

    if isinstance(term, dict) and not term["@id"].startswith(prefix + ":"):
        raise ValueError(f"Term {term} is not prefixed with {prefix}")
    elif isinstance(term, str) and not term.startswith(prefix + ":"):
        raise ValueError(f"Term {term} is not prefixed with {prefix}")

# Model Definitions

class AnIML(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    version: str = 0.9
    sample_set: Optional[SampleSet] = Field(default=None)
    experiment_step_set: Optional[ExperimentStepSet] = Field(default=None)
    audit_trail_entry_set: Optional[AuditTrailEntrySet] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:AnIML/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:AnIML",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class SampleSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    sample: list[Sample] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:SampleSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:SampleSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_sample(self, **kwargs) -> list[Sample]:
        """Filters the sample attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Sample]: The filtered list of Sample objects
        """

        return FilterWrapper[Sample](self.sample, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_sample(
        self,
        name: str,
        sample_id: str,
        barcode: Optional[str]= None,
        comment: Optional[str]= None,
        derived: Optional[str]= None,
        container_type: Optional[str]= None,
        container_id: Optional[str]= None,
        location_in_container: Optional[str]= None,
        source_data_location: Optional[str]= None,
        tag_set: Optional[TagSet]= None,
        category: list[Category]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "sample_id": sample_id,
            "barcode": barcode,
            "comment": comment,
            "derived": derived,
            "container_type": container_type,
            "container_id": container_id,
            "location_in_container": location_in_container,
            "source_data_location": source_data_location,
            "tag_set": tag_set,
            "category": category
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.sample.append(
            Sample(**params)
        )

        return self.sample[-1]

class AuditTrailEntrySet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    audit_trail_entry: list[AuditTrailEntry] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:AuditTrailEntrySet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:AuditTrailEntrySet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_audit_trail_entry(self, **kwargs) -> list[AuditTrailEntry]:
        """Filters the audit_trail_entry attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[AuditTrailEntry]: The filtered list of AuditTrailEntry objects
        """

        return FilterWrapper[AuditTrailEntry](self.audit_trail_entry, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_audit_trail_entry(
        self,
        timestamp: str,
        author: Author,
        action: str,
        software: Optional[Software]= None,
        reason: Optional[str]= None,
        comment: Optional[str]= None,
        diff: list[Diff]= [],
        reference: list[str]= [],
        **kwargs,
    ):
        params = {
            "timestamp": timestamp,
            "author": author,
            "action": action,
            "software": software,
            "reason": reason,
            "comment": comment,
            "diff": diff,
            "reference": reference
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.audit_trail_entry.append(
            AuditTrailEntry(**params)
        )

        return self.audit_trail_entry[-1]

class ExperimentStepSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    experiment_step: list[ExperimentStep] = Field(default_factory=list)
    template: list[Template] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:ExperimentStepSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:ExperimentStepSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_experiment_step(self, **kwargs) -> list[ExperimentStep]:
        """Filters the experiment_step attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[ExperimentStep]: The filtered list of ExperimentStep objects
        """

        return FilterWrapper[ExperimentStep](self.experiment_step, **kwargs).filter()

    def filter_template(self, **kwargs) -> list[Template]:
        """Filters the template attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Template]: The filtered list of Template objects
        """

        return FilterWrapper[Template](self.template, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_experiment_step(
        self,
        name: str,
        experiment_step_id: str,
        template_used: Optional[str]= None,
        comment: Optional[str]= None,
        source_data_location: Optional[str]= None,
        tag_set: Optional[TagSet]= None,
        technique: Optional[Technique]= None,
        infrastructure: Optional[Infrastructure]= None,
        method: Optional[Method]= None,
        result: list[Result]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "experiment_step_id": experiment_step_id,
            "template_used": template_used,
            "comment": comment,
            "source_data_location": source_data_location,
            "tag_set": tag_set,
            "technique": technique,
            "infrastructure": infrastructure,
            "method": method,
            "result": result
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.experiment_step.append(
            ExperimentStep(**params)
        )

        return self.experiment_step[-1]


    def add_to_template(
        self,
        name: str,
        template_id: str,
        source_data_location: Optional[str]= None,
        tag_set: Optional[TagSet]= None,
        technique: Optional[Technique]= None,
        infrastructure: Optional[Infrastructure]= None,
        method: Optional[Method]= None,
        result: list[Result]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "template_id": template_id,
            "source_data_location": source_data_location,
            "tag_set": tag_set,
            "technique": technique,
            "infrastructure": infrastructure,
            "method": method,
            "result": result
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.template.append(
            Template(**params)
        )

        return self.template[-1]

class Sample(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    sample_id: str
    barcode: Optional[str] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    derived: Optional[str] = Field(default=None)
    container_type: Optional[str] = Field(default=None)
    container_id: Optional[str] = Field(default=None)
    location_in_container: Optional[str] = Field(default=None)
    source_data_location: Optional[str] = Field(default=None)
    tag_set: Optional[TagSet] = Field(default=None)
    category: list[Category] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Sample/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Sample",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_category(self, **kwargs) -> list[Category]:
        """Filters the category attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Category]: The filtered list of Category objects
        """

        return FilterWrapper[Category](self.category, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_category(
        self,
        name: str,
        parameter: list[Parameter]= [],
        series_set: list[SeriesSet]= [],
        category: list[Category]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "parameter": parameter,
            "series_set": series_set,
            "category": category
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.category.append(
            Category(**params)
        )

        return self.category[-1]

class AuditTrailEntry(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    timestamp: str
    author: Author
    action: str
    software: Optional[Software] = Field(default=None)
    reason: Optional[str] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    diff: list[Diff] = Field(default_factory=list)
    reference: list[str] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:AuditTrailEntry/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:AuditTrailEntry",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_diff(self, **kwargs) -> list[Diff]:
        """Filters the diff attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Diff]: The filtered list of Diff objects
        """

        return FilterWrapper[Diff](self.diff, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_diff(
        self,
        scope: str,
        changed_item: str,
        old_value: str,
        new_value: str,
        **kwargs,
    ):
        params = {
            "scope": scope,
            "changed_item": changed_item,
            "old_value": old_value,
            "new_value": new_value
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.diff.append(
            Diff(**params)
        )

        return self.diff[-1]


class Template(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    template_id: str
    source_data_location: Optional[str] = Field(default=None)
    tag_set: Optional[TagSet] = Field(default=None)
    technique: Optional[Technique] = Field(default=None)
    infrastructure: Optional[Infrastructure] = Field(default=None)
    method: Optional[Method] = Field(default=None)
    result: list[Result] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Template/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Template",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_result(self, **kwargs) -> list[Result]:
        """Filters the result attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Result]: The filtered list of Result objects
        """

        return FilterWrapper[Result](self.result, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_result(
        self,
        name: str,
        series_set: Optional[SeriesSet]= None,
        category: list[Category]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "series_set": series_set,
            "category": category
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.result.append(
            Result(**params)
        )

        return self.result[-1]

class ExperimentStep(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    experiment_step_id: str
    template_used: Optional[str] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    source_data_location: Optional[str] = Field(default=None)
    tag_set: Optional[TagSet] = Field(default=None)
    technique: Optional[Technique] = Field(default=None)
    infrastructure: Optional[Infrastructure] = Field(default=None)
    method: Optional[Method] = Field(default=None)
    result: list[Result] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:ExperimentStep/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:ExperimentStep",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_result(self, **kwargs) -> list[Result]:
        """Filters the result attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Result]: The filtered list of Result objects
        """

        return FilterWrapper[Result](self.result, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_result(
        self,
        name: str,
        series_set: Optional[SeriesSet]= None,
        category: list[Category]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "series_set": series_set,
            "category": category
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.result.append(
            Result(**params)
        )

        return self.result[-1]

class Diff(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    scope: str
    changed_item: str
    old_value: str
    new_value: str

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Diff/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Diff",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Author(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    user_type: str
    name: str
    affiliation: Optional[str] = Field(default=None)
    role: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    phone: Optional[str] = Field(default=None)
    location: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Author/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Author",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Software(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    manufacturer: Optional[str] = Field(default=None)
    version: Optional[str] = Field(default=None)
    operating_system: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Software/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Software",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class TagSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    tag: list[Tag] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:TagSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:TagSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_tag(self, **kwargs) -> list[Tag]:
        """Filters the tag attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Tag]: The filtered list of Tag objects
        """

        return FilterWrapper[Tag](self.tag, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_tag(
        self,
        name: str,
        value: Optional[str]= None,
        **kwargs,
    ):
        params = {
            "name": name,
            "value": value
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.tag.append(
            Tag(**params)
        )

        return self.tag[-1]

class Result(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    series_set: Optional[SeriesSet] = Field(default=None)
    category: list[Category] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Result/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Result",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_category(self, **kwargs) -> list[Category]:
        """Filters the category attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Category]: The filtered list of Category objects
        """

        return FilterWrapper[Category](self.category, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_category(
        self,
        name: str,
        parameter: list[Parameter]= [],
        series_set: list[SeriesSet]= [],
        category: list[Category]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "parameter": parameter,
            "series_set": series_set,
            "category": category
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.category.append(
            Category(**params)
        )

        return self.category[-1]

class Method(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: Optional[str] = Field(default=None)
    author: Optional[Author] = Field(default=None)
    device: Optional[Device] = Field(default=None)
    software: Optional[Software] = Field(default=None)
    category: list[Category] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Method/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Method",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_category(self, **kwargs) -> list[Category]:
        """Filters the category attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Category]: The filtered list of Category objects
        """

        return FilterWrapper[Category](self.category, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_category(
        self,
        name: str,
        parameter: list[Parameter]= [],
        series_set: list[SeriesSet]= [],
        category: list[Category]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "parameter": parameter,
            "series_set": series_set,
            "category": category
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.category.append(
            Category(**params)
        )

        return self.category[-1]

class Technique(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    uri: str
    sha256: Optional[str] = Field(default=None)
    extension: list[Extension] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Technique/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Technique",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_extension(self, **kwargs) -> list[Extension]:
        """Filters the extension attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Extension]: The filtered list of Extension objects
        """

        return FilterWrapper[Extension](self.extension, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_extension(
        self,
        uri: str,
        name: str,
        sha256: Optional[str]= None,
        **kwargs,
    ):
        params = {
            "uri": uri,
            "name": name,
            "sha256": sha256
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.extension.append(
            Extension(**params)
        )

        return self.extension[-1]

class Infrastructure(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    sample_reference_set: Optional[SampleReferenceSet] = Field(default=None)
    parent_data_point_reference_set: Optional[ParentDataPointReferenceSet] = Field(default=None)
    experiment_data_reference_set: Optional[ExperimentDataReferenceSet] = Field(default=None)
    timestamp: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Infrastructure/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Infrastructure",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Tag(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    value: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Tag/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Tag",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Category(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    parameter: list[Parameter] = Field(default_factory=list)
    series_set: list[SeriesSet] = Field(default_factory=list)
    category: list[Category] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Category/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Category",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_parameter(self, **kwargs) -> list[Parameter]:
        """Filters the parameter attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Parameter]: The filtered list of Parameter objects
        """

        return FilterWrapper[Parameter](self.parameter, **kwargs).filter()

    def filter_series_set(self, **kwargs) -> list[SeriesSet]:
        """Filters the series_set attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[SeriesSet]: The filtered list of SeriesSet objects
        """

        return FilterWrapper[SeriesSet](self.series_set, **kwargs).filter()

    def filter_category(self, **kwargs) -> list[Category]:
        """Filters the category attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Category]: The filtered list of Category objects
        """

        return FilterWrapper[Category](self.category, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_parameter(
        self,
        name: str,
        parameter_type: str,
        value: Entry,
        unit: Optional[Unit]= None,
        **kwargs,
    ):
        params = {
            "name": name,
            "parameter_type": parameter_type,
            "value": value,
            "unit": unit
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.parameter.append(
            Parameter(**params)
        )

        return self.parameter[-1]


    def add_to_series_set(
        self,
        name: str,
        length: str,
        series: list[Series]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "length": length,
            "series": series
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.series_set.append(
            SeriesSet(**params)
        )

        return self.series_set[-1]


    def add_to_category(
        self,
        name: str,
        parameter: list[Parameter]= [],
        series_set: list[SeriesSet]= [],
        category: list[Category]= [],
        **kwargs,
    ):
        params = {
            "name": name,
            "parameter": parameter,
            "series_set": series_set,
            "category": category
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.category.append(
            Category(**params)
        )

        return self.category[-1]

class Device(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    device_identifier: Optional[str] = Field(default=None)
    manufacturer: Optional[str] = Field(default=None)
    firmware_version: Optional[str] = Field(default=None)
    serial_number: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Device/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Device",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Extension(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    uri: str
    name: str
    sha256: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Extension/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Extension",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class ExperimentDataReferenceSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    experiment_data_reference: list[ExperimentDataReference] = Field(default_factory=list)
    experiment_data_bulk_reference: list[ExperimentDataBulkReference] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:ExperimentDataReferenceSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:ExperimentDataReferenceSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_experiment_data_reference(self, **kwargs) -> list[ExperimentDataReference]:
        """Filters the experiment_data_reference attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[ExperimentDataReference]: The filtered list of ExperimentDataReference objects
        """

        return FilterWrapper[ExperimentDataReference](self.experiment_data_reference, **kwargs).filter()

    def filter_experiment_data_bulk_reference(self, **kwargs) -> list[ExperimentDataBulkReference]:
        """Filters the experiment_data_bulk_reference attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[ExperimentDataBulkReference]: The filtered list of ExperimentDataBulkReference objects
        """

        return FilterWrapper[ExperimentDataBulkReference](self.experiment_data_bulk_reference, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_experiment_data_reference(
        self,
        role: str,
        data_purpose: str,
        experiment_step_id: str,
        **kwargs,
    ):
        params = {
            "role": role,
            "data_purpose": data_purpose,
            "experiment_step_id": experiment_step_id
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.experiment_data_reference.append(
            ExperimentDataReference(**params)
        )

        return self.experiment_data_reference[-1]


    def add_to_experiment_data_bulk_reference(
        self,
        role: str,
        data_purpose: str,
        experiment_step_id_prefix: str,
        **kwargs,
    ):
        params = {
            "role": role,
            "data_purpose": data_purpose,
            "experiment_step_id_prefix": experiment_step_id_prefix
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.experiment_data_bulk_reference.append(
            ExperimentDataBulkReference(**params)
        )

        return self.experiment_data_bulk_reference[-1]

class ParentDataPointReferenceSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    parent_data_point_reference: list[ParentDataPointReference] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:ParentDataPointReferenceSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:ParentDataPointReferenceSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_parent_data_point_reference(self, **kwargs) -> list[ParentDataPointReference]:
        """Filters the parent_data_point_reference attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[ParentDataPointReference]: The filtered list of ParentDataPointReference objects
        """

        return FilterWrapper[ParentDataPointReference](self.parent_data_point_reference, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_parent_data_point_reference(
        self,
        series_id: str,
        start_value: StartValue,
        end_value: Optional[EndValue]= None,
        **kwargs,
    ):
        params = {
            "series_id": series_id,
            "start_value": start_value,
            "end_value": end_value
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.parent_data_point_reference.append(
            ParentDataPointReference(**params)
        )

        return self.parent_data_point_reference[-1]

class SampleReferenceSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    sample_reference: list[SampleReference] = Field(default_factory=list)
    sample_inheritance: list[SampleInheritance] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:SampleReferenceSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:SampleReferenceSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_sample_reference(self, **kwargs) -> list[SampleReference]:
        """Filters the sample_reference attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[SampleReference]: The filtered list of SampleReference objects
        """

        return FilterWrapper[SampleReference](self.sample_reference, **kwargs).filter()

    def filter_sample_inheritance(self, **kwargs) -> list[SampleInheritance]:
        """Filters the sample_inheritance attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[SampleInheritance]: The filtered list of SampleInheritance objects
        """

        return FilterWrapper[SampleInheritance](self.sample_inheritance, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_sample_reference(
        self,
        sample_id: str,
        role: str,
        sample_purpose: str,
        **kwargs,
    ):
        params = {
            "sample_id": sample_id,
            "role": role,
            "sample_purpose": sample_purpose
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.sample_reference.append(
            SampleReference(**params)
        )

        return self.sample_reference[-1]


    def add_to_sample_inheritance(
        self,
        role: str,
        sample_purpose: str,
        **kwargs,
    ):
        params = {
            "role": role,
            "sample_purpose": sample_purpose
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.sample_inheritance.append(
            SampleInheritance(**params)
        )

        return self.sample_inheritance[-1]

class SeriesSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    length: str
    series: list[Series] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:SeriesSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:SeriesSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_series(self, **kwargs) -> list[Series]:
        """Filters the series attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[Series]: The filtered list of Series objects
        """

        return FilterWrapper[Series](self.series, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_series(
        self,
        name: str,
        dependency: str,
        series_id: str,
        series_type: str,
        visible: Optional[str]= None,
        plot_scale: Optional[str]= None,
        value_set: Optional[SetEntry]= None,
        unit: Optional[Unit]= None,
        **kwargs,
    ):
        params = {
            "name": name,
            "dependency": dependency,
            "series_id": series_id,
            "series_type": series_type,
            "visible": visible,
            "plot_scale": plot_scale,
            "value_set": value_set,
            "unit": unit
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.series.append(
            Series(**params)
        )

        return self.series[-1]

class Parameter(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    parameter_type: str
    value: Entry
    unit: Optional[Unit] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Parameter/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Parameter",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class ExperimentDataReference(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    role: str
    data_purpose: str
    experiment_step_id: str

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:ExperimentDataReference/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:ExperimentDataReference",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class ExperimentDataBulkReference(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    role: str
    data_purpose: str
    experiment_step_id_prefix: str

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:ExperimentDataBulkReference/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:ExperimentDataBulkReference",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class ParentDataPointReference(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    series_id: str
    start_value: StartValue
    end_value: Optional[EndValue] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:ParentDataPointReference/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:ParentDataPointReference",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class SampleReference(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    sample_id: str
    role: str
    sample_purpose: str

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:SampleReference/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:SampleReference",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class SampleInheritance(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    role: str
    sample_purpose: str

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:SampleInheritance/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:SampleInheritance",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Series(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    name: str
    dependency: str
    series_id: str
    series_type: str
    visible: Optional[str] = Field(default=None)
    plot_scale: Optional[str] = Field(default=None)
    value_set: Optional[SetEntry] = Field(default=None)
    unit: Optional[Unit] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Series/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Series",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class SIUnit(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    factor: Optional[str] = Field(default=None)
    exponent: Optional[str] = Field(default=None)
    offset: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:SIUnit/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:SIUnit",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class EndValue(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    value: Entry

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:EndValue/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:EndValue",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class IndividualValueSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    values: Entry
    start_index: Optional[str] = Field(default=None)
    end_index: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:IndividualValueSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:IndividualValueSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Unit(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    label: str
    quantity: Optional[str] = Field(default=None)
    si_unit: list[SIUnit] = Field(default_factory=list)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Unit/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Unit",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )

    def filter_si_unit(self, **kwargs) -> list[SIUnit]:
        """Filters the si_unit attribute based on the given kwargs

        Args:
            **kwargs: The attributes to filter by.

        Returns:
            list[SIUnit]: The filtered list of SIUnit objects
        """

        return FilterWrapper[SIUnit](self.si_unit, **kwargs).filter()


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


    def add_to_si_unit(
        self,
        factor: Optional[str]= None,
        exponent: Optional[str]= None,
        offset: Optional[str]= None,
        **kwargs,
    ):
        params = {
            "factor": factor,
            "exponent": exponent,
            "offset": offset
        }

        if "id" in kwargs:
            params["id"] = kwargs["id"]

        self.si_unit.append(
            SIUnit(**params)
        )

        return self.si_unit[-1]

class AutoIncrementedValueSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    start_value: StartValue
    increment: Increment
    start_index: Optional[str] = Field(default=None)
    end_index: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:AutoIncrementedValueSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:AutoIncrementedValueSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class EncodedValueSet(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    start_index: Optional[str] = Field(default=None)
    end_index: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:EncodedValueSet/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:EncodedValueSet",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class StartValue(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    value: Entry

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:StartValue/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:StartValue",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Increment(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    value: Entry

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Increment/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Increment",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class Entry(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    an_integer: Optional[int] = Field(default=None)
    a_floating_point: Optional[float] = Field(default=None)
    a_string: Optional[str] = Field(default=None)
    a_date_string: Optional[str] = Field(default=None)
    a_boolean: Optional[bool] = Field(default=None)
    a_png: Optional[str] = Field(default=None)
    an_svg: Optional[str] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:Entry/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:Entry",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)


class SetEntry(BaseModel):

    model_config: ConfigDict = ConfigDict( # type: ignore
        validate_assigment = True,
    ) # type: ignore

    an_individual_value_set: Optional[IndividualValueSet] = Field(default=None)
    an_encoded_value_set: Optional[EncodedValueSet] = Field(default=None)
    an_auto_incremented_value_set: Optional[AutoIncrementedValueSet] = Field(default=None)

    # JSON-LD fields
    ld_id: str = Field(
        serialization_alias="@id",
        default_factory=lambda: "md:SetEntry/" + str(uuid4())
    )
    ld_type: list[str] = Field(
        serialization_alias="@type",
        default_factory = lambda: [
            "md:SetEntry",
        ],
    )
    ld_context: dict[str, str | dict] = Field(
        serialization_alias="@context",
        default_factory = lambda: {
            "md": "https://www.github.com/FAIRChemistry/animl-specifications",
        }
    )


    def set_attr_term(
        self,
        attr: str,
        term: str | dict,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Sets the term for a given attribute in the JSON-LD object

        Example:
            # Using an IRI term
            >> obj.set_attr_term("name", "http://schema.org/givenName")

            # Using a prefix and term
            >> obj.set_attr_term("name", "schema:givenName", "schema", "http://schema.org")

            # Usinng a dictionary term
            >> obj.set_attr_term("name", {"@id": "http://schema.org/givenName", "@type": "@id"})

        Args:
            attr (str): The attribute to set the term for
            term (str | dict): The term to set for the attribute

        Raises:
            AssertionError: If the attribute is not found in the model
        """

        assert attr in self.model_fields, f"Attribute {attr} not found in {self.__class__.__name__}"

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_context[attr] = term

    def add_type_term(
        self,
        term: str,
        prefix: str | None = None,
        iri: str | None = None
    ):
        """Adds a term to the @type field of the JSON-LD object

        Example:
            # Using a term
            >> obj.add_type_term("https://schema.org/Person")

            # Using a prefixed term
            >> obj.add_type_term("schema:Person", "schema", "https://schema.org/Person")

        Args:
            term (str): The term to add to the @type field
            prefix (str, optional): The prefix to use for the term. Defaults to None.
            iri (str, optional): The IRI to use for the term prefix. Defaults to None.

        Raises:
            ValueError: If prefix is provided but iri is not
            ValueError: If iri is provided but prefix is not
        """

        if prefix:
            validate_prefix(term, prefix)

        add_namespace(self, prefix, iri)
        self.ld_type.append(term)