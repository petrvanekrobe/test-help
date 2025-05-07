---
title : "Wheels Page"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 80
---

The Wheels page allows defining all physical or virtual wheels of the device. Physical or virtual wheels represent the changes to the light beam within the device. The following functions of a device are typically decribed using wheels:

*   Color
*   Gobo
*   Prism
*   Animation
*   Content

In the column on the left, all wheels and their wheel slots are listed. When selecting a wheel slot, all of its properties can be viewed and edited in the big panel on the right.

### Creating and Deleting Wheels and Wheel Slots

To create a new wheel, click on **+** Add Wheel in the column on the left. A new wheel with one wheel slot is created.

To add another wheel slot to a wheel, click on **+** Add Wheel Slot.

To add multiple wheel slots, select the wheel where to add the wheel slots, open the context menu (**≡**) and choose Add Multiple Wheel Slots. Enter the number of slots to add in the pop-up.

To rename a wheel, click the edit symbol (📝).

To duplicate a wheel, select it, open the context menu (**≡**) and choose Duplicate selected Wheel.

To copy a wheel, right-click on its name and choose Copy Wheel. To paste a wheel, right-click on the name of and wheel and choose Paste Wheel.

To copy a wheel slot, right-click on its name and choose Copy Wheel Slot. To paste a wheel slot, select the wheel where to paste the wheel slot, right click on its name and choose Paste Wheel Slot.

To delete a wheel or wheel slot, click the **X** symbol.

### Wheel Slot Properties

Each wheel slot can contain color and gobo information, a link to a defined color filter, a description of an animation system and a description of a prism. If all properties of the wheel slot are at their default values, the wheel slot does not affect the output of the device.

### Color

To define a wheel slot that changes the color of the output of the device, enter the CIE xyY color value of the resulting color in the Color field or click the edit symbol (📝) to open a color picker.

To reset the color to its default value, click the **X** symbol.

### Gobo

To define a wheel slot that affects the output of the device by a gobo, click the edit symbol (📝) next to the Gobo field. A file picker opens. Select an image file that represents the gobo.

Read more about the requirements for gobo images in the GDTF Spec (Annex E (normative) Wheel Slot Image Definition).

### Filter

If the wheel slot describes a physical color filter, a link to a filter from the PhysicalDescriptions can be created. This allows more precise color calculation using spectral distribution data from the filter.
To link the wheel slot to an existing filter, select the filter from the drop-down list.

If a filter is linked, the information given in the Color field above is ignored and the color information from the filter is used instead.

### Animation Wheel

To define an animation wheel, attach a gobo image to the wheel slot first.

To edit the animation path, click the edit symbol (📝) next to the Animation Wheel field. Select Enable Animation Wheel to turn this wheel slot into an animation wheel.

An animation wheel has the following properties:

*   Radius: Defines the radius of the beam that passes through the animation wheel. The value is relative to the to the radius of the animation wheel. A value of 1 equals the radius of the animation wheel.
*   x-P1 | y-P1: Defines the position of the center of the beam when the animation wheel is fully removed from the beam. A value of 0 equals the center of the animation wheel, a value of 1 equals the radius of the animation wheel.
*   x-P2 | y-P2: Defines the position of the center of the beam when the animation wheel is half-way inserted into the beam.
*   x-P3 | y-P3: Defines the position of the center of the beam when the animation wheel is fully inserted into the beam.

The plot in the pop-up gives a visual representation of the values for the properties of the animation wheel. If the mouse cursor is moved along the animation path on the plot, the beam is visualized by a circle.

To display the gobo image in the plot, enable Show Gobo. The opacity of the gobo image can be adjusted in the opacity field.

{{% notice tip %}}
Show Gobo and Opacity only affect the rendering in the animation wheel editor. These values are not stored in the GDTF file.
{{% /notice %}}

### Prism Facets

Prism facets are used to break up the beam into multiple beams. For each prism facet, an offset, rotation, scaling and color value can be given.

To quickly create multiple prism facets, click on **+** Add Multiple Facets. In the pop-up, the following options are available:

*   Count: The number of prism facets to create
*   Position shift from center: Defines the position offset for the resulting beams from the center of the original beam. The position shift is relative to the beam radius. A value of 1 equals the beam radius.
*   Rotate facets around the center: If disabled, the prism facets are just shifted, but not rotated. If enabled, the prism facets are additionally rotated around the center of the beam.

To manually add one prism facet, click on **+** Add Entry. To edit and existing prism facet, click the edit symbol (📝). To delete a prism facet, click the **X** symbol.

When a prism facet is created or edited, an editor pop-up opens. In this editor, all existing prism facets can be viewed and edited.

In the preview plot on the right, the currently selected prism facet has a black outline. The other prism facets have a blue outline. The original beam has a thicker black outline.

To select a different prism facet, navigate through the facets using the Previous and Next buttons.

In the 2D transform matrix on the left, scaling, translation and rotation in horizontal and vertical direction can be adjusted for the selected prism facet. If the prism facet affects the color of the beam, a color value can be given.

To rotate the selected prism facet by a certain amount of degrees, click Rotate and enter the rotation in degrees.

{{% notice tip %}}
By default, the plot displays the beams as squares in order to make rotation visible. To display the beams as circles instead, enable Display as circle. This setting is not stored in the GDTF file.
{{% /notice %}}
