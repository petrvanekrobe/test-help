---
title: "Revision Collect"
description: "This section defines the history of device type."
lead: "This section defines the history of device type."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 120
toc: true
---

## Revision Collect
  
### General

This section defines the history of device type. Revision collect
currently does not have any XML attributes (XML node `<Revisions>`). As
children the revision collect has a list of a
[revision](#revision ).

### Revision

This section defines one revision of a the device type (XML node
`Revision>`). Revisions are optional. Every time a GDTF file is uploaded
to the database, a revision with the actual time and UserID is created
by the database. The currently defined XML attributes of the revision
are specified in [table 68](#table-68 ).

<div id="table-68">

#### Table 68. *Revision Attributes*

| XML Attribute Name | Value Type                            | Description                                                                          |
|----|----|----|
| Text               | [String](../file-format-definition#attrtype-string ) | User-defined text for this revision; Default value: empty                            |
| Date               | [Date](../file-format-definition#attrtype-date )     | Revision date and time                                                               |
| UserID             | [Uint](../file-format-definition#attrtype-uint )     | UserID of the user that has uploaded the GDTF file to the database; Default value: 0 |
| ModifiedBy         | [String](../file-format-definition#attrtype-string ) | Name of the software that modified this revision; Default value: empty               |


</div>

The revision does not have any children.


