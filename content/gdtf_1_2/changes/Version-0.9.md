---
title: "Version 0.9"
description: "Changelog for 0.9"
lead: "Changelog for 0.9"
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 240
toc: true
---

## Version 0.9

  - Geometries are now always referenced by Name and not by Node Link;
    \#23
  - Fixed glitch in spec regarding ZIP-archive; \#8
  - Updated example for Data Version; \#4
  - Updated description of Model Node - Replaced wheel slot by model;
    \#5
  - Geometry type Beam: Changed name of XML attribute
    "LuminousIntensity" to "LuminousFlux";
  - Changed definition of value type "Date" corresponding to UTC;
  - Maximum count of vertices is now defined per device and not per
    model;
  - Removed optional checksum per file; \#7
  - Fixture type node: Added .svg as additional resource type for
    thumbnail; \#25
  - Changed maximum resolution of png files for thumbnail and wheel slot
    to 1024x1024; \#18
  - Updated format of value type "GUID" corresponding to RFC 4122; \#15
  - Defined folder structure for resource files; \#11 \#28
  - Links to all resource files do not have a file extension any longer;
  - Added first iteration of media server attributes; \#41
  - Added table for allowable UTF-8 chars for Names; \#64
  - Node ChannelSet: Changed description of XML attribute
    "WheelSlotIndex"; \#43
  - Defined more clearly how the wheel slot index is created; \#43
  - Updated RDM Section; \#69
  - Node DMXChannel: The XML attribute "Frequency" was removed; \#31
  - Node ChannelFunction: The XML attribute "EncoderInvert" was removed;
    \#31
  - Moved XML attributes "MibFade" and "DMXChangeTimeLimit" from the
    DMXChannel to the LogicalChannel; \#31
