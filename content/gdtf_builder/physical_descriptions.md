---
title : "Physical Descriptions"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 70
---

## PhysicalDescriptions Page

The PhysicalDescrptions page allows defining Emitters, Filters and DMX profiles that can later be linked to a channel function of a DMX channel.

In the column on the left, all Emitters, Filters and DMX profiles are listed. When selecting an item, all of its properties can be viewed and edited in the big panel on the right.

{{% notice tip %}}
Emitter and Filter definitions are optional. Enter them only if real-world color measurements are available.
{{% /notice %}}


### Creating and Deleting PhysicalDescription Items

To create a new PhysicalDescription item, go to one of the tabs in the left panel (Emitter/Filter/DMX Profile) and click on **+** Add Emitter, **+** Add Filter or **+** Add DMX Profile.
To duplicate an item, select it, open the context menu (**≡**) and choose Duplicate Selection.
To delete an item, click the red **X** symbol.

### Emitter Properties

Select an emitter to display its properties.

The name of an emitter needs to be unique in order to identify it later. To set the Color of an emitter, either enter the values in the format CIE x, y, Y or click the edit symbol (📝) to open a color picker and choose a color.

### Filter Properties

Select a filter to display its properties.

The name of a filter needs to be unique in order to identify it later. To set the Color of a filter, either enter the values in the format CIE x, y, Y or click the edit symbol (📝) to open a color picker and choose a color.

### Spectral Distribution (Measurements)

Emitters and Filters allow entering measurements about the light output and spectral distribution at a given DMX percentage. This enables control and visualization applications to precisely calculate the color mixing characteristics of a device.

By default, the measurements describe the light output at a DMX value of 100% for the given emitter or filter. To add measurements for a different DMX value, click the **+** icon in the tab bar of the spectral distribution section.

Spectral distribution data can be imported from a CSV file. Click the **+** Import from CSV button and select a CSV file with measurements on the hard drive. Each measurement at a given DMX percentage can hold individual spectral distribution data. The CSV file must contain two columns separated by semicolon (**;**):

*   The wavelengths in nm in the first column.
*   The measured lighting energy at that wavelength in W/m²/nm in the second column.

{{% notice tip %}}
To read more about the definition of emitters and filters, see the GDTF Spec (section Physical Descriptions).
{{% /notice %}}

### DMX Profile Properties

A DMX profile defines the relation between a DMX input value and a physical output value. The name of a DMX profile needs to be unique in order to identify it later.

A DMX profile contains one or multiple points. Points contain a mathematical function to describe the relation between DMX input and physical output. To add a new point, click **+** Add new point. Each point has the following properties:

*   DMX Percentage: Position of the point on the x axis. The graph of the mathematical function assigned to the point is drawn in the positive direction.
*   CFC0: Cubic Function Coefficient for x⁰.
*   CFC1: Cubic Function Coefficient for x.
*   CFC2: Cubic Function Coefficient for x².
*   CFC3: Cubic Function Coefficient for x³.

{{% notice tip %}}
All given values are interpreted as percentage.
{{% /notice %}}


The following example shows how to create an S-curve DMX profile:

1.  Create a new DMX profile and add a new point.
2.  Leave DMX Percentage at 0.
3.  Set CFC2 = 200, leave the other CFCs at 0.
4.  Add a new point.
5.  Set DMX Percentage = 50.
6.  Set CFC0 = 50; CFC1 = 200; CFC2 = -200; leave CFC3 at 0.

An application that is using the data calculates the output the following way:

*   DMX Percentage: 0, 𝓍 ⟼ 200𝓍²
*   DMX Percentage: 0.5, 𝓍 ⟼ - 200(𝓍 - 0.5)² + 200(𝓍 - 0.5) + 50

 {{% image_inline src="../media/builder_physicaldescriptions_dmxprofile.png" alt="" %}} 
