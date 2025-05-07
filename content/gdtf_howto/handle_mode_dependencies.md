---
title : "Mode Dependencies"
description: "Some fixtures have channels which control different functions depending on the state of another channel."
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 50
---

## How to handle Mode Dependencies

Some fixtures have channels which control different functions depending on the state of another channel. This behavior is called mode dependency. In GDTF, such mode dependencies can be described using **Mode Master Containers**.

Examples for mode dependencies are:

*   Gobo Position depending on the Gobo channel (Indexing vs. Rotation)
*   Shutter depending on a Strobe Mode channel (Strobe vs. Random Strobe vs. Pulse)
*   Color Macro depending on a Swatchbook channel

Mode dependencies can currently not be used for functions which are toggled in the fixture's firmware (e.g. setting Dimmer curves through the "Control" channel), as the current mode setting is in that case not connected to a unique DMX value and return channels are not supported.

This chapter describes how to set up mode dependencies for a Gobo and Gobo Rotate channel.

## Starting point

We want to describe a Gobo wheel which has indexing, rotation and shake functions and is controlled by two channels. Depending on the state of the first channel which selects the Gobos, the second channel controls either the indexing angle or the rotation speed of the current Gobo.

The Gobo wheel looks like this:

 {{% image_inline src="../media/screenshot-wheels-gobo.png" alt="" %}} 

If you would like to know how to create wheels, have a look at the [How to handle wheels](handle_wheels) chapter.

 The DMX channel which controls the selection of Gobos looks like this:

 {{% image_inline src="../media/screenshot-dmx-gobo1.png" alt="" %}} 

## Creating the Gobo Position channel

1.  On the DMX page, in this list of DMX channels on the left, create a new channel by clicking on Add Channel.
    The Add New Channel pop-up opens.
2.  For **Geometry**, select the same geometry as for the existing Gobo channel, in this case the "Head".
    Then click in the **Attribute** field. The Select Attribute pop-up opens.
3.  Search for the **Gobo1Pos** attribute, select it and confirm both pop-ups by clicking OK.

    For the attribute of the Logical Channel, it is best to use a common attribute of all its Channel Functions (in this case Gobo1Pos for the Channel Functions Gobo1Pos (indexing) and Gobo1PosRotate (rotation)).

4.  For more precise control, we're going to make it a 16 bit channel by setting the **Resolution** to 16 bit and giving a **Fine** DMX address.

     {{% image_inline src="../media/screenshot-resolution-16bit.png" alt="" %}} 

5.  The first **Channel Function** is the Indexing function, which uses the **Gobo1Pos** attribute. It is the same as for the logical channel and therefore automatically set for the Channel Function. With this channel function, you can set a fixed rotation angle between 180° and -180° for the current Gobo. The properties of the Channel Function are the following:

     {{% image_inline src="../media/screenshot-dmx-channel-function-gobo1pos.png" alt="" %}} 


## Setting the mode dependency for the first Channel Function

1.  To set the channel it is depending on and the range of values where it is active, go to the Edit Additional Properties menu of the Channel Function.
2.  There are two ways to define a Mode Master: either by **DMX Channel** or by **Channel Function**. While "DMX Channel" is the standard approach, you could even build cascades of mode dependencies using the "Channel Function" option. In our case, "DMX Channel" is the way to go.

     {{% image_inline src="../media/screenshot-modemaster-defined-by.png" alt="" %}} 

3.  For **Mode Master**, select the channel on which our channel depends, in this case "Head\_Gobo1".

     {{% image_inline src="../media/screenshot-modemaster-gobo1.png" alt="" %}} 

4.  Finally, define in which range of DMX values for the master channel our channel function should be active. Confirm by clicking OK.

     {{% image_inline src="../media/screenshot-mode-from-to.png" alt="" %}} 

## Creating a second Mode Master container

The first channel function already covers the whole range of DMX values for this channel. To add a second channel function, we first have to add a mode master container.

1.  Click on Add Mode Master Container. A second container will be created with a channel function. Please change the properties of the channel function to the following (using your own DMX and Physical values if needed):

     {{% image_inline src="../media/screenshot-dmx-channel-function-gobo1posrotate.png" alt="" %}} 

2.  Repeating the steps of the previous paragraph, set the mode dependencies to the following values. You can see that these values match the corresponding channel function of the Gobo1 channel:

     {{% image_inline src="../media/dmx-mode-master-channel-function.png" alt="" %}} 

## Creating a third Mode Master container

The third channel function controls the indexing like the first one, but now for the shake function of the Gobo1 channel. So you can copy and paste it and change the mode dependency afterwards.

1.  Create a third Mode Master Container by clicking on Add Mode Master Container.
2.  Select the first channel function, right-click on it and choose Copy.
3.  Select the third channel function (currently a "No Feature"), right-click on it and choose Paster After.
4.  Delete the "No Feature" channel function and select Gobo Wheel 1 for **Wheel** in your pasted channel function. Change the **Name** to a unique one.
5.  In the Edit Additional Properties of the channel function, set the mode dependencies the following:

     {{% image_inline src="../media/screenshot-modemaster-gobo1-2.png" alt="" %}} 

## Result

The Gobo1Pos channel now reacts to the state of the Gobo1 channel:

|     |     |     |
| --- | --- | --- |
| **Gobo1 value** | **Gobo1 function** | **Gobo1Pos function** |
| 0...34 | Select Gobo for indexing | Rotation angle of current Gobo |
| 35..59 | Select Gobo for rotation | Rotation speed of current Gobo |
| 60...209 | Select Gobo for shake and  <br>control the shake frequency | Rotation angle of current Gobo |

*   In every mode master container, the whole range of DMX values for the channel needs to be covered by channel functions
*   For ranges with no functions, create channel functions using the "No Feature" attribute
