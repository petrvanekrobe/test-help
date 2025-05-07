---
title : "Adding Geometries"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 10
---

To create a new geometry, click on **+** Add Top Level Geometry or **+** Add Child Geometry in the Geometries list. The Add Geometry pop-up opens.

 {{% image_inline src="../../media/builder_add_geometry.PNG" alt="" %}} 

### General Properties

The name of a geometry has to be unique for the whole GDTF file.

If Use File Dimensions is enabled, the geometry receives its dimensions from the linked 3D model. If Use File Dimensions is disabled, the dimensions given in the Length, Width and Height fields are used.
Use File Dimensions is not available for the included standard models (primitive types).

### Geometry Type

Defines special functions of the geometry. Read more about the available geometry types in the GDTF Spec (section Geometry Collect).

### Select Model

To link a 3D model to the geometry, use one of the following options:

*   Upload Mesh...: Opens a file browser to choose and upload a 3D model from the hard drive.
*   New Default Base etc.: Creates a new instance of one of the available primitive types.
*   Existing model: Use this option to link a model that already exists in the GDTF file.
*   New Empty Geometry: No 3D model is linked to the geometry.
{{% notice tip %}}
After a custom model is linked, it is possible to upload additional levels of detail for that model. This can be done in the model properties.

 {{% image_inline src="../../media/builder_models_quality_1.png" alt="" %}} 

Read more about the requirements for 3D models in the GDTF spec (section Model Collect).

{{% /notice %}}
When clicking OK, a geometry with all the given properties is created.
