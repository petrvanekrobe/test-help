---
title : "Add mode dependencies"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 110
---

Some attributes change function based on the value of a different attribute. An attribute that controls the rotation mode of a gobo, for example. Imagine a fixture that has an attribute that is used to select a gobo on a gobo wheel. First range of the DMX range will select the different gobos on the wheel, but the gobos are in an "index" mode. A second attribute controls the rotation of the gobo. When the selected gobo is in index mode, the rotation is set to be a degree number. The second range of the selection attribute also selects all the gobos on the wheel, but now in a continuous rotation mode. The rotation attribute will now control the rotation speed and direction.

The following example describes the rotating gobo of a device. There are two DMX channels that are used to control this unit. The first DMX channel (attribute Gobo1) has two channel functions. The first channel function (Attribute Gobo1) describes the selection of indexed and rotating gobos.

 {{% image_inline src="../../media/window_channel_function_mode_depe_v1-0.png" alt="" %}} 

_Channel function_

There are two value ranges that describe the selection of the individual gobos in indexed or continuous rotation mode. For every gobo there is a channel set for index and continuous rotation mode.

 {{% image_inline src="../../media/window_channel_function_mode_depe_2_v1-0.png" alt="" %}} 

_Channel sets_

The second channel function (Attribute Gobo1WheelSpin) is used to describe the continuous rotation of the whole gobo wheel.

The second DMX channel has two channel functions. The first channel function (Attribute Gobo1Pos) describes the indexed mode of the rotating gobos.

 {{% image_inline src="../../media/window_mode_master_container_1_v1-0.png" alt="" %}} 

_Mode master container 1_

The second channel function (Attribute Gobo1PosRotate) describes the continuous rotation mode of the rotating gobos.

 {{% image_inline src="../../media/window_mode_master_container_2_v1-0.png" alt="" %}} 

_Mode master container 2_

Both channel functions cover the complete DMX value range of the DMX channel. This is why every channel function needs its own Mode Master Container.


{{% notice tip %}}
Every mode master container covers the complete DMX value range of the DMX channel.
A mode master can contain one or several channel functions.
{{% /notice %}}


{{% notice important %}}
The value range of a mode master container must completely be filled with channel functions. There must be no gaps and there must be no overlapping values.
{{% /notice %}}

The functionality of these different ranges of the two DMX channels is linked by mode dependencies. If an indexed gobo is selected on the first DMX channel, the second channel controls the index rotation. If a continuous rotating gobo is selected on the first channel, the second channel controls the direction and the speed of the rotating gobo.
The DMX value range of the selection of an indexed gobo on channel 1 goes from DMX 0 to DMX 50; The value range of the selection of rotating gobos goes from DMX 51 to DMX 90.

To link the two DMX channels open the additional properties of the channel function with attribute GoboPos.

To open the additional properties click Edit Additional Properties.

This channel function is active when the DMX channel that controls Gobo1 is in the range between 0 and 50.

This is why you make the selections as shown below:

 {{% image_inline src="../../media/window_mode_follower_v1-1.png" alt="" %}} 

_Additional properties window_

The channel function with the attribute Gobo1PosRotate should be active when the DMX channel that controls the gobo is in the range between 51 and 90.

 {{% image_inline src="../../media/window_mode_follower_2_v1-1.png" alt="" %}} 

_Additional properties window_
