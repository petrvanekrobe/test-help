---
title : "Add Geometries"
description: "Geometries are used to describe the physical and logical dependencies of a fixture type."
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 10
---
## How to add geometries

Geometries are used to describe the physical and logical dependencies of a
fixture type. For example, dependencies between Pan and Tilt rotation as well
as dependencies between a Master Dimmer and a Dimmer of a subfixture. A valid
GDTF fixture type needs to have at least one geometry.

This chapter describes how to create geometries in an easy way.

To make things easier, look at your luminaire and think about the different
construction elements. "Disassemble" the luminaire in your mind and think of
the individual parts and what they do exactly.  By identifying the parts and
their functions, you can decide what type of geometry to use:

- **Static elements** (for visualisation only, e.g. a housing) ► Geometry Type
  **Normal Geometry**
- **Rotating elements** (e.g. the yoke and head of a moving light) ► Geometry
  Type **Axis**
- **Illuminated elements** (e.g. a lens) ► Geometry Type **Beam**

For a detailed description of all available geometry types, please see the GDTF
Spec.

If you would like to use your own 3D models, you now know which models (parts)
you need. To get these models, there are basically two ways:

1.  You already have a 3D model of the fixture. Then you can use a 3D modelling
software of your choice to export the needed parts as separate files.
2.  You don't have a 3D model of the fixture, but maybe a drawing or picture.
Then you can use a 3D modelling software to create the models from scratch and
export them as separate files.

When using high-resolution CAD models used for design and manufacturing of the
real device, you will likely exceed the recommended vertices count of 1200 for
the whole fixture. Such a high level of detail is not needed for visualising
the fixture. You should reduce the vertices count or re-draw the models,
keeping only the most relevant details.  Learn more about the requirements for
3D models in the GDTF Spec.

Next, think about the correct order of the geometries. Usually you start with
the part of the fixture which has the mounting points to attach it to a truss
or to put it on the floor. It can be a bracket or the base of a moving light,
for example. This geometry will be your **Top Level Geometry**.  Any other
geometries which are physically or logically attached to the Top Level Geometry
will be **Child Geometries**. A Child Geometry itself can have children as
well. This means you create a **tree structure**.

---

### Example 1: PAR can

One of the easiest luminaires in terms of geometries is a PAR can:

{{% image_inline src="../media/geometries-conventional.png" alt="" %}}

It consists of two geometries:

- The **"Body"**, which represents the housing of the PAR can. It has no
  special functions and is therefore a **Normal Geometry** type. Also, it is
  the part where you will attach a clamp to mount the fixture somewhere, so it
  is the **Top Level Geometry**.
- The "**Beam"**, which represents the front lens of the light source. It
  appears bright if you look at the fixture and it emits the beam, so it is a
  **Beam** geometry type. It is physically attached to the body, therefore it
  is a **Child Geometry** of the body. You can tell that by the indentation in
  the list.

If you move around the Body geometry, you will see that the Beam moves along -
this is how the top-down principle in the tree structure works. You will make
use of this concept in many other places when creating a GDTF fixture.

---

### Example 2: Moving light

This simple moving head, on the other hand, consists of four geometries:

{{% image_inline src="../media/geometries-movinglight.png" alt="" %}}

- The **"Base"** (**Normal Geometry** type), which is the **Top Level
  Geometry**
- The **"Yoke"**, which can rotate around the Pan axis and is therefore an
  **Axis** geometry type. It is physically connected to the Base and therefore
  a **Child Geometry** of the Base.
- The **"Head"**, which can rotate around the Tilt axis and is therefore an
  **Axis** geometry type as well. It is phyiscally connected to the Yoke and
  therefore a **Child Geometry** of the Yoke.
- The **"Beam"**, which represents again the front lens (not the light source
  itself!) and is therefore a **Beam** geometry type. It is physically
  connected to the Head and therefore a **Child Geometry** of the Head.

You will define whether an Axis geometry is a Pan or Tilt axis when creating
the corresponding DMX channels.

---

## Step-by-step guide to create the geometry structure of a basic moving light

We will now create a basic moving light, using only default models.

In a new GDTF file, the Geometry page will look like this:

{{% image_inline src="../media/screenshot-geometry-empty.PNG" alt="" %}}

_Empty Geometry page_

1.  Click on Add Top Level Geometry.  The Add Geometry pop-up opens.

{{% image_inline src="../media/screenshot-add-geometry-base.PNG" alt="" %}}

_Add Geometry pop-up_

2.  Fill in the **Name**, **Length**, **Width**, **Height**, **Geometry Type**
and **Select Model** as in the screenshot above. Then click on OK.  The
Geometry page will now look like this:

{{% image_inline src="../media/screenshot-geometry-base.png" alt="" %}}

Geometry page with Base

3.  With the Base geometry selected in the list, click on Add Child Geometry.
The Add Geometry pop-up opens again.

{{% image_inline src="../media/screenshot-add-geometry-yoke.png" alt="" %}}

Add Geometry pop-up

4.  Fill in the properties as in the screenshot above. Then click on OK.  Back
on the Geometries page, use the blue arrow handle to adjust the position of the
Yoke on the Z axis.

{{% image_inline src="../media/screenshot-geometry-base-yoke.png" alt="" %}}

Geometry page with Base and Yoke

5.  With the Yoke geometry selected in the list, click on Add Child Geometry.
The Add Geometry pop-up opens again.

{{% image_inline src="../media/screenshot-add-geometry-head.png" alt="" %}}

Add Geometry pop-up

6.  Fill in the properties as in the screenshot above. Then click on OK.  Back
on the Geometries page, use the blue arrow handle to adjust the position of the
Head on the Z axis.

{{% image_inline src="../media/screenshot-geometry-base-yoke-head.png" alt=""
%}}

Geometry page with Base, Yoke and Head

7.  With the Head geometry selected in the list, click on Add Child Geometry.
The Add Geometry pop-up opens again.

{{% image_inline src="../media/screenshot-add-geometry-lens.png" alt="" %}}

Add Geometry pop-up

8.  Fill in the properties as in the screenshot above. Then click on OK.  Back
on the Geometries page, use the blue arrow handle to adjust the position of the
Beam on the Z axis.

Learn more about the different Lamp Properties in the GDTF Spec.

**Important:** The Beam geometry must be positioned outside of the head.
Otherwise there will be no light output in the visualisation!

{{% image_inline src="../media/screenshot-geometry-base-yoke-head-beam.png"
alt="" %}}

Geometry page with Base, Yoke, Head and Beam

Now all geometries are created and positioned correctly.

If you would like to know how to deal with more complex geometry structures,
have a look at the chapter [How to Deal With Complex
Structures](3d027dc8-7d57-462d-b39b-ab8c8a4010b4).
