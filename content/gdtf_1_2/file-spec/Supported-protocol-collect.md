---
title: "Supported Protocol Collect"
description: "Describes supported protocols."
lead: "Describes supported protocols."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 140
toc: true
---

## Supported Protocol Collect
  
### General

If the device supports one or several additional protocols, these
protocol specific information have to be specified. The supported
protocol collect currently does not have any XML attributes (XML node
`<Protocols>`). Children of supported protocol collect are specified in
[table 69](#table-69 ).

<div id="table-69">

#### Table 69. *Supported Protocol Collect Children*

| XML node                                                   | Mandatory | Description                            |
|----|----|----|
| [RDM](#rdm-section )                             | No        | Describes RDM information              |
| [Art-Net](#art-net-section )                     | No        | Describes Art-Net information          |
| [sACN](#streaming-acn-section )                  | No        | Describes sACN information             |
| [PosiStageNet](#posi-stage-net-section )         | No        | Describes PosiStageNet information     |
| [OpenSoundControl](#open-sound-control-section ) | No        | Describes OpenSoundControl information |
| [CITP](#citp-section )                           | No        | Describes CITP information             |


</div>

### RDM Section

If the device supports the RDM protocol, this section defines the
corresponding information (XML node `<FTRDM>`). The currently defined XML
attributes of RDM are specified in [table 70](#table-70 ).

<div id="table-70">

#### Table 70. *RDM Attributes*

| XML Attribute Name | Value Type                      | Description            |
|----|----|----|
| ManufacturerID     | [Hex](../file-format-definition#attrtype-hex ) | Manufacturer ESTA ID   |
| DeviceModelID      | [Hex](../file-format-definition#attrtype-hex ) | Unique device model ID |


</div>

As children the FTRDM has a list of `SoftwareVersionID`.

#### SoftwareVersionID
  
##### General

For each supported software version add an XML node `<SoftwareVersionID>`.
The currently defined XML attributes are specified in [table 71](#table-71 ).

<div id="table-71">

#### Table 71. *SoftwareVersionID*

| XML Attribute Name | Value Type                      | Description         |
|----|----|----|
| Value              | [Hex](../file-format-definition#attrtype-hex ) | Software version ID |


</div>

As children the SoftwareVersionID has a list of `DMXPersonality`.

##### DMXPersonality

To define the supported software versions add an XML node
`<DMXPersonality>`. The currently defined XML attributes are specified in
[table 72](#table-72 ).

<div id="table-72">

#### Table 72. *DMXPersonality*

| XML Attribute Name | Value Type                        | Description                                                       |
|----|----|----|
| Value              | [Hex](../file-format-definition#attrtype-hex )   | Hex Value of the DMXPersonality                                   |
| DMXMode            | [Name](../file-format-definition#attrtype-name ) | Link to the DMX Mode that can be used with this software version. |


</div>

The DMXPersonality does not have any children.

### Art-Net Section
  
#### General

If the device supports the Art-Net protocol, this section defines the
corresponding information (XML node `<Art-Net>`).

As children the Art-Net has a list of [Maps](#map).

To define a custom mapping between Art-Net values and DMX Stream values you can add an XML node
`<Map>` as a child. The currently defined XML attributes are specified in
[table 73](#table-73 ).

By default, it is assumed that all the values are mapped 1:1, so only when you differ from that you can add a custom map.

#### Map

<div id="table-73">

#### Table 73. *Map Attributes*

| XML Attribute Name  | Value Type                            | Description                                                       |
|----|----|----|
| Key                 | [Uint](../file-format-definition#attrtype-uint )  | Value of the Artnet value.                                        |
| Value               | [Uint](../file-format-definition#attrtype-uint )  | Value of the DMX value.                                           |

</div>

### Streaming ACN Section
  
#### General

If the device supports the Streaming ACN protocol, this section defines the
corresponding information (XML node `<sACN>`).

As children the Streaming ACN has a list of [Maps](#map).

To define a custom mapping between Streaming ACN values and DMX Stream values you can add an XML node
`<Map>` as a child. The currently defined XML attributes are specified in
[table 73](#table-73 ).

By default, it is assumed that all the values are mapped 1:1, so only when you differ from that you can add a custom map.

### Posi Stage Net Section

This section has not yet been defined (XML node `<PosiStageNet>`).

### Open Sound Control Section

This is intentionally left empty. Future settings for custom OpenSoundControl behavior can be defined in later version. (XML node `<OpenSoundControl>`).


### CITP Section

This section has not yet been defined (XML node `<CITP>`).

