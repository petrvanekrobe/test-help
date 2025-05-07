---
title : "Add Channel Functions"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 80
---

Channel functions are used for bundling specific channel values, for example a strobe function of a shutter channel.


{{% notice important %}}
The value range of a DMX channel must completely be filled with channel functions. There must be no gaps and there must be no overlapping values.
{{% /notice %}}


{{% notice tip %}}
Refer to the fixture's DMX table and identify the available channel functions.
{{% /notice %}}


{{% notice important %}}
Every DMX channel must at least have one channel function and may have channel sets.
{{% /notice %}}

*   By default one channel function is created for every DMX channel.

 {{% image_inline src="../../media/window_DMX_channel_function_v1-1.png" alt="" %}} 

_Edit Channel Function window_

*   A channel function gets a name by default. This name can be changed.


{{% notice important %}}
The names of all channel functions of a DMX channel must be unique.
{{% /notice %}}

*   To open the Select Attribute window, click into the attribute input field.
    The Select Attribute window opens.
    Select the **Attribute** from the dropdown menu or search for it in the search field.

 {{% image_inline src="../../media/window_channel_function_select_attribute_v1-0.PNG" alt="" %}} 

_Select attribute window_

*   Select the matching attribute from the attribute list.


{{% notice tip %}}
For faster search through the attributes, use the selection box **Feature Group** as a filter, for example Position.
{{% /notice %}}

 {{% image_inline src="../../media/window_channel_function_select_attribute_2_v1-0.PNG" alt="" %}} 

_Selection box Feature Group window_

*   To define the lowest DMX value of this channel function, fill **DMX From**.
*   To switch the readout from 8bit, 16 bit, 32bit, 64bit to %, click the **arrow right** button.


{{% notice tip %}}
Changing the readout does not change the resolution of the property but allows to enter the values in a different resolution or as percentage.
{{% /notice %}}

*   To define the highest DMX value of this channel function, fill **DMX To**.
*   To switch the readout from 8bit, 16 bit, 32bit, 64bit to %, click the **arrow right** button.
*   To enter the physical value related to the lowest DMX value, fill **Physical From**.
*   To enter the physical value related to the highest DMX value, fill **Physical To**.

**Example:**

The DMX channel shutter of Robe's Megapointe has several different channel functions:

Shutter open

Shutter closed

Shutter strobe

Shutter strobe pulse open

Shutter strobe pulse close

Shutter strobe random

Every channel function must be added individually.


{{% notice tip %}}
The unit of the channel function is automatically defined when selecting the matching attribute!
{{% /notice %}}

 {{% image_inline src="../../media/window_DMX_channel_function_shutter_v1-1.png" alt="" %}} 

_Channel functions shutter_
