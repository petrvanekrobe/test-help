---
title: "Geometry Collect"
description: "The physical description of the device parts is defined in the geometry collect."
lead: "The physical description of the device parts is defined in the geometry collect."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 100
toc: true
---
 
## Geometry Collect
  
### General

The physical description of the device parts is defined in the geometry
collect. Geometry collect can contain a separate geometry or a tree of
geometries. The geometry collect currently does not have any XML
attributes (XML node `<Geometries>`). The currently defined children nodes
of geometry collect are specified in [table 34](#table-34 ).

<div id="table-34">

#### Table 34. *Geometry Children Types*

| XML node                                                              | Amount | Description                                                                                    |
|----|----|----|
| [Geometry](#general-geometry )                           | Any    | General Geometry.                                                                              |
| [Axis](#geometry-type-axis )                             | Any    | Geometry with axis.                                                                            |
| [FilterBeam](#geometry-type-beam-filter )                | Any    | Geometry with a beam filter.                                                                   |
| [FilterColor](#geometry-type-color-filter )              | Any    | Geometry with color filter.                                                                    |
| [FilterGobo](#geometry-type-gobo-filter )                | Any    | Geometry with gobo.                                                                            |
| [FilterShaper](#geometry-type-shaper-filter )            | Any    | Geometry with shaper.                                                                          |
| [Beam](#geometry-type-beam )                             | Any    | Geometry that describes a light output to project.                                             |
| [MediaServerLayer](#geometry-type-media-server-layer )   | Any    | Geometry that describes a media representation layer of a media device.                        |
| [MediaServerCamera](#geometry-type-media-server-camera ) | Any    | Geometry that describes a camera or output layer of a media device.                            |
| [MediaServerMaster](#geometry-type-media-server-master ) | Any    | Geometry that describes a master control layer of a media device.                              |
| [Display](#geometry-type-display )                       | Any    | Geometry that describes a surface to display visual media.                                     |
| [GeometryReference](#geometry-type-reference )           | Any    | Reference to already described geometries.                                                     |
| [Laser](#geometry-type-laser )                           | Any    | Geometry with a laser light output.                                                            |
| [WiringObject](#geometry-type-wiring-object )            | Any    | Geometry that describes an internal wiring for power or data.                                  |
| [Inventory](#geometry-type-inventory )                   | Any    | Geometry that describes an additional item that can be used for a fixture (like a rain cover). |
| [Structure](#geometry-type-structure )                   | Any    | Geometry that describes the internal framing of an object (like members).                      |
| [Support](#geometry-type-support )                       | Any    | Geometry that describes a support like a base plate or a hoist.                                |
| [Magnet](#geometry-type-magnet )                         | Any    | Geometry that describes a point where other geometries should be attached.                     |


</div>

Note 1: Position the geometry in it's "Default" position. This is defined by
the Default Value from the DMX Channel that controls the position of that
geometry.

### General Geometry

It is a basic geometry type without specification (XML node `<Geometry>`).
The currently defined XML attributes of the geometry are specified in
[table 35](#table-35 ).

<div id="table-35">

#### Table 35. *Geometry Attributes*

| XML Attribute Name | Value Type                            | Description                                                                                                                                                             |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of geometry. Recommendation for conventional is “Body”. Recommendation for a geometry that is representing the base housing of a moving head is “Base”. |
| Model              | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model.                                                                                                                                        |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                                                                                           |


</div>

The geometry has the same children types as the geometry collect (see
[table 34](#table-34 )).


### Geometry Type Axis

This type of geometry defines device parts with a rotation axis (XML
node `<Axis>`). The currently defined XML attributes of the axis are
specified in [table 36](#table-36 ).

<div id="table-36">

#### Table 36. *Axis Attributes*

| XML Attribute Name | Value Type                            | Description                                                                                                                                                                                                                                   |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry. Recommendation for an axis-geometry is “Yoke”. Recommendation for an axis-geometry representing the lamp housing of a moving head is “Head”. Note: The Head of a moving head is usually mounted to the Yoke. |
| Model           | [Name](../file-format-definition#attrtype-name ) | Link to the corresponding model. Matrix                                                                                                                                                                                 |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                                                                                                                                                                 |


</div>

The axis has the same children types as the geometry collect (see
[table 34](#table-34 )).


### Geometry Type Beam Filter

This type of geometry defines device parts with a beam filter (XML node
`<FilterBeam>`). The currently defined XML attributes of the beam filter
are specified in [table 37](#table-37 ).

<div id="table-37">

#### Table 37. *Beam Filter Attributes*

| XML Attribute Name | Value Type                            | Description                                                                                                                                                                                                                                              |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry. Recommendation for beam filter limiting the diffusion of light is “BarnDoor”. Recommendation for beam filter adjusting the diameter of the beam is “Iris”. Note: BarnDoor and Iris are usually mounted to conventional. |
| Model              | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model.                                                                                                                                                                                                                         |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                                                                                                                                                                            |


</div>

The beam filter has the same children types as the geometry collect (see
[table 34](#table-34 )).

### Geometry Type Color Filter

This type of geometry is used to describe device parts which have a
color filter (XML node `<FilterColor>`). The currently defined XML
attributes of the color filter are specified in [table 38](#table-38 ).

<div id="table-38">

#### Table 38. *Color Filter Attributes*

| XML Attribute Name | Value Type                            | Description                                                                                                                                                           |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of geometry. Recommendation for filter of a color or mechanical color changer is “FilterColor”. Note: FilterColor is usually mounted to conventional. |
| Model              | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model.                                                                                                                                      |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                                                                                         |


</div>

The color filter has the same children types as the geometry collect (see
[table 34](#table-34 )).


### Geometry Type Gobo Filter

This type of geometry is used to describe device parts which have gobo
wheels (XML node `<FilterGobo>`). The currently defined XML attributes of
the gobo filter are specified in [table 39](#table-39 ).

<div id="table-39">

#### Table 39. *Gobo Filter Attributes*

| XML Attribute Name | Value Type                            | Description                                                                                                                                                           |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry. Recommendation for filter of a gobo or mechanical gobo changer is “FilterGobo”. Note: FilterGobo is usually mounted to conventional. |
| Model              | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model.                                                                                                                                      |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                                                                                         |


</div>

The gobo filter has the same children types as the geometry collect (see
[table 34](#table-34 )).


### Geometry Type Shaper Filter

This type of geometry is used to describe device parts which have a
shaper (XML node `<FilterShaper>`). The currently defined XML attributes
of the shaper filter are specified in [table 40](#table-40 ).

<div id="table-40">

#### Table 40. *Shaper Filter Attributes*

| XML Attribute Name | Value Type                            | Description                                                                                                                                                                                 |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry; Recommendation for filter used to form the beam to a framed, triangular, or trapezoid shape, is “Shaper”. Note: Shaper is usually mounted to conventional. |
| Model              | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model.                                                                                                                                                            |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                                                                                                               |


</div>

The shaper filter has the same children types as the geometry collect (see
[table 34](#table-34 )).


### Geometry Type Beam

This type of geometry is used to describe device parts which have a
light source (XML node `<Beam>`). The currently defined XML attributes of
the Beam are specified in [table 41](#table-41 ).

<div id="table-41">

#### Table 41. *Beam Attributes*

| XML Attribute Name  | Value Type                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----|----|----|
| Name                | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry. Recommendation for a light source of a conventional or moving head or a projector is “Beam”. Note 1: Beam is usually mounted to Head or Body. Recommendation for a self-emitting single light source is “Pixel”. Note 2: Pixel is usually mounted to Head or Body. Recommendation for a number of Pixel that are controlled at the same time is “Array”. Note 3: Array is usually mounted to Head or Body. Recommendation for a light source of a moving mirror is “Mirror”. Note 4: Mirror is usually mounted to Yoke. |
| Model               | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Position            | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| LampType            | [Enum](../file-format-definition#attrtype-enum )     | Defines type of the light source; The currently defined types are: Discharge, Tungsten, Halogen, LED; Default value “Discharge”                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PowerConsumption    | [Float](../file-format-definition#attrtype-float )   | Power consumption; Default value: 1000; Unit: Watt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| LuminousFlux        | [Float](../file-format-definition#attrtype-float )   | Intensity of all the represented light emitters; Default value: 10000; Unit: lumen                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ColorTemperature    | [Float](../file-format-definition#attrtype-float )   | Color temperature; Default value: 6000; Unit: kelvin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| BeamAngle           | [Float](../file-format-definition#attrtype-float )   | Beam angle; Default value: 25.0; Unit: degree                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| FieldAngle          | [Float](../file-format-definition#attrtype-float )   | Field angle; Default value: 25.0; Unit: degree                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ThrowRatio          | [Float](../file-format-definition#attrtype-float )   | Throw Ratio of the lens for BeamType Rectangle; Default value: 1; Unit: None                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| RectangleRatio      | [Float](../file-format-definition#attrtype-float )   | Ratio from Width to Height of the Rectangle Type Beam; Default value: 1.7777; Unit: None                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| BeamRadius          | [Float](../file-format-definition#attrtype-float )   | Beam radius on starting point. Default value: 0.05; Unit: meter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| BeamType            | [Enum](../file-format-definition#attrtype-enum )     | Beam Type; Specified values: "Wash", "Spot", "None", "Rectangle", "PC", "Fresnel", "Glow". Default value "Wash"
| ColorRenderingIndex | [Uint](../file-format-definition#attrtype-uint )     | The CRI according to TM-30 is a quantitative measure of the ability of the light source showing the object color naturally as it does as daylight reference. Size 1 byte. Default value 100.                                                                                                                                                                                                                                                                                                                                                             |
| EmitterSpectrum     | [Node](../file-format-definition#attrtype-node )     | Optional link to emitter in the physical description; use this to define the white light source of a subtractive color mixing system. Starting point: Emitter Collect; Default spectrum is a Black-Body with the defined ColorTemperature.                                                                                                                                                                                                                                                                                                                                                                   |

</div>

The beam has the same children types as the geometry collect (see
[table 34](#table-34 )).


Use the Geometry Type "Beam" to describe the position of the fixture's
light output (usually the position of the lens) and not the position of
the light source inside the device. The origin of the Geometry Type
"Beam" is the origin of the rendered beam. The origin of the Geometry
Type "Beam" should not be covered by any faces of other geometries in
order to not block the rendered beam.

The `<BeamType>` describes how the Beam will be rendered.

"Wash", "Fresnel", "PC"- A conical beam with soft edges and softened field projection.

"Spot" - A conical beam with hard edges.

"Rectangle" - A pyramid-shaped beam with hard edges.

"None", "Glow" - No beam will be drawn, only the geometry will emit light
itself.

The beam geometry emits its light into negative Z direction (and Y-up).

### Geometry Type Media Server Layer

This type of geometry is used to describe the layer of a media device
that is used for representation of media files (XML node
`<MediaServerLayer>`). The currently defined XML attributes of the media
server layer are specified in [table 42](#table-42 ).

<div id="table-42">

#### Table 42. *Media Server Layer Attributes*

| XML Attribute Name | Value Type                            | Description                                                                                       |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry.                                                                  |
| Model              | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model that will be used to display the alignment in media server space. |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                     |


</div>

The media server layer has the same children types as the geometry
collect (see [table 34](#table-34 )).

### Geometry Type Media Server Camera

This type of geometry is used to describe the camera or output of a
media device (XML node `<MediaServerCamera>`). The currently defined XML
attributes of the media server camera are specified in [table
43](#table-43 ).

<div id="table-43">

#### Table 43. *Media Server Camera Attributes*

| XML Attribute Name | Value Type                            | Description                                                                                       |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry.                                                                  |
| Model              | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model that will be used to display the alignment in media server space. |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                     |


</div>

The media server camera has the same children types as the geometry
collect (see [table 34](#table-34 )).

The media server camera-view points into the positive Y-direction (and
Z-up).

### Geometry Type Media Server Master

This type of geometry is used to describe the master control of one or
several media devices (XML node `<MediaServerMaster>`). The currently
defined XML attributes of the media server master are specified in
[table 44](#table-44 ).

<div id="table-44">

#### Table 44. *Media Server Master Attributes*

| XML Attribute Name | Value Type                            | Description                                                   |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry.                              |
| Model              | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model.                              |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix |


</div>

The media server master has the same children types as the geometry
collect (see [table 34](#table-34 )).

### Geometry Type Display

This type of geometry is used to describe a self-emitting surface which
is used to display visual media (XML node `<Display>`). The currently
defined XML attributes of the display are specified in [table 45](#table-45 ).

<div id="table-45">

#### Table 45. *Display Attributes*

| XML Attribute Name | Value Type                                | Description                                                                               |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )         | The unique name of the geometry.                                                          |
| Model              | [Name](../file-format-definition#attrtype-name )         | Link to the corresponding model.                                                          |
| Position           | [Matrix](../file-format-definition#attrtype-matrix )     | Relative position of geometry; Default value: Identity Matrix                             |
| Texture            | [Resource](../file-format-definition#attrtype-resource ) | Name of the mapped texture in Model file that will be swapped out for the media resource. |


</div>

The display has the same children types as the geometry collect (see
[table 34](#table-34 )).


### Geometry Type Laser
  
#### General

This type of geometry is used to describe the position of a laser's 
light output (XML node `<Laser>`). The currently
defined XML attributes of the laser are specified in [table 46](#table-46 ).

<div id="table-46">

#### Table 46. *Laser Attributes*

| XML Attribute Name | Value Type     |                    |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )      | The unique name of the geometry.                                                                               |
| Model              | [Name](../file-format-definition#attrtype-name )      | Link to the corresponding model.                                                                               |
| Position           | [Matrix](../file-format-definition#attrtype-matrix )  | Relative position of geometry; Default value: Identity Matrix                                                  |
| ColorType <a id="attrtype-colortype" />         | [Enum](../file-format-definition#attrtype-enum )      | The currently defined unit values are: “RGB”, “SingleWaveLength”,  Default: RGB.                               |
| Color              | [Float](../file-format-definition#attrtype-float)     | Required if [ColorType](#attrtype-colortype) is "SingleWaveLength"; Unit:nm (nanometers)                                            |
| OutputStrength     | [Float](../file-format-definition#attrtype-float)     | Output Strength of the Laser; Unit: Watt                                                              |
| Emitter            | [Node](../file-format-definition#attrtype-node )      | Optional link to the emitter group. The starting point is the [Emitter Collect](../physical-descriptions/#emitter-collect). |
| BeamDiameter       | [Float](../file-format-definition#attrtype-float)     | Beam diameter where it leaves the projector; Unit: meter                                            |
| BeamDivergenceMin  | [Float](../file-format-definition#attrtype-float)     | Minimum beam divergence; Unit: mrad  (milliradian)                                                             |
| BeamDivergenceMax  | [Float](../file-format-definition#attrtype-float)     | Maximum beam divergence; Unit: mrad  (milliradian)                                                             |
| ScanAnglePan       | [Float](../file-format-definition#attrtype-float)     | Possible Total Scan Angle Pan of the beam. Assumes symmetrical output; Unit: Degree                            |
| ScanAngleTilt      | [Float](../file-format-definition#attrtype-float)     | Possible Total Scan Angle Tilt of the beam. Assumes symmetrical output; Unit: Degree                           |
| ScanSpeed          | [Float](../file-format-definition#attrtype-float)     | Speed of the beam; Unit: kilo point per second                                                                 |


</div>

The laser has the same children types as the geometry collect (see
[table 34](#table-34 )).

In addition, it also has a list of supported protocols (XML node `<Protocol>`) as children.

#### Protocol

This XML node specifies the protocol for a Laser (XML node `<Protocol>`). The currently defined XML
attributes of the protocol are specified in [table 47](#table-47 ).

<div id="table-47">

#### Table 47 *Protocol attributes*

| XML Attribute Name | Value Type                                    | Description                                                                                              |
|----|----|----|
| Name          | [String](../file-format-definition#attrtype-string ) | Name of the protocol                      |

The protocol doesn't have any children.

### Geometry Type Reference
  
#### General

The Geometry Type Reference is used to describe multiple instances of
the same geometry. Example: LED panel with multiple pixels. (XML node ).
The currently defined XML attributes of reference are specified in
[table 48](#table-48). 

Note 1: Geometry Reference also allows easier definition of the DMX Channels
for these geometries.

<div id="table-48">

#### Table 48. *Geometry Reference Attributes*

| XML Attribute Name | Value Type                            | Description    |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of geometry.                                                                                                                                                                                                                                                                               |
| Position           | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix                                                                                                                                                                                                                                              |
| Geometry           | [Name](../file-format-definition#attrtype-name )     | Name of the referenced geometry. Only top level geometries are allowed to be referenced.                                                                                                                                                                                                                   |
| Model              | [Name](../file-format-definition#attrtype-name )     | Optional. Link to the corresponding model. The model only replaces the model of the parent of the referenced geometry. The models of the children of the referenced geometry are not affected. The starting point is Models Collect. If model is not set, the model is taken from the referenced geometry. |


</div>

As children, the Geometry Type Reference has a list of breaks. The
count of the children depends on the number of different breaks in the
DMX channels of the referenced geometry. If the referenced geometry, for
example, has DMX channels with DMX break 2 and 4, the geometry reference
has to have 2 children. The first child with DMX offset for DMX break 2
and the second child for DMX break 4. If one or more of the DMX channels
of the referenced geometry have the special value “Overwrite” as a DMX
break, the DMX break for those channels and the DMX offsets need to be
defined.

#### Break

This XML node specifies the DMX offset for the DMX channel of the
referenced geometry (XML node `<Break>`). The currently defined XML
attributes of the break are specified in [table 49](#table-49 ).

<div id="table-49">

#### Table 49. *Break Attributes*

| XML Attribute Name | Value Type                                    | Description                                                                                              |
|----|----|----|
| DMXOffset          | [DMXAddress](../file-format-definition#attrtype-dmxaddress ) | DMX offset; Default value:1 (Means no offset for the corresponding DMX Channel)                          |
| DMXBreak           | [Uint](../file-format-definition#attrtype-uint )             | Defines the unique number of the DMX Break for which the Offset is given. Size: 1 byte; Default value 1. |


</div>


### Geometry Type Wiring Object
  
#### General

This type of geometry is used to describe an electrical device that can be wired (XML node `<WiringObject>`). The currently
defined XML attributes of a wiring object geometry are specified in [table 50](#table-50 ).

<div id="table-50">

#### Table 50. *Wiring Object Attributes*

| XML Attribute Name  | Value Type                                | Description                                                                                       |
|----|----|----|
| Name                | [Name](../file-format-definition#attrtype-name )      | The unique name of the geometry. The name is also the name of the interface to the outside        |
| Model               | [Name](../file-format-definition#attrtype-name )      | Link to the corresponding model.                                                                  |
| ConnectorType   <a id="attrtype-connectortype" />    | [Name](../file-format-definition#attrtype-name )      | The type of the connector. Find a list of predefined types in [Annex D](/gdtf/annex/annex-d/). This is not applicable for Component Types Fuses. Custom type of connector can also be defined, for example "Loose End".|
| Position            | [Matrix](../file-format-definition#attrtype-matrix )  | Relative position of geometry; Default value: Identity Matrix                                     |
| ComponentType       | [Enum](../file-format-definition#attrtype-enum )      | The type of the electrical component used. Defined values are "Input", "Output", "PowerSource", "Consumer", "Fuse", "NetworkProvider", "NetworkInput", "NetworkOutput", "NetworkInOut". |
| SignalType          | [String](../file-format-definition#attrtype-string )  | The type of the signal used. Predefinded values are "Power", "DMX512", "Protocol", "AES", "AnalogVideo", "AnalogAudio". When you have a custom protocol, you can add it here.        |
| PinCount            | [Int](../file-format-definition#attrtype-int )        | The number of available pins of the connector type to connect internal wiring to it.              |
| ElectricalPayLoad   | [Float](../file-format-definition#attrtype-float )    | The electrical consumption in Watts. Only for [Consumers](#attrtype-connectortype). Unit: Watt.                                         |
| VoltageRangeMax     | [Float](../file-format-definition#attrtype-float )    | The voltage range's maximum value. Only for [Consumers](#attrtype-connectortype). Unit:volt.                                           |
| VoltageRangeMin     | [Float](../file-format-definition#attrtype-float )    | The voltage range's minimum value. Only for [Consumers](#attrtype-connectortype). Unit: volt.                                            |
| FrequencyRangeMax     | [Float](../file-format-definition#attrtype-float )    | The Frequency range's maximum value. Only for [Consumers](#attrtype-connectortype). Unit: hertz.                                           |
| FrequencyRangeMin     | [Float](../file-format-definition#attrtype-float )    | The Frequency range's minimum value. Only for [Consumers](#attrtype-connectortype). Unit: hertz.                                            |
| MaxPayLoad          | [Float](../file-format-definition#attrtype-float )    | The maximum electrical payload that this power source can handle. Only for [Power Sources](#attrtype-connectortype). Unit: voltampere.        |
| Voltage             | [Float](../file-format-definition#attrtype-float )    | The voltage output that this power source can handle. Only for [Power Sources](#attrtype-connectortype). Unit: volt.                     |
| SignalLayer         | [Integer](../file-format-definition#attrtype-int )  | The layer of the Signal Type. In one device, all wiring geometry that use the same Signal Layers are connected. Special value 0: Connected to all geometries. |
| CosPhi              | [Float](../file-format-definition#attrtype-float )    | The Power Factor of the device. Only for consumers.                                               |
| FuseCurrent         | [Float](../file-format-definition#attrtype-float )    | The fuse value. Only for fuses. Unit: ampere.                                                                   |
| FuseRating          | [Enum](../file-format-definition#attrtype-enum )      | Fuse Rating. Defined values are "B", "C", "D", "K", "Z".                                          |
| Orientation         | [Enum](../file-format-definition#attrtype-enum )      | Where the pins are placed on the object. Defined values are "Left", "Right", "Top", "Bottom".     |
| WireGroup           | [String](../file-format-definition#attrtype-string )  | Name of the group to which this wiring object belong.                                             |


</div>

The wiring object has the same children types as the geometry
collect (see [table 34](#table-34 )).
In addition, it also has pin patch (XML node `<PinPatch>`) children.

#### Pin Patch

This XML node (XML node `<PinPatch>`) specifies how the different sockets of its parent
wiring object are connected to the pins of other wiring objects. The currently
defined XML attributes of a pin patch are specified in [table 51](#table-51 ).

<div id="table-51">

#### Table 51. *Pin Patch Attributes*

| XML Attribute Name  | Value Type                               | Description                                                                                            |
|----|----|----|
| ToWiringObject      | [Node](../file-format-definition#attrtype-node )     | Link to the wiring object connected through this pin patch.                                         |
| FromPin          | [Int](../file-format-definition#attrtype-int )       | The pin number used by the parent wiring object to connect to the targeted wiring object "ToWiringObject". |
| ToPin            | [Int](../file-format-definition#attrtype-int )       | The pin number used by the targeted wiring object "ToWiringObject" to connect to the parent wiring object. |


</div>

The pin patch doesn't have any children.

### Geometry Type Inventory

This type of geometry is used to describe a geometry used for the inventory (XML node `<Inventory>`). The currently
defined XML attributes of an inventory geometry are specified in
[table 52](#table-52 ).

<div id="table-52">

#### Table 52. *Inventory Attributes*

| XML Attribute Name  | Value Type                               | Description                                                    |
|----|----|----|
| Name                | [Name](../file-format-definition#attrtype-name )     | The unique name of the geometry.                               |
| Model               | [Name](../file-format-definition#attrtype-name )     | Link to the corresponding model.                               |
| Position            | [Matrix](../file-format-definition#attrtype-matrix ) | Relative position of geometry; Default value: Identity Matrix  |
| Count               | [Int](../file-format-definition#attrtype-int )       | The default count for new objects.                             |


</div>

The inventory geometry has the same children types as the geometry
collect (see [table 34](#table-34 )).

### Geometry Type Structure

This type of geometry is used to describe a structure (XML node `<Structure>`). The currently
defined XML attributes of a structure geometry are specified in
[table 53](#table-53 ).

<div id="table-53">

#### Table 53. *Structure Attributes*

| XML Attribute Name        | Value Type                                | Description                                                             |
|----|----|----|
| Name                      | [Name](../file-format-definition#attrtype-name )      | The unique name of the geometry.                                        |
| Model                     | [Name](../file-format-definition#attrtype-name )      | Link to the corresponding model.                                        |
| Position                  | [Matrix](../file-format-definition#attrtype-matrix )  | Relative position of geometry; Default value: Identity Matrix           |
| LinkedGeometry            | [Name](../file-format-definition#attrtype-name )      | The linked geometry.                                                    |
| StructureType             | [Enum](../file-format-definition#attrtype-enum )      | The type of structure. Defined values are "CenterLineBased", "Detail".  |
| CrossSectionType  <a id="attrtype-crosssectiontype" />        | [Enum](../file-format-definition#attrtype-enum )      | The type of cross section. Defined values are "TrussFramework", "Tube".       |
| CrossSectionHeight        | [Float](../file-format-definition#attrtype-float )    | The height of the cross section. Only for [Tubes](#attrtype-crosssectiontype). Unit: meter.                        |
| CrossSectionWallThickness | [Float](../file-format-definition#attrtype-float )    | The thickness of the wall of the cross section.Only for [Tubes](#attrtype-crosssectiontype). Unit: meter.          |
| TrussCrossSection         | [String](../file-format-definition#attrtype-string )  | The name of the truss cross section. Only for [Trusses](#attrtype-crosssectiontype).                  |




</div>

The structure geometry has the same children types as the geometry
collect (see [table 34](#table-34)).

### Geometry Type Support

This type of geometry is used to describe a support (XML node `<Support>`). The currently
defined XML attributes of a support geometry are specified in
[table 54](#table-54 ).

<div id="table-54">

#### Table 54. *Support Attributes*

| XML Attribute Name        | Value Type                                | Description                                                                                                                            |
|----|----|----|
| Name                      | [Name](../file-format-definition#attrtype-name )      | The unique name of the geometry.                                                                                                       |
| Model                     | [Name](../file-format-definition#attrtype-name )      | Link to the corresponding model.                                                                                                       |
| Position                  | [Matrix](../file-format-definition#attrtype-matrix )  | Relative position of geometry; Default value: Identity Matrix                                                                          |
| SupportType    <a id="attrtype-supporttype" />           | [Enum](../file-format-definition#attrtype-enum )      | The type of support. Defined values are "Rope", "GroundSupport".                                        |
| RopeCrossSection          | [String](../file-format-definition#attrtype-string )  | The name of the rope cross section. Only for [Ropes](#attrtype-supporttype).                                             |
| RopeOffset                | [Vector3](../file-format-definition#attrtype-vector3 )| The Offset of the rope from bottom to top. Only for [Ropes](#attrtype-supporttype). Unit: meter.                                     |
| CapacityX                 | [Float](../file-format-definition#attrtype-float )    | The allowable force on the X-Axis applied to the object according to the Eurocode. Unit: N.                                            |
| CapacityY                 | [Float](../file-format-definition#attrtype-float )    | The allowable force on the Y-Axis applied to the object according to the Eurocode. Unit: N.                                            |
| CapacityZ                 | [Float](../file-format-definition#attrtype-float )    | The allowable force on the Z-Axis applied to the object according to the Eurocode. Unit: N.                                            |
| CapacityXX                | [Float](../file-format-definition#attrtype-float )    | The allowable moment around the X-Axis applied to the object according to the Eurocode. Unit: N/m.                                     |
| CapacityYY                | [Float](../file-format-definition#attrtype-float )    | The allowable moment around the Y-Axis applied to the object according to the Eurocode. Unit: N/m.                                     |
| CapacityZZ                | [Float](../file-format-definition#attrtype-float )    | The allowable moment around the Z-Axis applied to the object according to the Eurocode.  Unit: N/m.                                    |
| ResistanceX               | [Float](../file-format-definition#attrtype-float )    | The compression ratio for this support along the X-Axis. Unit N/m. Only for [Ground Supports](#attrtype-supporttype).   |
| ResistanceY               | [Float](../file-format-definition#attrtype-float )    | The compression ratio for this support along the Y-Axis. Unit N/m. Only for [Ground Supports](#attrtype-supporttype).   |
| ResistanceZ               | [Float](../file-format-definition#attrtype-float )    | The compression ratio for this support along the Z-Axis. Unit N/m. Only for [Ground Supports](#attrtype-supporttype).   |
| ResistanceXX              | [Float](../file-format-definition#attrtype-float )    | The compression ratio for this support around the X-Axis. Unit N/m. Only for [Ground Supports](#attrtype-supporttype).  |
| ResistanceYY              | [Float](../file-format-definition#attrtype-float )    | The compression ratio for this support around the Y-Axis. Unit N/m. Only for [Ground Supports](#attrtype-supporttype).  |
| ResistanceZZ              | [Float](../file-format-definition#attrtype-float )    | The compression ratio for this support around the Z-Axis. Unit N/m. Only for [Ground Supports](#attrtype-supporttype).  |


</div>

The support geometry has the same children types as the geometry
collect (see [table 34](#table-34 )).

### Geometry Type Magnet

This type of geometry is used to describe a magnet, a point where other geometries should be attached (XML node `<Magnet>`). The currently
defined XML attributes of a magnet geometry are specified in
[table 55](#table-55 ).

<div id="table-55">

#### Table 55. *Magnet Attributes*

| XML Attribute Name        | Value Type                                | Description                                                                                     |
|----|----|----|
| Name                      | [Name](../file-format-definition#attrtype-name )      | The unique name of the geometry.                                                                |
| Model                     | [Name](../file-format-definition#attrtype-name )      | Link to the corresponding model.                                                                |
| Position                  | [Matrix](../file-format-definition#attrtype-matrix )  | Relative position of geometry; Default value: Identity Matrix                                   |


</div>

The magnet geometry has the same children types as the geometry
collect (see [table 34](#table-34 )).

## DMX Mode Collect
  
### General

This section is describes all DMX modes of the device. If firmware
revisions change a DMX footprint, then such revisions should be
specified as new DMX mode. The DMX mode collect currently does not have
any attributes (XML node `<DMXModes>`). As a child the fixture type DMX
mode collect has DMX modes.

### DMX Mode

Each DMX mode describes logical control part of the device in a specific
mode (XML node `<DMXMode>`). The currently defined XML attributes of the
DMX mode are specified in [table 56](#table-56 ).

<div id="table-56">

#### Table 56. *DMX Mode Attributes*

| XML Attribute Name | Value Type                        | Description                                                                                   |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name ) | The unique name of the DMX mode                                                               |
| Description        | [String](../file-format-definition#attrtype-string ) | Description of the DMX mode                                                               |
| Geometry           | [Name](../file-format-definition#attrtype-name ) | Name of the first geometry in the device; Only top level geometries are allowed to be linked. |


</div>

DMX mode children are specified in [table 57](#table-57 ).

<div id="table-57">

#### Table 57. *DMX Mode Children*

| XML node                                       | Mandatory | Description                                      |
|----|----|----|
| [DMXChannels](#dmx-channel-collect ) | Yes       | Description of all DMX channels used in the mode |
| [Relations](#relation-collect )      | No        | Description of relations between channels        |
| [FTMacros](#macro-collect )      | No        | Is used to describe macros of the manufacturer.  |


</div>

#### DMX Channel Collect
  
##### General

This section defines the DMX footprint of the device. The DMX channel
collect currently does not have any attributes (XML node `<DMXChannels>`).
As children the DMX channel collect has a list of a [DMX
channels](#dmx-channel ).

##### DMX Channel
  
###### General

This section defines the DMX channel (XML node `<DMXChannel>`). The name
of a DMX channel cannot be user-defined and must consist of a geometry
name and the attribute name of the first logical channel with separator
"\_". In one DMX Mode, this combination needs to be unique. Currently
defined XML attributes of the DMX channel are specified in [table
58](#table-58).

<div id="table-58">

#### Table 58. *DMX Channel Attributes*

| XML Attribute Name | Value Type                                | Description                                                                                                                                                                                                    |
|----|----|----|
| DMXBreak           | [Int](../file-format-definition#attrtype-int )           | Number of the DMXBreak; Default value: 1; Special value: “Overwrite” – means that this number will be overwritten by Geometry Reference; Size: 4 bytes                                                         |
| Offset             | [Array of Int](../file-format-definition#attrtype-int )  | Relative addresses of the current DMX channel from highest to least significant; Separator of values is ","; Special value: “None” – does not have any addresses; Default value: “None”; Size per int: 4 bytes |
| InitialFunction    | [Node](../file-format-definition#attrtype-node )         | Link to the channel function that will be activated by default for this DMXChannel. Default value is the first channel function of the first logical function of this DMX channel.                                                                                                                            |
| Highlight          | [DMXValue](../file-format-definition#attrtype-dmxvalue ) | Highlight value for current channel; Special value: “None”. Default value: “None”.                                                                                                                             |
| Geometry           | [Name](../file-format-definition#attrtype-name )         | Name of the geometry the current channel controls.                                                                                                                                                             |


</div>

The `Geometry` should be the place in the tree of geometries where the function
of the DMX Channel (as defined by ChannelFunction) is located either physically
or logically. If the DMX channel doesn't have a location, put it in the top
level geometry of the geometry tree. Attributes follow a trickle down
principle, so they are inherited from top down. 

As children the DMX channel has a list of [logical
channels](#logical-channel ).

###### Logical Channel

The Fixture Type Attribute is assigned to a LogicalChannel and defines
the function of the LogicalChannel. All logical channels that are
children of the same DMX channel are mutually exclusive. In a DMX mode,
only one logical channel with the same attribute can reference the same
geometry at a time. The name of a Logical Channel cannot be user-defined
and is equal to the linked attribute name. The XML node of the logical
channel is `<LogicalChannel>`. The currently defined XML attributes of the
logical channel are specified in [table 59](#table-59 ).

<div id="table-59">

#### Table 59. *Logical Channel Attributes*

| XML Attribute Name | Value Type                          | Description                                                                                                                                                                                  |
|----|----|----|
| Attribute          | [Node](../file-format-definition#attrtype-node )   | Link to the attribute; The starting point is the Attribute Collect (see [Annex A](/gdtf/annex/annex-a/)).                                                              |
| Snap               | [Enum](../file-format-definition#attrtype-enum )   | If snap is enabled, the logical channel will not fade between values. Instead, it will jump directly to the new value.; Value: “Yes”, “No”, “On”, “Off”. Default value: “No”                 |
| Master             | [Enum](../file-format-definition#attrtype-enum )   | Defines if all the subordinate channel functions react to a Group Control defined by the control system. Values: “None”, “Grand”, “Group”; Default value: “None”.                            |
| MibFade            | [Float](../file-format-definition#attrtype-float ) | Minimum fade time for moves in black action. MibFade is defined for the complete DMX range. Default value: 0; Unit: second                                                                   |
| DMXChangeTimeLimit | [Float](../file-format-definition#attrtype-float ) | Minimum fade time for the subordinate channel functions to change DMX values by the control system. DMXChangeTimeLimit is defined for the complete DMX range. Default value: 0; Unit: second |


</div>

As a child the logical channel has a list of a [channel
function](#channel-function ).

###### Channel Function

The Fixture Type Attribute is assigned to a Channel Function and defines
the function of its DMX Range. (XML node `<ChannelFunction>`). The
currently defined XML attributes of channel function are specified in
[table 60](#table-60 ).

<div id="table-60">

#### Table 60. *Channel Function Attributes*

| XML Attribute Name | Value Type                                   | Description                                                                                                                                                   |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )         | Unique name; Default value: Name of attribute and number of channel function.                                                                                 |
| Attribute          | [Node](../file-format-definition#attrtype-node )         | Link to attribute; Starting point is the attributes node. Default value: “NoFeature”.                                                                         |
| OriginalAttribute  | [String](../file-format-definition#attrtype-string )     | The manufacturer's original name of the attribute; Default: empty                                                                                             |
| DMXFrom            | [DMXValue](../file-format-definition#attrtype-dmxvalue ) | Start DMX value; The end DMX value is calculated as a DMXFrom of the next channel function – 1 or the maximum value of the DMX channel. Default value: "0/1". |
| Default            | [DMXValue](../file-format-definition#attrtype-dmxvalue ) | Default DMX value of channel function when activated by the control system.                                                                                   |
| PhysicalFrom       | [Float](../file-format-definition#attrtype-float )       | Physical start value; Default value: 0                                                                                                                        |
| PhysicalTo         | [Float](../file-format-definition#attrtype-float )       | Physical end value; Default value: 1                                                                                                                          |
| RealFade           | [Float](../file-format-definition#attrtype-float )       | Time in seconds to move from min to max of the Channel Function; Default value: 0                                                                             |
| RealAcceleration   | [Float](../file-format-definition#attrtype-float )       | Time in seconds to accelerate from stop to maximum velocity; Default value: 0                                                                                 |
| Wheel              | [Node](../file-format-definition#attrtype-node )         | Optional. Link to a wheel; Starting point: Wheel Collect                                                                                                      |
| Emitter            | [Node](../file-format-definition#attrtype-node )         | Optional. Link to an emitter in the physical description; Starting point: Emitter Collect                                                                     |
| Filter             | [Node](../file-format-definition#attrtype-node )         | Optional. Link to a filter in the physical description; Starting point: Filter Collect                                                                        |
| ColorSpace         | [Node](../file-format-definition#attrtype-node )         | Optional. Link to a color space in the physical description; Starting point: Physical Descriptions Collect                                                    |
| Gamut              | [Node](../file-format-definition#attrtype-node )         | Optional. Link to a gamut in the physical description; Starting point: Gamut Collect                                                                          |
| ModeMaster         | [Node](../file-format-definition#attrtype-node )         | Optional. Link to DMX Channel or Channel Function; Starting point DMX mode.                                                                                   |
| ModeFrom           | [DMXValue](../file-format-definition#attrtype-dmxvalue ) | Only used together with ModeMaster; DMX start value; Default value: 0/1                                                                                       |
| ModeTo             | [DMXValue](../file-format-definition#attrtype-dmxvalue ) | Only used together with ModeMaster; DMX end value; Default value: 0/1                                                                                         |
| DMXProfile         | [Node](../file-format-definition#attrtype-node )         | Optional link to DMX Profile; Starting point: DMX Profile Collect                                                                                             |
| Min                | [Float](../file-format-definition#attrtype-float )       | Minimum Physical Value that will be used for the DMX Profile. Default: Value from PhysicalFrom                                                                |
| Max                | [Float](../file-format-definition#attrtype-float )       | Maximum Physical Value that will be used for the DMX Profile. Default: Value from PhysicalTo                                                                  |
| CustomName         | [String](../file-format-definition#attrtype-string )     | Custom Name that can he used do adress this channel function with other command based protocols like OSC. Default: Node Name of the Channel function Example: Head_Dimmer.Dimmer.Dimmer   |



</div>

Note:  
For command based control systems, you can control the fixture by sending it a string in the following style:  
`"/FIXTURE_ID/CUSTOM_NAME_CHANNELFUCTION ,f FLOAT_VALUE_PHYSICAL"`  
or   
`"/FIXTURE_ID/CUSTOM_NAME_CHANNELFUCTION/percent ,f FLOAT_VALUE_PERCENT"`

Where:  
- FIXTURE_ID is the fixture ID is the value defined for the fixture instance.
- CUSTOM_NAME_CHANNELFUCTION is the Custom Name for the ChannelFunction. Note that all "." Separators can be replaced with "/".
- FLOAT_VALUE_PHYSICAL is the physical value that the fixture should adopt. The values will be capped by the fixture by PhysicalFrom and PhysicalTo.
- FLOAT_VALUE_PERCENT is the percent value that the fixture should adopt. The values can be between 0 and 100.


As children the channel function has list of a [channel
sets](#channel-set ) and a [sub channel
sets](#sub-channel-set ).

###### Channel Set

This section defines the channel sets of the channel function (XML node
<ChannelSet>). The currently defined XML attributes of the channel set
are specified in [table 61](#table-61 ).

<div id="table-61">

#### Table 61. *Channel Set Attributes*

| XML Attribute Name | Value Type                                | Description                                                                                                                                                                                                                                                   |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )         | The name of the channel set. Default: Empty                                                                                                                                             |
| DMXFrom            | [DMXValue](../file-format-definition#attrtype-dmxvalue ) | Start DMX value; The end DMX value is calculated as a DMXFrom of the next channel set – 1 or the maximum value of the current channel function; Default value: 0/1                      |
| PhysicalFrom       | [Float](../file-format-definition#attrtype-float )       | Physical start value. Default value is the PhysicalFrom from the parent channel function.                                                                                               |
| PhysicalTo         | [Float](../file-format-definition#attrtype-float )       | Physical end value. Default value is the PhysicalTo from the parent channel function.                                                                                                   |
| WheelSlotIndex     | [Int](../file-format-definition#attrtype-int )           | If the channel function has a link to a wheel, a corresponding slot index shall be specified. The wheel slot index results from the order of slots of the wheel which is linked in the channel function. The wheel slot index is normalized to 1. Size: 4 bytes |


</div>

The channel set does not have any children.

###### Sub Channel Set

This section defines the sub channel sets of the channel function (XML node
<SubChannelSet>). The currently defined XML attributes of the sub channel set
are specified in [table 62](#table-62 ).

<div id="table-62">

#### Table 62. *Sub Channel Set Attributes*

| XML Attribute Name | Value Type                                | Description                                                                                                                                                                                                                                                     |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )         | The name of the sub channel set. Default: Empty                                                                                                                                                                                                              |
| PhysicalFrom       | [Float](../file-format-definition#attrtype-float )       | Physical start value                                                                                                                                                                                                                                         |
| PhysicalTo         | [Float](../file-format-definition#attrtype-float )       | Physical end value                                                                                                                                                                                                                                           |
| SubPhysicalUnit    | [Node](../file-format-definition#attrtype-node )         | Link to the sub physical unit; Starting Point: Attribute                                                                                                                                                                                                     |
| DMXProfile         | [Node](../file-format-definition#attrtype-node )         | Optional link to the DMX Profile; Starting Point: DMX Profile Collect                                                                                                                                                                                        |


</div>

The sub channel set does not have any children.

#### Relation Collect
  
##### General

This section describes the dependencies between DMX channels and channel
functions, such as multiply and override. The relation collect currently
does not have any XML attributes (XML node `<Relations>`). As children the
relation collect has a list of a [relation](#relation ).

##### Relation

This section defines the relation between the master DMX channel and the
following logical channel (XML node `<Relation>`). The currently defined
XML attributes of the relations are specified in [table 63](#table-63 ).

<div id="table-63">

#### Table 63. *Relation Attributes*

| XML Attribute Name | Value Type                               | Description                                                      |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name )     | The unique name of the relation                                  |
| Master             | [Node](../file-format-definition#attrtype-node )     | Link to the master DMX channel; Starting point: DMX mode         |
| Follower           | [Node](../file-format-definition#attrtype-node )     | Link to the following channel function; Starting point: DMX mode |
| Type               | [Enum](../file-format-definition#attrtype-enum )     | Type of the relation; Values: “Multiply”, “Override”             |


</div>

The relation does not have any children. [Listing
1](#listing-1 ) shows an example of a simple DMX mode
described in XML.

<div id="listing-1">

#### Listing 1. *DMX mode with relations*

```
<DMXMode Name="Default" Geometry="Body">

   <DMXChannels>  
       <DMXChannel Highlight="255/1" Geometry="Pixel">  
           <LogicalChannel Attribute="Dimmer" Master="Grand">  
               <ChannelFunction Attribute="Dimmer" DMXFrom="0/1">  
                   <ChannelSet Name="closed" DMXFrom="0/1" PhysicalTo="0" />  
                   <ChannelSet DMXFrom="1/1" />  
                   <ChannelSet Name="open" DMXFrom="255/1" PhysicalFrom="1" />  
               </ChannelFunction>  
           </LogicalChannel>  
       </DMXChannel>  
       <DMXChannel DMXBreak="Overwrite" Offset="1" Default="255/1" Highlight="255/1" Geometry="Pixel">  
           <LogicalChannel Attribute="ColorAdd_R">  
               <ChannelFunction Attribute="ColorAdd_R" DMXFrom="0/1"/>  
           </LogicalChannel>  
       </DMXChannel>  
       <DMXChannel DMXBreak="Overwrite" Offset="2" Default="255/1" Highlight="255/1" Geometry="Pixel">  
           <LogicalChannel Attribute="ColorAdd_G">  
               <ChannelFunction Attribute="ColorAdd_G" DMXFrom="0/1"/>  
           </LogicalChannel>  
       </DMXChannel>  
       <DMXChannel DMXBreak="Overwrite" Offset="3" Default="255/1" Highlight="255/1" Geometry="Pixel">  
           <LogicalChannel Attribute="ColorAdd_B">  
               <ChannelFunction Attribute="ColorAdd_B" DMXFrom="0/1"/>  
           </LogicalChannel>  
       </DMXChannel>  
   </DMXChannels>  
   <Relations>  
       <Relation Name="VirtualDimmer" Master="Pixel_Dimmer" Follower="Pixel_ColorAdd_R.ColorAdd_R.ColorAdd_R 1" Type="Multiply" />  
       <Relation Name="VirtualDimmer" Master="Pixel_Dimmer" Follower="Pixel_ColorAdd_G.ColorAdd_G.ColorAdd_G 1" Type="Multiply" />  
       <Relation Name="VirtualDimmer" Master="Pixel_Dimmer" Follower="Pixel_ColorAdd_B.ColorAdd_B.ColorAdd_B 1" Type="Multiply" />  
   </Relations>
</DMXMode> 

```





#### Macro Collect
 
##### General

This section describes DMX sequences to be executed by the control
system. The macro collect currently does not have any XML attributes
(XML node `<FTMacros>`). As children the macro collect has a list of a
[macro](#macro ).

##### Macro
  
###### General

This section defines a DMX sequence. (XML node `<FTMacro>`). The currently
defined XML attributes of the macro are specified in [table
64](#table-64 ).

<div id="table-64">

#### Table 64. *Macro Attributes*

| XML Attribute Name | Value Type                        | Description                   |
|----|----|----|
| Name               | [Name](../file-format-definition#attrtype-name ) | The unique name of the macro. |
| ChannelFunction    | [Node](../file-format-definition#attrtype-node ) | Optional. Link to channel function; Starting point [DMX Mode](#dmx-mode) |


</div>

Macro children are specified in [table 65](#table-65 )

<div id="table-65">

#### Table 65. *Macro Children*

| XML node                          | Mandatory | Description                          |
|----|----|----|
| [MacroDMX](#macro-dmx ) | No        | This section defines a DMX sequence. |


</div>

###### Macro DMX

This section defines the sequence of DMX values which are sent by a
control system. (XML node `<MacroDMX>`). As children the macro DMX has a
list of [MacroDMXStep](#macro-dmx-step ).

###### Macro DMX Step

This section defines a DMX step (XML node `<MacroDMXStep>`). The currently
defined XML attributes of the macro DMX step are specified in [table
66](#table-66 ).

<div id="table-66">

#### Table 66. *Macro DMX Step Attributes*

| XML Attribute Name | Value Type                          | Description                                          |
|----|----|----|
| Duration           | [Float](../file-format-definition#attrtype-float ) | Duration of a step; Default value: 1; Unit: seconds. |


</div>

As children the macro DMX -Step has a list of a [DMX
Value](#dmx-value ).

###### DMX Value

This section defines the value for DMX channel (XML node
<MacroDMXValue>). The currently defined XML attributes of the DMX Value
are specified in [table 67](#table-67 ).

<div id="table-67">

#### Table 67. *DMX Value Attributes*

| XML Attribute Name | Value Type                                | Description                                                                                  |
|----|----|----|
| Value              | [DMXValue](../file-format-definition#attrtype-dmxvalue ) | Value of the DMX channel                                                                     |
| DMXChannel         | [Node](../file-format-definition#attrtype-node )         | Link to a DMX channel. Starting node [DMX Channel collect](#dmx-channel-collect ). |


</div>

The DMX value does not have any children.

