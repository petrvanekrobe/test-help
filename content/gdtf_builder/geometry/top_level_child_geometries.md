---
title : "Top-Level vs. Child Geometries"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 20
---

### Top-Level Geometries

A top-level geometry is the starting point of a new geometry tree. It usually represents the part of a device where it is mounted to any kind of support structure, e.g. the base of a moving light fixture or the yoke of a PAR can.

### Child Geometries

A child geometry is a subordinate geometry inside a geometry tree. It always depends on its parent object. Each child geometry has exactly one parent geometry and it can have multiple child geometries itself.

Child geometries represent parts of a device which are physically and/or logically connected to their parent object.

The position and rotation of a child geometry is always relative to its parent geometry.

Furthermore, control and visualization applications can make use of the geometry structure to inherit controls from a parent object to its children or vice versa.

### Transformation Between Top-Level and Child Geometries

To transform a top-level geometry into a child geometry, drag and drop it on top of the desired parent object. This will make the geometry a child of that parent object.

To transform a child geometry into a top-level geometry, drag and drop it on the **+** Add Top Level Geometry or **+** Add Child Geometry labels.
