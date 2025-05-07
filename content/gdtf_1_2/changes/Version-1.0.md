---
title: "Version 1.0"
description: "Changelog for 1.0"
lead: "Changelog for 1.0"
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 230
toc: true
---

## Version 1.0

  - Geometry Type Axis: Removed XML attributes "From", "To" and "Speed";
    \#2
  - Changed enumeration of attribute names; \#33
  - Node Revision: added XML attribute "UserID"; \#17
  - Revisions are optional now. Every time a GDTF file is uploaded to
    GDTF-Share.com a revision with the actual time and UserID is created
    by the GDTF-Share; \#17
  - Geometry Type Geometry Reference: XML attribute "Model" added. \#24
  - All Geometry Nodes: XML attribute "Model" now uses value type
    "Name". \#77
  - Node Model: Changed description of XML attribute "File"; \#79
  - ChannelFunction: removed XML attribute DMXInvert; \#31
  - DMX Mode Children: Removed RDM Personality; \#79
  - Node DMXPersonality: Changed Value type of XML attribute DMXMode;
    \#79
  - Physical Description: Updated definition of emitters; \#34
  - Physical Description: Added definition of filters; \#34
  - Channel Function: Added XML attribute "Filter"; \#34
  - Wheel Slot: Added XML attribute "Filter"; \#34
  - Physical Description: Added definition of color space for indirect
    color mixing; \#34
  - Updated suggested names for Geometry Type "Geometry" and "Axis";
    \#19
  - Updated appendix A and B due to rework and addition of attributes;
    \#35
  - DMXChannel: Removed XML attributes "Coarse", "Fine", "Ultra" and
    "Uber" and added XML attribute "Offset" instead.
  - Fixture Type Node: Added XML attribute "LongName"; \#78
  - Fixture Type Node: Changed description of XML attribute "ShortName";
    \#78
  - Fixture Type Node: Changed description of XML attribute
    "Manufacturer"; \#78
