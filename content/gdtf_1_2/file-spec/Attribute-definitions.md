---
title: "Attribute definitions"
description: "This section defines the attribute definitions for the Fixture Type Attributes."
lead: "This section defines the attribute definitions for the Fixture Type Attributes."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 60
toc: true
---

## Attribute Definitions

### General

This section defines the attribute definitions for the Fixture Type
Attributes.

Note 1: More information on the definitions of attributes can be found in
[Annex A "Attribute Definitions"](/gdtf/annex/annex-a/). 

Note 2: All currently defined Fixture Type Attributes can be found in [Annex B
"Attribute Listing"](/gdtf/annex/annex-b/).

Note 3: All currently defined activation groups can be found in [Annex B
"Attribute Listing"](/gdtf/annex/annex-b/). 

Note 4: All currently defined feature groups can be found in [Annex B
"Attribute Listing"](/gdtf/annex/annex-b/). 

The current attribute definition node does not have any XML attributes
(XML node `<AttributeDefinitions>`). Children of the attribute definition
are specified in [table 5](#table-5 ).

<div id="table-5">

#### Table 5. *Attribute Definition Children*

| XML node     | Mandatory | Description     |
|----|----|----|
| [ActivationGroups](#activation-group) | No        | Defines which attributes are to be activated together. For example, Pan and Tilt are in the same activation group.                      |
| [FeatureGroups](#feature-group)       | Yes       | Describes the logical grouping of attributes. For example, Gobo 1 and Gobo 2 are grouped in the feature Gobo of the feature group Gobo. |
| [Attributes](#attribute)              | Yes       | List of Fixture Type Attributes that are used. Predefindes fixtury type attributes can be found in [Annex A](/gdtf/annex/annex-a/).                             |

</div>


### Activation Groups
  
#### General

This section defines groups of Fixture Type Attributes that are intended
to be used together.

Example: Usually Pan and Tilt are Fixture Type Attributes that shall be
activated together to be able to store and recreate any position.

The current activation groups node does not have any XML attributes (XML
node `<ActivationGroups>`). As children it can have a list of a
[activation group](#activation-group ).

#### Activation Group

This section defines the activation group Attributes (XML node
`<ActivationGroup`>). Currently defined XML attributes of the activation
group are specified in [table 6](#table-6 ).

<div id="table-6">

#### Table 6. *Activation Group Attributes*

| XML Attribute Name | Value Type                        | Description                              |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name ) | The unique name of the activation group. |


</div>

The activation group does not have any children.

### Feature Groups
  
#### General

This section defines the logical grouping of Fixture Type Attributes
(XML node `<FeatureGroups>`).

Note 1: A feature group can contain more than one logical control unit. A
feature group Position shall contain PanTilt and XYZ as separate Feature. 

Note 2: Usually Pan and Tilt create a logical unit to enable position control,
so they must be grouped in a Feature PanTilt.

As children the feature groups has a list of a [feature group](#feature-group ).

#### Feature Group
  
##### General

This section defines the feature group (XML node `<FeatureGroup>`). The
currently defined XML attributes of the feature group are specified in
[table 7](#table-7 ).

<div id="table-7">

#### Table 7. *Feature Group Attributes*

| XML Attribute Name | Value Type                            | Description                           |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the feature group. |
| Pretty             | [String](../file-format-definition#attrtype-string ) | The pretty name of the feature group. |


</div>

As children the feature group has a list of a
[feature](#feature ).

##### Feature

This section defines the feature (XML node `<Feature>`). The currently
defined XML attributes of the feature are specified in [table
8](#table-8 ).

<div id="table-8">

#### Table 8. *Feature Attributes*

| XML Attribute Name | Value Type                        | Description                     |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name ) | The unique name of the feature. |


</div>

The feature does not have any children.

### Attributes

#### General

This section defines the Fixture Type Attributes (XML node
`<Attributes>`). As children the attributes node has a list of a
[attributes](#attribute ).

#### Attribute

This section defines the Fixture Type Attribute (XML node `<Attribute>`).
The currently defined XML attributes of the attribute Node are specified
in [table 9](#table-9 ).

<div id="table-9">

#### Table 9. *XML Attributes of the Attribute*

| XML Attribute Name | Value Type | Description |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )         | The unique name of the attribute.                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pretty             | [String](../file-format-definition#attrtype-string )     | The pretty name of the attribute .                                                                                                                                                                                                                                                                                                                                                                                                   |
| ActivationGroup    | [Node](../file-format-definition#attrtype-node )         | Optional link to the activation group. The starting point is the [activation groups](#activation-groups ) node.                                                                                                                                                                                                                                                                                                            |
| Feature            | [Node](../file-format-definition#attrtype-node )         | Link to the corresponding feature. The starting point is the [feature groups](#feature-groups ) node.                                                                                                                                                                                                                                                                                                                      |
| MainAttribute      | [Node](../file-format-definition#attrtype-node )         | Optional link to the main attribute. The starting point is the [attribute](#attribute ) node.                                                                                                                                                                                                                                                                                                                              |
| PhysicalUnit       | [Enum](../file-format-definition#attrtype-enum )         | The currently defined unit values are: “None”, “Percent”, “Length” (m), “Mass” (kg), “Time” (s), “Temperature” (K), “LuminousIntensity”(cd), “Angle” (degree), “Force” (N), “Frequency” (Hz), “Current” (A), “Voltage” (V), “Power” (W), “Energy” (J), “Area” (m2), “Volume” (m3), “Speed” (m/s), “Acceleration” (m/s2), “AngularSpeed” (degree/s), “AngularAccc” (degree/s2), “WaveLength” (nm), “ColorComponent”. Default: “None”. |
| Color              | [ColorCIE](../file-format-definition#attrtype-colorcie ) | Optional. Defines the color for the attribute.                                                                                                                                                                                                                                                                                                                                                                                       |
|                    |                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                      |


</div>

As children the attribute node has a list of a [subphysical units](#subphysical-unit ).

##### Subphysical Unit

This section defines the Attribute Subphysical Unit (XML node `<SubPhysicalUnit>`).
The currently defined XML attributes of the subphysical unit are specified in [table 10](#table-10 ).

<div id="table-10">

#### Table 10. *XML Attributes of the Subphysical Unit*

| XML Attribute Name | Value Type                                | Description                                                                                             |
|----|----|----|
| Type               | [Enum](../file-format-definition#attrtype-enum )      | The currently defined values are: "PlacementOffset", "Amplitude", "AmplitudeMin", "AmplitudeMax", "Duration", "DutyCycle",  "TimeOffset", "MinimumOpening", "Value", "RatioHorizontal", "RatioVertical".  |
| PhysicalUnit       | [Enum](../file-format-definition#attrtype-enum )      | The currently defined unit values are: “None”, “Percent”, “Length” (m), “Mass” (kg), “Time” (s), “Temperature” (K), “LuminousIntensity”(cd), “Angle” (degree), “Force” (N), “Frequency” (Hz), “Current” (A), “Voltage” (V), “Power” (W), “Energy” (J), “Area” (m2), “Volume” (m3), “Speed” (m/s), “Acceleration” (m/s2), “AngularSpeed” (degree/s), “AngularAccc” (degree/s2), “WaveLength” (nm), “ColorComponent”. Default: “None”. |
| PhysicalFrom       | [Float](../file-format-definition#attrtype-float )    | The default physical from of the subphysical unit; Unit: as defined in PhysicalUnit; Default value: 0   |
| PhysicalTo         | [Float](../file-format-definition#attrtype-float )    | The default physical to of the subphysical unit; Unit: as defined in PhysicalUnit; Default value: 1     |


</div>

The subphysical unit does not have any children.

