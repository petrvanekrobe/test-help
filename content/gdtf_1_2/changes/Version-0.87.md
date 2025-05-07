---
title: "Version 0.87"
description: "Changelog for 0.87"
lead: "Changelog for 0.87"
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 260
toc: true
---

## Version 0.87

  - Changing format of type Matrix and Rotation;
  - New XML attribute of DMX Channel - Uber;
  - Attribute has no more Special XML attribute;
  - Pigtail position should not be specified in 2D or 3D files anymore.
    Instead of it should be created a general geometry and linked to a
    model with primitive type “Pigtail”;
  - Measurement point does not have DMX and Color XML properties
    anymore;
  - Added specification to 3D mesh;
  - Added new part Color rendering index collect;
  - Added new part Supported protocol collect and moved RDM section to
    this part;
  - GDTF file should have extension “.gdtf”;
  - Subattributes are no more part of GDTF. Instead Attributes get a new
    XML attribute “MainAttribute”;
  - Macro Collect moved into DMX Mode and is defined;
  - Channel Set has no more XML attribute Real Fade;
  - Defined measurement resolution for Emitters;
  - Logical Channel and DMX Channel has an automatically generated name,
    which cannot be specified in XML.

