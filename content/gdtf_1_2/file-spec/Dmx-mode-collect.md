---
title: "DMX Mode Collect"
description: "This section is describes all DMX modes of the device."
lead: "This section is describes all DMX modes of the device."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 110
toc: true
---

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
