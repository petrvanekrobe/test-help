---
title : "Channel Function Properties"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 90
---

To edit the additional properties of a channel function, click **Edit Additional Properties** at the bottom of a channel function tile.

 {{% image_inline src="../../media/window_DMX_channel_function_v1-1.png" alt="" %}} 

_Channel function additional properties_

The channel function additional properties opens.

 {{% image_inline src="../../media/window_DMX_editor_channel_function_v1-0.PNG" alt="" %}} 

_Channel function additional properties_

*   Enter the manufacturer's **original name** of the attribute.
*   Enter the link to an existing **emitter**. To add a new emitter, type the emitter name and click **Add**.
    The color information of the emitter can be used for visualization or color mixing control of the channel function.
*   Enter the link to an existing **filter**. To add a new filter, type the filter name and click **Add**.
    The color information of the filter can be used for visualization or color mixing control of the channel function.
*   Enter the link to an existing **wheel**. To add a new wheel, type the wheel name and click **Add**.
    The information of the wheel can be used for visualization of the channel function.


{{% notice tip %}}
The emitter, filter and wheel can also be defined in physical descriptions first.
{{% /notice %}}

*   Enter the **real fade** time.
    Real fade defines how long it takes for the device to travel from the start to the end of the DMX range that is described with this channel function. For example, how long does it take to rotate the pan from minimum to maximum. The value is defined in seconds. The real fade time is used for visualization.
*   Select the **Mode Master Defined By.**
    Defines if the mode master is a DMX channel or a channel function.
*   Select the **mode master** of a mode dependency from the dropdown menu.
*   To define the lowest DMX value of the linked DMX channel or channel function to activate the current channel function, fill **Mode From**.
*   To switch the readout from 8bit, 16 bit, 32bit, 64bit to %, click the **arrow right** button.
*   To define the highest DMX value of the linked DMX channel or channel function to activate the current channel function, fill **Mode To**.
*   To confirm, click **OK**.
