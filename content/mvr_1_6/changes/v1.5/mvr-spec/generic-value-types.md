---
title: "Generic value types"
description: "Here is a list of the available types for node or attribute values."
lead: "Here is a list of the available types for node or attribute values."
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 120
toc: true
---
# Generic Value Types

Here is a list of the available types for node or attribute values:

| Value Type Name                               | Description                                                                                                                                                                                       |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span id="attrtype-integer"> Integer </span>  | A signed or unsigned integer value represented in base 10. Uses a dash '-' (U+002D) as a prefix to denote negative numbers<br/>Eg `15` or `-6` |
| <span id="attrtype-float"> Float </span>      | A floating point numeric value represented in base 10 decimal or scientific format.<br/>Uses full stop '.' (U+002E) to delimit the whole and decimal part and 'e' or 'E' to delimit mantissa and exponent.<br/>Implementations shall write sufficient decimal places to precisely round-trip their internal level of precision.<br/>Infinities and not-a-number (NaN) are not permitted.<br/>Eg `1.5`, `3.9265e+2` |
| <span id="attrtype-string"> String </span>    | Any sequence of Unicode codepoints, encoded as necessary for XML.<br>Eg The following XML encodings (with their meaning in brackets):<br/>`&lt;` (\<), `&amp;` (&), `&gt;` (\>), `&quot;` ("), and `&apos;` (') |
| <span id="attrtype-uuid"> UUID </span>        | A UUID to RFC4122 in text representation.<br/>The nil UUID (all zeros) is not permitted.<br/>Formatted as `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX` |
| <span id="attrtype-vector">Vector</span>      | Three Float values separated by ',' defining a 3D vector's X, Y, and Z components.<br/>Eg `1.0,2.0,3.0` |
| <span id="attrtype-filename">FileName</span>  | The case-sensitive name of a file within the archive.<br/>The filename must not contain any FAT32 or NTFS reserved characters.<br/>The extension is delimited from the base name by full stop '.' and the base name shall not be empty.<br/>It is recommended to limit filenames to the POSIX "Fully Portable Filenames" character set: [A-Z], [a-z], [0-9], the symbols '\_' (U+005F), '-' (U+002D) and a maximum of one '.' (U+002E)<br/>Eg `My-Fixture_5.gdtf` |
| <span id="attrtype-ciecolor">CIE Color</span> | CIE 1931 xyY absolute color point.<br/>Formatted as three Floats `x,y,Y`<br/>Eg `0.314303,0.328065,87.699166`|

