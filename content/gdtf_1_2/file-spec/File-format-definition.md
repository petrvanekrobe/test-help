---
title: "File Format Definition"
description: "Describes the GDTF file format and the included files."
lead: "Describes the GDTF file format and the included files."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 40
toc: true
---

## File Format Definition

To describe the device type, a zip file with the extension
"*.gdtf" is used. The archive shall contain a description XML file and
resource files. Some of the resource files are located in a folder
structure. There are two folders defined: "./wheels" and "./models". The
folder "./models" has subfolders for a better structural overview:
- ./models/3ds
- ./models/gltf
- ./models/svg

The description.xml file
contains the description of the device type and all DMX modes as well as
all firmware revisions of the device.

```
./description.xml
./thumbnail.png
./thumbnail.svg
./wheels/gobo1.png
./wheels/gobo2.png
./models/3ds/base.3ds
./models/3ds/yoke.3ds
./models/gltf/base.glb
./models/gltf/yoke.glb
./models/3ds_low/base.3ds
./models/3ds_low/yoke.3ds
./models/gltf_low/base.glb
./models/gltf_low/yoke.glb
./models/gltf_high/base.glb
./models/gltf_high/yoke.glb
./models/3ds_high/base.3ds
./models/3ds_high/yoke.3ds
./models/svg/base.svg
./models/svg/yoke.svg
./models/svg_side/base.svg
./models/svg_side/yoke.svg
./models/svg_front/base.svg
./models/svg_front/yoke.svg

```

The ZIP archive name is specified as follows:
`<ManufacturerName>@<FixtureTypeName>@<OptionalComment>`

Example: `generic@led@comment`

UTF-8 has to be used to encode the XML file. Each XML file internally
consists of XML nodes. Each XML node could have XML attributes and XML
children. Each XML attribute has a value. If a XML attribute is not
specified, the default value of this XML attribute will be used. If the
XML attribute value is specified as a string, the format of the string
will depend on the XML attribute type. All XML attribute types are
specified in [Table 1](#table-1 ).


<div id="table-1">

##### Table 1 — *XML Attribute Value Types*

| Value Type                            | Format                | Description           |
|----|----|----|
|Uint<a id="attrtype-uint" />                       | Integer               | Unsigned integer|
|Int<a id="attrtype-int" />                         | Integer               | Signed integer|
|Hex<a id="attrtype-hex" />                         | Integer               | Number in hexadecimal  notation; Default value: 0|
|Float<a id="attrtype-float" />        | float                 | Floating point numeric; Separator: "."|
|String<a id="attrtype-string" />                   | Literal               | Text|
|Name<a id="attrtype-name" />                       | restricted Literal    | Unique object names; The allowed characters are listed in [Annex C](/gdtf/annex/annex-c/) Default value: object type with an index in parent.|
|Date<a id="attrtype-date" />                       | yyyy-mm-ddThh:mm:ss   |  Date and time corresponding to UTC +00:00 (Coordinated Universal Time): yyyy – year, mm – month, dd – day, hh – hours (24 format), mm – minutes, ss – seconds. Example: “2016-06-21T11:22:48” |
|Node<a id="attrtype-node" />                       | Name.Name.Name...     | Link to an element: “Name” is the value of the attribute “Name” of a defined XML node. The starting point defines each attribute separately. |
|ColorCIE<a id="attrtype-colorcie" />               | floatx, floaty,floatY       | CIE color representation xyY 1931|
|Vector3<a id="attrtype-vector3" />                 |  {float,float,float} | Vector with 3 float components|
|Matrix<a id="attrtype-matrix" />                   |  {float,float,float,float} <br/>{float,float,float,float} <br/>{float,float,float,float} <br/>{float,float,float,float} |  The transformation matrix consists 4 x 4 floats. Stored in a row-major order. For example, each row of the matrix is stored as a 4- component vector. The mathematical definition of the matrix is in a column-major order. For example, the matrix rotation is stored in the first three columns, and the translation is stored in the 4th column. The metric system consists of the Right- handed Cartesian Coordinates XYZ:<br/>X – from left (-X) to right (+X),<br/>Y – from the outside of the monitor (-Y) to the inside of the monitor (+Y),<br/>Z – from bottom (-Z) to top (+Z). 0,0,0 – center base. |
|Rotation<a id="attrtype-rotation"/>                | {float, float, float}<br/>{float, float, float} <br/>{float, float, float} | Rotation matrix, consist of 3\*3 floats. Stored as row-major matrix, i.e. each row of the matrix is stored as a 3-component vector. Mathematical definition of the matrix is column-major, i.e. the matrix rotation is stored in the three columns. Metric system, right-handed Cartesian coordinates XYZ:<br/>X – from left (-X) to right (+X),<br/>Y – from the outside of the monitor (-Y) to the inside of the monitor (+Y),<br/>Z – from the bottom (-Z) to the top (+Z). |
|Enum<a id="attrtype-enum"/>                        | Literal               | Possible values are predefined.|
|DMXAddress<a id="attrtype-dmxaddress"/>            |Int, Alternative format: Universe.Address | Absolute DMX address (size 4 bytes); Alternative format: Universe – integer universe number, starting with 1; Address: address within universe from 1 to 512. Format: integer |
|DMXValue<a id="attrtype-dmxvalue"/>                | Uint/n for ByteMirroring values <br/>Uint/ns for ByteShifting values |Special type to define DMX value where n is the byte count. The byte count can be individually specified without depending on the resolution of the DMX Channel.<br/> By default byte mirroring is used for the conversion. So 255/1 in a 16 bit channel will result in 65535.<br/>You can use the byte shifting operator to use byte shifting for the conversion. So 255/1s in a 16 bit channel will result in 65280. |
|GUID<a id="attrtype-guid"/>                        | XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX | Unique ID corresponding to RFC 4122: X–1 digit in hexadecimal notation. Example: “308EA87D-7164-42DE-8106-A6D273F57A51”. |
|Resource<a id="attrtype-resource"/>                | String|File name of the resource file without extension and without subfolder. |
|Pixel<a id="attrtype-pixel"/>                      | Pixel| 	Integer value representing one Pixel inside a MediaFile. Pixel count starts with zero in the top left corner.| 

The first XML node is always the XML description node: `<?xml version="1.0" encoding="UTF-8"?>`

The second XML node is the GDTF node. The attribute of this node is the
DataVersion: `<GDTF DataVersion="1.2">`

The example above shows the XML node for GDTF version 1.2.

<div id="table-2">

#### Table 2. *GDTF Node Attributes*

| XML Attribute Name | Value Type                             | Description                                                                                                                                                 |
|----|----|----|
| DataVersion        | [UInt.UInt](../file-format-definition#attrtype-uint )| The DataVersion attribute defines the minimal version of compatibility. The Version format is “Major.Minor”, where major and minor is Uint with size 1 byte. |


</div>

