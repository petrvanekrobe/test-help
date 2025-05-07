---
title: "Version 1.5"
description: "Specification for version 1.5"
lead: "Specification for version 1.5"
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 75
toc: true
---

### This document describes MVR Version 1.5

{{% badge style="primary" title="MVR Version" %}}1.5.0{{% /badge %}}

In the entertainment industry, the MVR file format allows programs to
share data and geometry for a scene. A scene is a set of parametric
objects such as fixtures, trusses, video screens, and other objects that
are used in the entertainment industry.

All objects used have a persistent unique ID to track changes between
the exchanging programs.

## Typical workflow

1.  Program A saves an MVR file containing a scene;
2.  Program B imports this file;
3.  Program B changes some parametric data in the scene;
4.  Program B saves an MVR containing the scene;
5.  Program A imports this file and applies the changes to the existing
    objects.

## Definition

An MVR file is a ZIP archive file containing one Root File named
`GeneralSceneDescription.xml`, along with all other files referenced via this Root File.

- The archive must not use encryption or password protection.
- All files referenced by the Root File shall be placed at the root level. They shall not be placed in folders.
- Files shall be placed using either STORE (uncompressed) or DEFLATE compression. No other compression algorithms are supported.
- Files may be placed into the archive in any order.
- A `Universal.gdtf` file can be added as template GDTF to define Gobos, Emitters und filter to reference.
- Filenames within the archive must not differ only by case. Eg it is prohibited to have the files `GEO1.glb` and `geo1.glb` within the same archive.

The file name of the ZIP archive can be chosen freely. The extension is:

`*.mvr`

Example of a typical MVR archive:

```
GeneralSceneDescription.xml
Custom@Fixture1.gdtf
Custom@Fixture2.gdtf
geo1.3ds
geo1.glb
Textr12.png
Universal.gdtf
```

References:
- [ISO/IEC 21320-1:2015 Document Container File - Part 1: Core](https://www.iso.org/standard/60101.html)
- [PKWARE 6.3.3](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)
- [Wikipedia ZIP (file format)](https://en.wikipedia.org/wiki/ZIP_(file_format))


