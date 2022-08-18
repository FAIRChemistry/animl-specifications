### AnIML

ComplexType for the root element of an AnIML document.

- __version*__
    - Type: string
    - Default: "0.90"
    - Description: Version number of the AnIML Core Schema used in this document. Must be "0.90".
    - XML: @version
- __sample_set__
    - Type: [SampleSet](#SampleSet)
    - Description: Container for Samples used in this AnIML document.
    - XML: SampleSet
- __experiment_step_set__
    - Type: [ExperimentStepSet](#ExperimentStepSet)
    - Description: Container for multiple ExperimentSteps that describe the process and results.
    - XML: ExperimentStepSet
- __audit_trail_entry_set__
    - Type: [AuditTrailEntrySet](#AuditTrailEntrySet)
    - Description: Container for audit trail entries describing changes to this document.
    - XML: AuditTrailEntrySet
- __signature_set__
    - Type: [SignatureSet](#SignatureSet)
    - Description: Container for digital signatures covering parts of this AnIML document.
    - XML: SignatureSet

### SampleSet

Container for Samples used in this AnIML document.

- __sample*__
    - Type: [Sample](#Sample)
    - Multiple: True
    - Description: Individual Sample, referenced from other parts of this AnIML document.
    - XML: Sample
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id

### ExperimentStepSet

Container for multiple ExperimentSteps that describe the process and results.

- __experiment_step*__
    - Type: [ExperimentStep](#ExperimentStep)
    - Multiple: True
    - Description: Container that documents a step in an experiment. Use one ExperimentStep per application of a Technique.
    - XML: ExperimentStep
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __template__
    - Type: [Template](#Template)
    - Multiple: True
    - Description: Represents a template for an ExperimentStep.
    - XML: Template

### AuditTrailEntrySet

Container for audit trail entries describing changes to this document.

- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __audit_trail_entry__
    - Type: [AuditTrailEntry](#AuditTrailEntry)
    - Multiple: True
    - Description: Describes a set of changes made to the particular AnIML document by one user at a given time.
    - XML: AuditTrailEntry

### Sample

Individual Sample, referenced from other parts of this AnIML document.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __sample_id*__
    - Type: string
    - Description: None
    - XML: @sampleID
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __barcode__
    - Type: string
    - Description: Value of barcode label that is attached to sample container.
    - XML: @barcode
- __comment__
    - Type: string
    - Description: Unstructured text comment to further describe the Sample.
    - XML: @comment
- __derived__
    - Type: string
    - Description: Indicates whether this is a derived Sample. A derived Sample is a Sample that has been created by applying a Technique. (Sub-Sampling, Processing, ...)
    - XML: @derived
- __container_type__
    - Type: string
    - Description: Whether this sample is also a container for other samples. Set to "simple" if not.
    - XML: @containerType
- __container_id__
    - Type: string
    - Description: Sample ID of container in which this sample is located.
    - XML: @containerID
- __location_in_container__
    - Type: string
    - Description: Coordinates of this sample within the enclosing container. In case of microplates or trays, the row is identified by letters and the column is identified by numbers (1-based) while in landscape orientation. Examples: A10 = 1st row, 10th column, Z1 = 26th row, 1st column, AB2 = 28th row, 2nd column.
    - XML: @locationInContainer
- __source_data_location__
    - Type: string
    - Description: Points to the original data source. May be a file name, uri, database ID, etc.
    - XML: @sourceDataLocation
- __tag_set__
    - Type: [TagSet](#TagSet)
    - Description: Set of Tag elements.
    - XML: TagSet
- __category__
    - Type: [Category](#Category)
    - Multiple: True
    - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
    - XML: Category

### ExperimentStep

Container that documents a step in an experiment. Use one ExperimentStep per application of a Technique.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __experiment_step_id*__
    - Type: string
    - Description: Unique identifier for this ExperimentStep. Used to point to this step from an ExperimentDataReference.
    - XML: @experimentStepID
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __template_used__
    - Type: string
    - Description: None
    - XML: @templateUsed
- __comment__
    - Type: string
    - Description: Unstructured text comment to further describe the ExperimentStep.
    - XML: @comment
- __source_data_location__
    - Type: string
    - Description: Points to the original data source. May be a file name, uri, database ID, etc.
    - XML: @sourceDataLocation
- __tag_set__
    - Type: [TagSet](#TagSet)
    - Description: Set of Tag elements.
    - XML: TagSet
- __technique__
    - Type: [Technique](#Technique)
    - Description: Reference to Technique Definition used in this Experiment.
    - XML: Technique
- __infrastructure__
    - Type: [Infrastructure](#Infrastructure)
    - Description: Contains references to the context of this Experiment.
    - XML: Infrastructure
- __method__
    - Type: [Method](#Method)
    - Description: Describes how this Experiment was performed.
    - XML: Method
- __result__
    - Type: [Result](#Result)
    - Multiple: True
    - Description: Container for Data derived from Experiment.
    - XML: Result

### Template

Represents a template for an ExperimentStep.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __template_id*__
    - Type: string
    - Description: None
    - XML: @templateID
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __source_data_location__
    - Type: string
    - Description: Points to the original data source. May be a file name, uri, database ID, etc.
    - XML: @sourceDataLocation
- __tag_set__
    - Type: [TagSet](#TagSet)
    - Description: Set of Tag elements.
    - XML: TagSet
- __technique__
    - Type: [Technique](#Technique)
    - Description: Reference to Technique Definition used in this Experiment.
    - XML: Technique
- __infrastructure__
    - Type: [Infrastructure](#Infrastructure)
    - Description: Contains references to the context of this Experiment.
    - XML: Infrastructure
- __method__
    - Type: [Method](#Method)
    - Description: Describes how this Experiment was performed.
    - XML: Method
- __result__
    - Type: [Result](#Result)
    - Multiple: True
    - Description: Container for Data derived from Experiment.
    - XML: Result

### AuditTrailEntry

Describes a set of changes made to the particular AnIML document by one user at a given time.

- __timestamp*__
    - Type: datetime
    - Description: Date and time of modification.
    - XML: Timestamp
- __author*__
    - Type: [Author](#Author)
    - Description: Information about a person, a device or a piece of software authoring AnIML files.
    - XML: Author
- __action*__
    - Type: string
    - Description: Type of change made (created, modified, ...)
    - XML: Action
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __software__
    - Type: [Software](#Software)
    - Description: Software used to author this.
    - XML: Software
- __reason__
    - Type: string
    - Description: Explanation why changes were made.
    - XML: Reason
- __comment__
    - Type: string
    - Description: Human-readable comment further explaining the changes.
    - XML: Comment
- __diff__
    - Type: [Diff](#Diff)
    - Multiple: True
    - Description: Machine-readable description of changes made.
    - XML: Diff
- __reference__
    - Type: string
    - Multiple: True
    - Description: ID of the SignableItem that was affected. If none is specified, entire document is covered.
    - XML: Reference

### Result

Container for Data derived from Experiment.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __series_set__
    - Type: [SeriesSet](#SeriesSet)
    - Description: Container for n-dimensional Data.
    - XML: SeriesSet
- __category__
    - Type: [Category](#Category)
    - Multiple: True
    - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
    - XML: Category
- __experiment_step_set__
    - Type: [ExperimentStepSet](#ExperimentStepSet)
    - Description: Container for multiple ExperimentSteps that describe the process and results.
    - XML: ExperimentStepSet

### Technique

Reference to Technique Definition used in this Experiment.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __uri*__
    - Type: string
    - Description: URI where Technique Definition file can be fetched.
    - XML: @uri
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __sha256__
    - Type: string
    - Description: SHA256 checksum of the referenced Technique Definition. Hex encoded, lower cased. Similar to the output of the sha256 unix command.
    - XML: @sha256
- __extension__
    - Type: [Extension](#Extension)
    - Multiple: True
    - Description: Reference to an Extension to amend the active Technique Definition.
    - XML: Extension

### TagSet

Set of Tag elements.

- __tag__
    - Type: [Tag](#Tag)
    - Multiple: True
    - Description: Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system.
    - XML: Tag

### Method

Describes how this Experiment was performed.

- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __name__
    - Type: string
    - Description: Optional method name, as defined in the instrument software.
    - XML: @name
- __author__
    - Type: [Author](#Author)
    - Description: Information about a person, a device or a piece of software authoring AnIML files.
    - XML: Author
- __device__
    - Type: [Device](#Device)
    - Description: Device used to perform experiment.
    - XML: Device
- __software__
    - Type: [Software](#Software)
    - Description: Software used to author this.
    - XML: Software
- __category__
    - Type: [Category](#Category)
    - Multiple: True
    - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
    - XML: Category

### Infrastructure

Contains references to the context of this Experiment.

- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __sample_reference_set__
    - Type: [SampleReferenceSet](#SampleReferenceSet)
    - Description: Set of Samples used in this Experiment.
    - XML: SampleReferenceSet
- __parent_data_point_reference_set__
    - Type: [ParentDataPointReferenceSet](#ParentDataPointReferenceSet)
    - Description: Contains references to the parent Result.
    - XML: ParentDataPointReferenceSet
- __experiment_data_reference_set__
    - Type: [ExperimentDataReferenceSet](#ExperimentDataReferenceSet)
    - Description: Set of Experiment Steps consumed by this Experiment Step.
    - XML: ExperimentDataReferenceSet
- __timestamp__
    - Type: datetime
    - Description: Date and time of modification.
    - XML: Timestamp

### Diff

Machine-readable description of changes made.

- __scope*__
    - Type: string
    - Description: Scope of diff. May be "element" or "attribute".
    - XML: @scope
- __changed_item*__
    - Type: string
    - Description: ID of the SignableItem that was changed
    - XML: @changedItem
- __old_value*__
    - Type: string
    - Description: 
    - XML: OldValue
- __new_value*__
    - Type: string
    - Description: 
    - XML: NewValue

### Author

Information about a person, a device or a piece of software authoring AnIML files.

- __user_type*__
    - Type: string
    - Description: Type of user (human, device, software)
    - XML: @userType
- __name*__
    - Type: string
    - Description: Common name.
    - XML: Name
- __affiliation__
    - Type: string
    - Description: Organization the Author is affiliated with.
    - XML: Affiliation
- __role__
    - Type: string
    - Description: Role the Author plays within the organization.
    - XML: Role
- __email__
    - Type: string
    - Description: RFC822-compliant email address.
    - XML: Email
- __phone__
    - Type: string
    - Description: Phone number.
    - XML: Phone
- __location__
    - Type: string
    - Description: Location or physical address.
    - XML: Location

### Software

Software used to author this.

- __name*__
    - Type: string
    - Description: Common name.
    - XML: Name
- __manufacturer__
    - Type: string
    - Description: Company name.
    - XML: Manufacturer
- __version__
    - Type: string
    - Description: Version identifier of software release.
    - XML: Version
- __operating_system__
    - Type: string
    - Description: Operating system the software was running on.
    - XML: OperatingSystem

### Category

Defines a category of Parameters and SeriesSets. Used to model hierarchies.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __parameter__
    - Type: [Parameter](#Parameter)
    - Multiple: True
    - Description: Name/Value Pair.
    - XML: Parameter
- __series_set__
    - Type: [SeriesSet](#SeriesSet)
    - Multiple: True
    - Description: Container for n-dimensional Data.
    - XML: SeriesSet
- __category__
    - Type: [Category](#Category)
    - Multiple: True
    - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
    - XML: Category

### Extension

Reference to an Extension to amend the active Technique Definition.

- __uri*__
    - Type: string
    - Description: URI where Extension file can be fetched.
    - XML: @uri
- __name*__
    - Type: string
    - Description: Name of Extension to be used. Must match Name given in Extension Definition file.
    - XML: @name
- __sha256__
    - Type: string
    - Description: SHA256 checksum of the referenced Extension. Hex encoded, lower cased. Similar to the output of the sha256 unix command.
    - XML: @sha256

### Tag

Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system.

- __name*__
    - Type: string
    - Description: None
    - XML: @name
- __value__
    - Type: string
    - Description: None
    - XML: @value

### Device

Device used to perform experiment.

- __name*__
    - Type: string
    - Description: Common name.
    - XML: Name
- __device_identifier__
    - Type: string
    - Description: Unique name or identifier of the device.
    - XML: DeviceIdentifier
- __manufacturer__
    - Type: string
    - Description: Company name.
    - XML: Manufacturer
- __firmware_version__
    - Type: string
    - Description: Version identifier of firmware release.
    - XML: FirmwareVersion
- __serial_number__
    - Type: string
    - Description: Unique serial number of device.
    - XML: SerialNumber

### SampleReferenceSet

Set of Samples used in this Experiment.

- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __sample_reference__
    - Type: [SampleReference](#SampleReference)
    - Multiple: True
    - Description: Reference to a Sample used in this Experiment.
    - XML: SampleReference
- __sample_inheritance__
    - Type: [SampleInheritance](#SampleInheritance)
    - Multiple: True
    - Description: Indicates that a Sample was inherited from the parent ExperimentStep.
    - XML: SampleInheritance

### ParentDataPointReferenceSet

Contains references to the parent Result.

- __parent_data_point_reference*__
    - Type: [ParentDataPointReference](#ParentDataPointReference)
    - Multiple: True
    - Description: Reference to a data point or value range in an independent Series in the parent Result.
    - XML: ParentDataPointReference

### ExperimentDataReferenceSet

Set of Experiment Steps consumed by this Experiment Step.

- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __experiment_data_reference__
    - Type: [ExperimentDataReference](#ExperimentDataReference)
    - Multiple: True
    - Description: Reference to an Experiment Step whose data is consumed.
    - XML: ExperimentDataReference
- __experiment_data_bulk_reference__
    - Type: [ExperimentDataBulkReference](#ExperimentDataBulkReference)
    - Multiple: True
    - Description: Prefix-based reference to a set of Experiment Steps whose data are consumed.
    - XML: ExperimentDataBulkReference

### Parameter

Name/Value Pair.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __parameter_type*__
    - Type: string
    - Description: Data type of this parameter
    - XML: @parameterType
- __value*__
    - Type: datetime, string, bytes, float, bool, int
    - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value. DateTime: Individual ISO date/time value. PNG: Base 64 encoded PNG image. EmbeddedXML: Value governed by a different XML Schema. SVG: Value governed by the SVG DTD. Used to represent vector graphic images.
    - XML: int: I, float: L, float: F, float: D, string: S, bool: Boolean, datetime: DateTime, bytes: PNG, string: EmbeddedXML, string: SVG
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __value__
    - Type: [SIUnit](#SIUnit)
    - Description: SIUnit: Combination of SI Units used to represent Scientific unit
    - XML: SIUnit: SIUnit

### SeriesSet

Container for n-dimensional Data.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __length*__
    - Type: string
    - Description: Number of data points each Series contains.
    - XML: @length
- __series*__
    - Type: [Series](#Series)
    - Multiple: True
    - Description: Container for multiple Values.
    - XML: Series
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id

### SampleReference

Reference to a Sample used in this Experiment.

- __sample_id*__
    - Type: string
    - Description: SampleID of the Sample used in the current ExperimentStep. Refers to the sampleID within the SampleSet section of the document.
    - XML: @sampleID
- __role*__
    - Type: string
    - Description: Role this sample plays within the current ExperimentStep.
    - XML: @role
- __sample_purpose*__
    - Type: string
    - Description: Specifies whether the referenced sample is produced or consumed by the current ExperimentStep.
    - XML: @samplePurpose
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id

### SampleInheritance

Indicates that a Sample was inherited from the parent ExperimentStep.

- __role*__
    - Type: string
    - Description: Role this sample plays within the current ExperimentStep.
    - XML: @role
- __sample_purpose*__
    - Type: string
    - Description: Specifies whether the referenced sample is produced or consumed by the current ExperimentStep.
    - XML: @samplePurpose
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id

### ParentDataPointReference

Reference to a data point or value range in an independent Series in the parent Result.

- __series_id*__
    - Type: string
    - Description: Contains the ID of the Series referenced.
    - XML: @seriesID
- __start_value*__
    - Type: [StartValue](#StartValue)
    - Description: Lower boundary of an interval or ValueSet.
    - XML: StartValue
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __end_value__
    - Type: [EndValue](#EndValue)
    - Description: Upper boundary of an interval.
    - XML: EndValue

### ExperimentDataReference

Reference to an Experiment Step whose data is consumed.

- __role*__
    - Type: string
    - Description: None
    - XML: @role
- __data_purpose*__
    - Type: string
    - Description: None
    - XML: @dataPurpose
- __experiment_step_id*__
    - Type: string
    - Description: None
    - XML: @experimentStepID
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id

### ExperimentDataBulkReference

Prefix-based reference to a set of Experiment Steps whose data are consumed.

- __role*__
    - Type: string
    - Description: None
    - XML: @role
- __data_purpose*__
    - Type: string
    - Description: None
    - XML: @dataPurpose
- __experiment_step_id_prefix*__
    - Type: string
    - Description: None
    - XML: @experimentStepIDPrefix
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id

### SIUnit

Combination of SI Units used to represent Scientific unit

- __factor__
    - Type: string
    - Description: None
    - XML: @factor
- __exponent__
    - Type: string
    - Description: None
    - XML: @exponent
- __offset__
    - Type: string
    - Description: None
    - XML: @offset

### Series

Container for multiple Values.

- __name*__
    - Type: string
    - Description: Plain-text name of this item.
    - XML: @name
- __dependency*__
    - Type: string
    - Description: Specified whether the Series is independent or dependent.
    - XML: @dependency
- __series_id*__
    - Type: string
    - Description: Identifies the Series. Used in References from subordinate ExperimentSteps. Unique per SeriesSet.
    - XML: @seriesID
- __series_type*__
    - Type: string
    - Description: Data type used by all values in this Series.
    - XML: @seriesType
- __id__
    - Type: string
    - Description: Anchor point for digital signature. This identifier is referred to from the "Reference" element in a Signature. Unique per document.
    - XML: @id
- __visible__
    - Type: string
    - Description: Specifies whether data in this Series is to be displayed to the user by default.
    - XML: @visible
- __plot_scale__
    - Type: string
    - Description: Specifies whether the data in this Series is typically plotted on a linear or logarithmic scale.
    - XML: @plotScale
- __value__
    - Type: [IndividualValueSet, EncodedValueSet, AutoIncrementedValueSet](#IndividualValueSet, EncodedValueSet, AutoIncrementedValueSet)
    - Description: IndividualValueSet: Multiple Values explicitly specified. EncodedValueSet: Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order. AutoIncrementedValueSet: Multiple values given in form of a start value and an increment.
    - XML: IndividualValueSet: IndividualValueSet, EncodedValueSet: EncodedValueSet, AutoIncrementedValueSet: AutoIncrementedValueSet
- __unit__
    - Type: [Unit](#Unit)
    - Description: Definition of a Scientific Unit.
    - XML: Unit

### EndValue

Upper boundary of an interval.

- __value*__
    - Type: float, int
    - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.
    - XML: int: I, float: L, float: F, float: D

### IndividualValueSet

Multiple Values explicitly specified.

- __values*__
    - Type: datetime, string, bytes, float, bool, int
    - Multiple: True
    - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value. DateTime: Individual ISO date/time value. PNG: Base 64 encoded PNG image. EmbeddedXML: Value governed by a different XML Schema. SVG: Value governed by the SVG DTD. Used to represent vector graphic images.
    - XML: int: I, float: L, float: F, float: D, string: S, bool: Boolean, datetime: DateTime, bytes: PNG, string: EmbeddedXML, string: SVG
- __start_index__
    - Type: string
    - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
    - XML: @startIndex
- __end_index__
    - Type: string
    - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
    - XML: @endIndex

### EncodedValueSet

Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order.

- __start_index__
    - Type: string
    - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
    - XML: @startIndex
- __end_index__
    - Type: string
    - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
    - XML: @endIndex

### Unit

Definition of a Scientific Unit.

- __label*__
    - Type: string
    - Description: Defines the visual representation of a particular Unit.
    - XML: @label
- __quantity__
    - Type: string
    - Description: Quantity the unit can be applied to
    - XML: @quantity
- __si_unit__
    - Type: [SIUnit](#SIUnit)
    - Multiple: True
    - Description: Combination of SI Units used to represent Scientific unit
    - XML: SIUnit

### AutoIncrementedValueSet

Multiple values given in form of a start value and an increment.

- __start_value*__
    - Type: [StartValue](#StartValue)
    - Description: Lower boundary of an interval or ValueSet.
    - XML: StartValue
- __increment*__
    - Type: [Increment](#Increment)
    - Description: Increment value
    - XML: Increment
- __start_index__
    - Type: string
    - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
    - XML: @startIndex
- __end_index__
    - Type: string
    - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
    - XML: @endIndex

### Increment

Increment value

- __value*__
    - Type: float, int
    - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.
    - XML: int: I, float: L, float: F, float: D

### StartValue

Lower boundary of an interval or ValueSet.

- __value*__
    - Type: float, int
    - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.
    - XML: int: I, float: L, float: F, float: D
