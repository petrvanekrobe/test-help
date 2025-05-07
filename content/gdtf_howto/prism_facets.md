--- 
title : "Handle Prisms"
description: "Prisms in GDTF are part of a Wheel and in particular, they are inside of what is called a Wheel Slot."
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 80
---

## How to define Prism facets

Prisms in GDTF are part of a Wheel and in particular, they are inside of what is called a Wheel Slot. Prisms definitions in GDTF allow precise definition of each prism facet and it is done by using transformations represented by Rotation matrices. There are many resources on rotation matrices, for example this Wikipedia article and also many game engine related tutorials and articles, like this one, which is useful for our 2D prism definitions.

In the GDTF Builder, there is a really nice Prism editor which can do some of the math for you, like rotations and transformation (movement):

![image.thumb.png.db7882ff18084a5039d85f95cfbfaa54.png](../media/defining_prisms_01.png)

The editor also allows you to visualize multiple facets at the same time and show a circular view, which is useful for checking the final result. Here you can see linear and circular prism represented by the Rotation matrix and also visually:

![514156784_Peek2021-03-2711-44b.thumb.gif.aa410dc7da4b45e03f26b0664e2775c9.gif](../media/defining_prisms_02.gif)

![1319875171_Peek2021-03-2711-44.thumb.gif.cd43a6cd3cb7eece1d75eb1567f9700f.gif](../media/defining_prisms_03.gif)

When defining prisms/prism facets, it is good to know how the Rotation matrix works or at least what each field means. Here i labeled the fields important for prism definition:

![image.png.ac6ef3c22788920472fb3f6da81d2534.png](../media/defining_prisms_04.png)

It is important to know what are the units used for the transformation. For the sake of simplicity, we can say here that the unit used in the matrix is "the radius of the unaltered beam". This sounds weird, so lets make an example:

Let's say, that we want to define a linear prism, which looks like this:

![image.png.716eaa77a251b6bf4a49fffcbf0f7684.png](../media/defining_prisms_05.png)

We need to define three beams.

First one in an unaltered form, so horizontal and vertical scale are 1, and there is no rotation and no offset (translation):

 {{% image_inline src="../media/defining_prisms_06.png" alt="" %}} 

Now we define one facet to the left, touching the first beam. As the translation is to the left (negative) and it it 2x the radius of the unaltered beam, we enter -2 into the Horizontal translation field:

 {{% image_inline src="../media/defining_prisms_07.png" alt="" %}} 

Now, we define the facet to the right, just touching the first beam. As the translation is 2x the radius of the unaltered beam, we enter 2 into the Horizontal translation field:

 {{% image_inline src="../media/defining_prisms_08.png" alt="" %}} 

So anytime we want to move the beam from the original position, we simply use the original beam as the reference. Of course, in real life, we will need to do a bit of math, here is a practical example:

**Linear 4-facet prism**

Measured projection on a wall:

Unaltered beam diameter: 53
Offset of beam centers from center of unaltered beam, facets 1,2,3,4: -99, 30, 30, 99

Vertical translation:

facet 3: 30/53\*2 = 1.1320754716981132

facet 4: 99/53\*2 = 3.7358490566037736

facet 1: negative value of facet 4

facet 2: negative value of facet 3

Horizontal and vertical Scale:
If the altered beam was different, for example 55: 55/53=1.0377358490566038

Resulting preview:

 {{% image_inline src="../media/defining_prisms_09.png" alt="" %}} 

And the definition:

 {{% image_inline src="../media/defining_prisms_10.png" alt="" %}} 

**Circular prisms**

The Builder Prism facet editor contains a handy tool to define what is the offset of the facets from the center and will calculate parameters for the desired number of facets placed in a circle around the center:

 {{% image_inline src="../media/defining_prisms_11.png" alt="" %}} 

Here is the initial generated result (preview):

 {{% image_inline src="../media/defining_prisms_12.png" alt="" %}} 

And the definition:

![image.png.85573f083ff97a22ddd3dae650b7f8df.png](../media/defining_prisms_13.png)

But you must pay attention also to the rotation of each facet. The above example shows us that some facets are actually rotated:

 {{% image_inline src="../media/defining_prisms_14.png" alt="" %}} 

Which we must adjust by using the Rotate tool on each of the facets where this is required (-90, -180, -270):

 {{% image_inline src="../media/defining_prisms_15.png" alt="" %}} 

To achieve our final look:

 {{% image_inline src="../media/defining_prisms_16.png" alt="" %}} 

And definition:

 {{% image_inline src="../media/defining_prisms_17.png" alt="" %}} 

Now you have a basic understanding on how to define prism facets in GDTF.
