---
title : "Add Channel Set"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 100
---

Channel sets can be used for defining individual functions, for example minimum and maximum strobe speed or wheel slots.

 {{% image_inline src="../../media/window_DMX_channel_set_add_v1-1.png" alt="" %}} 

_Add channel set_

*   To add a new channel set, click **Add Channel Set**.
    A new line Empty Channel Set is added.

{{% notice tip %}}
To add multiple channel sets click at **Add Multiple Channel Sets** and enter the count.
{{% /notice %}}

*   Fill the fields with the respective information.

**Use Parent Physical**

This option defines whether the physical values of the channel sets are taken from the corresponding channel function or are defined individually for the channel set. By default this option is enabled.

{{% notice tip %}}
Disable **Use Parent Physical** to enter individual physical values for a channel set.
{{% /notice %}}

**Wheel Slot**

The channel set is linked to the respective slot of a wheel by the wheel slot number. The link to the wheel is defined in the channel function.

 {{% image_inline src="../../media/window_channel_set_wheel_slot_v1-1.png" alt="" %}} 

_Wheel Slot window_


{{% notice important %}}
Make sure that the wheel slot in the wheel definition matches the wheel slot number in the channel set.
The index is shown between the preview and the wheel slot name.
{{% /notice %}}

 {{% image_inline src="../../media/window_channel_set_wheel_slot_2_v1-0.png" alt="" %}} 

_Color wheel 1 slots with wheel slot index_
