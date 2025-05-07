---
title : "Summary"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 90
---

## Summary Page

The Summary Page provides an overview of the following properties of the fixture type:

### Attributes

 {{% image_inline src="../media/builder_summary_attributes.png" alt="" %}} 

All used attributes and their properties are listed here. Predefined attributes show a briefcase icon (💼), custom attributes show a user icon (👤).
Click on the edit icon (📝) to edit a custom attribute. Predefined attributes cannot be edited.

### Activation Groups

 {{% image_inline src="../media/builder_summary_activationgroups.png" alt="" %}} 

All used attributes that belong to an Activation Group are listed here. To change the Activation Group of a custom attribute, edit the attribute in the Attributes summary.
Activation Groups for predefined attributes cannot be changed.

### Feature Groups

 {{% image_inline src="../media/builder_summary_featuregroups.png" alt="" %}} 

All used attributes are displayed in their Feature Groups and Features here. To change the Feature Group or Feature of a custom attribute, edit the attribute in the Attributes summary.
Feature Groups or Features for predefined attributes cannot be changed.

### DMX Mode Overview

 {{% image_inline src="../media/builder_summary_dmxmode_1.png" alt="" %}} 

All DMX channels of a DMX mode are listed here. To view a different DMX mode, select it from the drop-down list.

The DMX channels are listed separately for each DMX break. For each DMX channel, additional information is displayed:

*   HL: Highlight value
*   DF: Default value
*   RTM: React To Master setting

To identify DMX address conflicts, a DMX address is highlighted in red if two or more DMX channels are assigned to one address.
Unassigned DMX addresses are highlighted in yellow.

 {{% image_inline src="../media/builder_summary_dmx_error_1.png" alt="" %}} 

DMX address conflict

### DMX Channels by Geometry

 {{% image_inline src="../media/builder_summary_dmxchannels.png" alt="" %}} 

Here all DMX channels are grouped by the geometry they are assigned to.

### Revisions

 {{% image_inline src="../media/builder_summary_revisions.png" alt="" %}} 

All previous revisions of the fixture type are listed here, showing the revision text and revision time. To edit the revision text, click on the Edit icon (📝). To delete a revision from the revisions list, click on the Delete icon (❌).

{{% notice tip %}}
Modifying revisions in the summary will only affect the revisions history of the current GDTF file. It will not affect revisions of this fixture type on the GDTF share. To manage revisions on the GDTF share, continue reading [here](fixture_information).
{{% /notice %}}
