---
title: "Fixture Type Node"
description: "Describes the starting point of the description of the fixture type."
lead: "Describes the starting point of the description of the fixture type."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 50
toc: true
---

## Fixture Type Node

The FixtureType node is the starting point of the description of the
fixture type within the XML file. The defined Fixture Type Node
attributes of the fixture type are specified in [table 3](#table-3 ).


<div id="table-3">

#### Table 3. *Fixture Type Node Attributes*

| XML Attribute Name | Value Type | Description  |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )         | Name of the fixture type. As it is based on Name, it is safe for parsing. |
| ShortName          | [String](../file-format-definition#attrtype-string )     | Shortened name of the fixture type. Non detailed version or an abbreviation. Can use any characters or symbols. |
| LongName           | [String](../file-format-definition#attrtype-string )     | Detailed, complete name of the fixture type, can include any characters or extra symbols. |
| Manufacturer       | [String](../file-format-definition#attrtype-string )     | Manufacturer of the fixture type.|
| Description        | [String](../file-format-definition#attrtype-string )     | Description of the fixture type. |
| FixtureTypeID      | [GUID](../file-format-definition#attrtype-guid )         | Unique number of the fixture type. |
| Thumbnail          | [Resource](../file-format-definition#attrtype-resource ) | Optional. File name without extension containing description of the thumbnail. Use the following as a resource file: <br />- png file to provide the rasterized picture. Maximum resolution of picture: 1024x1024 <br />- svg file to provide the vector graphic.  <br />- These resource files are located in the root directory of the zip file.  |
| ThumbnailOffsetX   | [Int](../file-format-definition#attrtype-int )           | Horizontal offset in pixels from the top left of the viewbox to the insertion point on a label. Default value: 0 |
| ThumbnailOffsetY   | [Int](../file-format-definition#attrtype-int )           | Vertical offset in pixels from the top left of the viewbox to the insertion point on a label. Default value: 0 |
| RefFT              | [GUID](../file-format-definition#attrtype-guid )         | Optional. GUID of the referenced fixture type. |
| CanHaveChildren    | [Enum](../file-format-definition#attrtype-enum )         | Describes if it is possible to mount other devices to this device. Value: “Yes”, “No”. Default value: “Yes” |

</div>


Fixture type node children are specified in [table 4](#table-4 ).

<div id="table-4">

#### Table 4. *Fixture Type Node Children*

| Child Node                                                | Mandatory | Description                                                                                 |
|----|----|----|
| [AttributeDefinitions](../attribute-definitions ) | Yes       | Defines all Fixture Type Attributes that are used in the fixture type.                      |
| [Wheels](../wheel-collect )                       | No        | Defines the physical or virtual color wheels, gobo wheels, media server content and others. |
| [PhysicalDescriptions](../physical-descriptions ) | No        | Contains additional physical descriptions.                                                  |
| [Models](../model-collect )                       | No        | Contains models of physically separated parts of the device.                                |
| [Geometries](../geometry-collect )                | Yes       | Describes physically separated parts of the device.                                         |
| [DMXModes](../dmx-mode-collect )                  | Yes       | Contains descriptions of the DMX modes.                                                     |
| [Revisions](../revision-collect )                 | No        | Describes the history of the fixture type.                                                  |
| [FTPresets](../fixture-type-preset-collect )              | No        | Is used to transfer user-defined and fixture type specific presets to other show files.     |
| [Protocols](../supported-protocol-collect)                        | No        | Is used to specify supported protocols.                                                     |


</div>

One or more sections could be empty or missing, but the order of
sections is mandatory as specified in [table 4](#table-4 ).

