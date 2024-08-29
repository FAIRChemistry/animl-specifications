---
repo: "https://www.github.com/FAIRChemistry/animl-specifications"
--- 

# Analytical Information Markup Language

An AnIML file (also called an instance in XML speak) is an XML representation of a piece of analytical data gathered from an instrument. The format of AnIML files is structured based off of a set of rules - a schema file (see 'Core Schema'). The schema dictates the elements (tags) allowed in the file, the data type of the information in the elements, and even (if required) what values are allowed within an element. If an AnIML file is written in accordance with the published schema it is said to be 'a valid instance file'.

## Core Objects

### AnIML

ComplexType for the root element of an AnIML document.

- **version**
  - Type: string
  - Description: Version number of the AnIML Core Schema used in this document. Must be '0.90'.
  - Default: 0.90
  - XML: @version
- sample_set
  - Type: SampleSet
  - Description: Container for Samples used in this AnIML document.
  - XML: SampleSet
- experiment_step_set
  - Type: ExperimentStepSet
  - Description: Container for multiple ExperimentSteps that describe the process and results.
  - XML: ExperimentStepSet
- audit_trail_entry_set
  - Type: AuditTrailEntrySet
  - Description: Container for audit trail entries describing changes to this document.
  - XML: AuditTrailEntrySet

### SampleSet

Container for Samples used in this AnIML document.

- sample
  - Type: Sample[]
  - Description: Individual Sample, referenced from other parts of this AnIML document.
  - XML: Sample

### AuditTrailEntrySet

Container for audit trail entries describing changes to this document.

- audit_trail_entry
  - Type: AuditTrailEntry[]
  - Description: Describes a set of changes made to the particular AnIML document by one user at a given time.
  - XML: AuditTrailEntry

### ExperimentStepSet

Container for multiple ExperimentSteps that describe the process and results.

- experiment_step
  - Type: ExperimentStep[]
  - Description: Container that documents a step in an experiment. Use one ExperimentStep per application of a Technique.
  - XML: ExperimentStep
- template
  - Type: Template[]
  - Description: Represents a template for an ExperimentStep.
  - XML: Template

### Sample

Individual Sample, referenced from other parts of this AnIML document.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **sample_id**
  - Type: string
  - Description: None
  - XML: @sampleID
- barcode
  - Type: string
  - Description: Value of barcode label that is attached to sample container.
  - XML: @barcode
- comment
  - Type: string
  - Description: Unstructured text comment to further describe the Sample.
  - XML: @comment
- derived
  - Type: string
  - Description: Indicates whether this is a derived Sample. A derived Sample is a Sample that has been created by applying a Technique. (Sub-Sampling, Processing, ...)
  - XML: @derived
- container_type
  - Type: string
  - Description: Whether this sample is also a container for other samples. Set to 'simple' if not.
  - XML: @containerType
- container_id
  - Type: string
  - Description: Sample ID of container in which this sample is located.
  - XML: @containerID
- location_in_container
  - Type: string
  - Description: Coordinates of this sample within the enclosing container. In case of microplates or trays, the row is identified by letters and the column is identified by numbers (1-based) while in landscape orientation. Examples: A10 = 1st row, 10th column, Z1 = 26th row, 1st column, AB2 = 28th row, 2nd column.
  - XML: @locationInContainer
- source_data_location
  - Type: string
  - Description: Points to the original data source. May be a file name, uri, database ID, etc.
  - XML: @sourceDataLocation
- tag_set
  - Type: TagSet
  - Description: Set of Tag elements.
  - XML: TagSet
- category
  - Type: Category[]
  - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
  - XML: Category

### AuditTrailEntry

Describes a set of changes made to the particular AnIML document by one user at a given time.

- **timestamp**
  - Type: string
  - Description: Date and time of modification.
  - XML: Timestamp
- **author**
  - Type: Author
  - Description: Information about a person, a device or a piece of software authoring AnIML files.
  - XML: Author
- **action**
  - Type: string
  - Description: Type of change made (created, modified, ...)
  - XML: Action
- software
  - Type: Software
  - Description: Software used to author this.
  - XML: Software
- reason
  - Type: string
  - Description: Explanation why changes were made.
  - XML: Reason
- comment
  - Type: string
  - Description: Human-readable comment further explaining the changes.
  - XML: Comment
- diff
  - Type: Diff[]
  - Description: Machine-readable description of changes made.
  - XML: Diff
- reference
  - Type: string[]
  - Description: ID of the SignableItem that was affected. If none is specified, entire document is covered.
  - XML: Reference

### Template

Represents a template for an ExperimentStep.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **template_id**
  - Type: string
  - Description: None
  - XML: @templateID
- source_data_location
  - Type: string
  - Description: Points to the original data source. May be a file name, uri, database ID, etc.
  - XML: @sourceDataLocation
- tag_set
  - Type: TagSet
  - Description: Set of Tag elements.
  - XML: TagSet
- technique
  - Type: Technique
  - Description: Reference to Technique Definition used in this Experiment.
  - XML: Technique
- infrastructure
  - Type: Infrastructure
  - Description: Contains references to the context of this Experiment.
  - XML: Infrastructure
- method
  - Type: Method
  - Description: Describes how this Experiment was performed.
  - XML: Method
- result
  - Type: Result[]
  - Description: Container for Data derived from Experiment.
  - XML: Result

### ExperimentStep

Container that documents a step in an experiment. Use one ExperimentStep per application of a Technique.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **experiment_step_id**
  - Type: string
  - Description: Unique identifier for this ExperimentStep. Used to point to this step from an ExperimentDataReference.
  - XML: @experimentStepID
- template_used
  - Type: string
  - Description: None
  - XML: @templateUsed
- comment
  - Type: string
  - Description: Unstructured text comment to further describe the ExperimentStep.
  - XML: @comment
- source_data_location
  - Type: string
  - Description: Points to the original data source. May be a file name, uri, database ID, etc.
  - XML: @sourceDataLocation
- tag_set
  - Type: TagSet
  - Description: Set of Tag elements.
  - XML: TagSet
- technique
  - Type: Technique
  - Description: Reference to Technique Definition used in this Experiment.
  - XML: Technique
- infrastructure
  - Type: Infrastructure
  - Description: Contains references to the context of this Experiment.
  - XML: Infrastructure
- method
  - Type: Method
  - Description: Describes how this Experiment was performed.
  - XML: Method
- result
  - Type: Result[]
  - Description: Container for Data derived from Experiment.
  - XML: Result

### Diff

Machine-readable description of changes made.

- **scope**
  - Type: string
  - Description: Scope of diff. May be 'element' or 'attribute'.
  - XML: @scope
- **changed_item**
  - Type: string
  - Description: ID of the SignableItem that was changed
  - XML: @changedItem
- **old_value**
  - Type: string
  - Description: No descripiton provided
  - XML: OldValue
- **new_value**
  - Type: string
  - Description: No descripiton provided
  - XML: NewValue

### Author

Information about a person, a device or a piece of software authoring AnIML files.

- **user_type**
  - Type: string
  - Description: Type of user (human, device, software)
  - XML: @userType
- **name**
  - Type: string
  - Description: Common name.
  - XML: Name
- affiliation
  - Type: string
  - Description: Organization the Author is affiliated with.
  - XML: Affiliation
- role
  - Type: string
  - Description: Role the Author plays within the organization.
  - XML: Role
- email
  - Type: string
  - Description: RFC822-compliant email address.
  - XML: Email
- phone
  - Type: string
  - Description: Phone number.
  - XML: Phone
- location
  - Type: string
  - Description: Location or physical address.
  - XML: Location

### Software

Software used to author this.

- **name**
  - Type: string
  - Description: Common name.
  - XML: Name
- manufacturer
  - Type: string
  - Description: Company name.
  - XML: Manufacturer
- version
  - Type: string
  - Description: Version identifier of software release.
  - XML: Version
- operating_system
  - Type: string
  - Description: Operating system the software was running on.
  - XML: OperatingSystem

### TagSet

Set of Tag elements.

- tag
  - Type: Tag[]
  - Description: Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system.
  - XML: Tag

### Result

Container for Data derived from Experiment.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- series_set
  - Type: SeriesSet
  - Description: Container for n-dimensional Data.
  - XML: SeriesSet
- category
  - Type: Category[]
  - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
  - XML: Category

### Method

Describes how this Experiment was performed.

- name
  - Type: string
  - Description: Optional method name, as defined in the instrument software.
  - XML: @name
- author
  - Type: Author
  - Description: Information about a person, a device or a piece of software authoring AnIML files.
  - XML: Author
- device
  - Type: Device
  - Description: Device used to perform experiment.
  - XML: Device
- software
  - Type: Software
  - Description: Software used to author this.
  - XML: Software
- category
  - Type: Category[]
  - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
  - XML: Category

### Technique

Reference to Technique Definition used in this Experiment.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **uri**
  - Type: string
  - Description: URI where Technique Definition file can be fetched.
  - XML: @uri
- sha256
  - Type: string
  - Description: SHA256 checksum of the referenced Technique Definition. Hex encoded, lower cased. Similar to the output of the sha256 unix command.
  - XML: @sha256
- extension
  - Type: Extension[]
  - Description: Reference to an Extension to amend the active Technique Definition.
  - XML: Extension

### Infrastructure

Contains references to the context of this Experiment.

- sample_reference_set
  - Type: SampleReferenceSet
  - Description: Set of Samples used in this Experiment.
  - XML: SampleReferenceSet
- parent_data_point_reference_set
  - Type: ParentDataPointReferenceSet
  - Description: Contains references to the parent Result.
  - XML: ParentDataPointReferenceSet
- experiment_data_reference_set
  - Type: ExperimentDataReferenceSet
  - Description: Set of Experiment Steps consumed by this Experiment Step.
  - XML: ExperimentDataReferenceSet
- timestamp
  - Type: string
  - Description: Date and time of modification.
  - XML: Timestamp

### Tag

Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system.

- **name**
  - Type: string
  - Description: None
  - XML: @name
- value
  - Type: string
  - Description: None
  - XML: @value

### Category

Defines a category of Parameters and SeriesSets. Used to model hierarchies.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- parameter
  - Type: Parameter[]
  - Description: Name/Value Pair.
  - XML: Parameter
- series_set
  - Type: SeriesSet[]
  - Description: Container for n-dimensional Data.
  - XML: SeriesSet
- category
  - Type: Category[]
  - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
  - XML: Category

### Device

Device used to perform experiment.

- **name**
  - Type: string
  - Description: Common name.
  - XML: Name
- device_identifier
  - Type: string
  - Description: Unique name or identifier of the device.
  - XML: DeviceIdentifier
- manufacturer
  - Type: string
  - Description: Company name.
  - XML: Manufacturer
- firmware_version
  - Type: string
  - Description: Version identifier of firmware release.
  - XML: FirmwareVersion
- serial_number
  - Type: string
  - Description: Unique serial number of device.
  - XML: SerialNumber

### Extension

Reference to an Extension to amend the active Technique Definition.

- **uri**
  - Type: string
  - Description: URI where Extension file can be fetched.
  - XML: @uri
- **name**
  - Type: string
  - Description: Name of Extension to be used. Must match Name given in Extension Definition file.
  - XML: @name
- sha256
  - Type: string
  - Description: SHA256 checksum of the referenced Extension. Hex encoded, lower cased. Similar to the output of the sha256 unix command.
  - XML: @sha256

### ExperimentDataReferenceSet

Set of Experiment Steps consumed by this Experiment Step.

- experiment_data_reference
  - Type: ExperimentDataReference[]
  - Description: Reference to an Experiment Step whose data is consumed.
  - XML: ExperimentDataReference
- experiment_data_bulk_reference
  - Type: ExperimentDataBulkReference[]
  - Description: Prefix-based reference to a set of Experiment Steps whose data are consumed.
  - XML: ExperimentDataBulkReference

### ParentDataPointReferenceSet

Contains references to the parent Result.

- **parent_data_point_reference**
  - Type: ParentDataPointReference[]
  - Description: Reference to a data point or value range in an independent Series in the parent Result.
  - XML: ParentDataPointReference

### SampleReferenceSet

Set of Samples used in this Experiment.

- sample_reference
  - Type: SampleReference[]
  - Description: Reference to a Sample used in this Experiment.
  - XML: SampleReference
- sample_inheritance
  - Type: SampleInheritance[]
  - Description: Indicates that a Sample was inherited from the parent ExperimentStep.
  - XML: SampleInheritance

### SeriesSet

Container for n-dimensional Data.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **length**
  - Type: string
  - Description: Number of data points each Series contains.
  - XML: @length
- **series**
  - Type: Series[]
  - Description: Container for multiple Values.
  - XML: Series

### Parameter

Name/Value Pair.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **parameter_type**
  - Type: string
  - Description: Data type of this parameter
  - XML: @parameterType
- **value**
  - Type: Entry[](#entry)
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value. string: Individual ISO date/time value. PNG: Base 64 encoded PNG image. EmbeddedXML: Value governed by a different XML Schema. SVG: Value governed by the SVG DTD. Used to represent vector graphic images.
- unit
  - Type: Unit
  - Description: Unit: Definition of a Scientific Unit.
  - XML: Unit: Unit

### ExperimentDataReference

Reference to an Experiment Step whose data is consumed.

- **role**
  - Type: string
  - Description: None
  - XML: @role
- **data_purpose**
  - Type: string
  - Description: None
  - XML: @dataPurpose
- **experiment_step_id**
  - Type: string
  - Description: None
  - XML: @experimentStepID

### ExperimentDataBulkReference

Prefix-based reference to a set of Experiment Steps whose data are consumed.

- **role**
  - Type: string
  - Description: None
  - XML: @role
- **data_purpose**
  - Type: string
  - Description: None
  - XML: @dataPurpose
- **experiment_step_id_prefix**
  - Type: string
  - Description: None
  - XML: @experimentStepIDPrefix

### ParentDataPointReference

Reference to a data point or value range in an independent Series in the parent Result.

- **series_id**
  - Type: string
  - Description: Contains the ID of the Series referenced.
  - XML: @seriesID
- **start_value**
  - Type: StartValue
  - Description: Lower boundary of an interval or ValueSet.
  - XML: StartValue
- end_value
  - Type: EndValue
  - Description: Upper boundary of an interval.
  - XML: EndValue

### SampleReference

Reference to a Sample used in this Experiment.

- **sample_id**
  - Type: string
  - Description: SampleID of the Sample used in the current ExperimentStep. Refers to the sampleID within the SampleSet section of the document.
  - XML: @sampleID
- **role**
  - Type: string
  - Description: Role this sample plays within the current ExperimentStep.
  - XML: @role
- **sample_purpose**
  - Type: string
  - Description: Specifies whether the referenced sample is produced or consumed by the current ExperimentStep.
  - XML: @samplePurpose

### SampleInheritance

Indicates that a Sample was inherited from the parent ExperimentStep.

- **role**
  - Type: string
  - Description: Role this sample plays within the current ExperimentStep.
  - XML: @role
- **sample_purpose**
  - Type: string
  - Description: Specifies whether the referenced sample is produced or consumed by the current ExperimentStep.
  - XML: @samplePurpose

### Series

Container for multiple Values.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **dependency**
  - Type: string
  - Description: Specified whether the Series is independent or dependent.
  - XML: @dependency
- **series_id**
  - Type: string
  - Description: Identifies the Series. Used in References from subordinate ExperimentSteps. Unique per SeriesSet.
  - XML: @seriesID
- **series_type**
  - Type: string
  - Description: Data type used by all values in this Series.
  - XML: @seriesType
- visible
  - Type: string
  - Description: Specifies whether data in this Series is to be displayed to the user by default.
  - XML: @visible
- plot_scale
  - Type: string
  - Description: Specifies whether the data in this Series is typically plotted on a linear or logarithmic scale.
  - XML: @plotScale
- value_set
  - Type: SetEntry
  - Description: IndividualValueSet: Multiple Values explicitly specified. EncodedValueSet: Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order. AutoIncrementedValueSet: Multiple values given in form of a start value and an increment.
- unit
  - Type: Unit
  - Description: Definition of a Scientific Unit.
  - XML: Unit

### SIUnit

Combination of SI Units used to represent Scientific unit

- factor
  - Type: string
  - Description: None
  - XML: @factor
- exponent
  - Type: string
  - Description: None
  - XML: @exponent
- offset
  - Type: string
  - Description: None
  - XML: @offset

### EndValue

Upper boundary of an interval.

- **value**
  - Type: Entry[](#entry)
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.

### IndividualValueSet

Multiple Values explicitly specified.

- **values**
  - Type: Entry[]
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value. string: Individual ISO date/time value. PNG: Base 64 encoded PNG image. EmbeddedXML: Value governed by a different XML Schema. SVG: Value governed by the SVG DTD. Used to represent vector graphic images.
- start_index
  - Type: string
  - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
  - XML: @startIndex
- end_index
  - Type: string
  - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
  - XML: @endIndex

### Unit

Definition of a Scientific Unit.

- **label**
  - Type: string
  - Description: Defines the visual representation of a particular Unit.
  - XML: @label
- quantity
  - Type: string
  - Description: Quantity the unit can be applied to
  - XML: @quantity
- si_unit
  - Type: SIUnit[]
  - Description: Combination of SI Units used to represent Scientific unit
  - XML: SIUnit

### AutoIncrementedValueSet

Multiple values given in form of a start value and an increment.

- **start_value**
  - Type: StartValue
  - Description: Lower boundary of an interval or ValueSet.
  - XML: StartValue
- **increment**
  - Type: Increment
  - Description: Increment value
  - XML: Increment
- start_index
  - Type: string
  - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
  - XML: @startIndex
- end_index
  - Type: string
  - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
  - XML: @endIndex

### EncodedValueSet

Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order.

- start_index
  - Type: string
  - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
  - XML: @startIndex
- end_index
  - Type: string
  - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
  - XML: @endIndex

### StartValue

Lower boundary of an interval or ValueSet.

- **value**
  - Type: Entry[](#entry)
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.

### Increment

Increment value

- **value**
  - Type: Entry[](#entry)
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.
 
 ### Entry

 Custom type to represent a value in a parameter

- an_integer
  - Type: integer
  - XML: I
- a_floating_point
  - Type: float
  - XML: F
- a_string
  - Type: string
  - XML: S
- a_date_string
  - Type: string
  - XML: string
- a_boolean
  - Type: boolean
  - XML: Boolean
- a_png
  - Type: string
  - XML: PNG
- an_svg
  - Type: string
  - XML: SVG

### SetEntry

Custom type to represent value in a series

- an_individual_value_set
  - Type: IndividualValueSet
  - XML: IndividualValueSet
- an_encoded_value_set
  - Type: EncodedValueSet
  - XML: EncodedValueSet
- an_auto_incremented_value_set
  - Type: AutoIncrementedValueSet
  - XML: AutoIncrementedValueSet
