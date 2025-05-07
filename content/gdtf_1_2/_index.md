---
title: "GDTF Spec"
description: "GDTF documentation"
lead: ""
date: 2020-10-06T08:48:23+00:00
lastmod: 2020-10-06T08:48:23+00:00
draft: false
images: []
weight: 10
---

This document describes the [DIN SPEC 15800:2022-02](https://www.dinmedia.de/en/technical-rule/din-spec-15800/349717520) also known as GDTF Version 1.2.

{{% badge style="primary" title="GDTF Version" %}}1.2{{% /badge %}} {{% badge style="primary" title="DIN SPEC" %}}15800:2022-02{{% /badge %}}

## Introduction

In the lighting and entertainment industry, lighting fixtures
(luminaires and other controllable devices) have become more and more
complex, and the development of these devices happens faster than ever.
New devices are designed with very involved structures; they have
numerous complex color-mixing systems and mode dependencies. To give the
user access to the enormous flexibility of existing devices, a method of
providing accurate fixture type data, and controlling and
pre-visualizing devices quickly and precisely as possible, is needed.
The "General Device Type Format" (GDTF) is that method.

There are many different lighting consoles and software manufacturers on
the market, and all of them use different file formats and methods of
getting the fixture control information into their systems. The
development of new high-end fixtures at an amazing rate creates a lack
of available control data on the side of the console and
pre-visualization software manufacturers. Also, fixture manufacturers
are often approached directly by their clients with requests to support
them with accurate fixture types. As there are so many different
consoles and visualizers on the market, this process requires vast
knowledge of many different systems. Fixture manufacturers would need to
understand how every console or visualizer works, and how to provide the
required data. A format description is needed that not only provides all
of the required control information, but also structures it in a
hierarchical way matching that of the described device.

The lighting designer who would like to use these devices has to deal
with such obstacles. Designers often receive the device control data of
a specific new fixture later than expected. Also, the data may be
incomplete, because it was not created with the latest information from
the fixture manufacturer.

These issues demonstrate that our industry needs a standardized way of
defining the description of intelligent and complex devices. This
document defines such a data format. After the DIN SPEC has been
published, the format will continue to be developed further, but it is
important to make an initial version publicly available. Topics for
which no specifications can be made at this time, but which will soon
become necessary, are therefore already included in this DIN SPEC, but
with a note that no specifications can be made now.
