---
title: "Generic value types"
description: "Generic value types"
lead: "Generic value types"
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 220
toc: true
---

## Generic Value Types

Table 1 contains a list of the available types for node or attribute values:

##### Table 1 — *XML Generic Value Types*

| Value Type Name    | Description                                      |
| ------------------ |--------------------------------------------------------------------------- |
| <span id="user-content-attrtype-integer"> Integer </span>  | A signed or unsigned integer value represented in base 10. Uses a dash ‘-’ (U+002D) as a prefix to denote negative numbers. E.g. `15` or `-6`|
| <span id="user-content-attrtype-float"> Float </span>      | A floating point numeric value represented in #attrType-Bool base 10 decimal or scientific format.<br/>Uses full stop '.' (U+002E) to delimit the whole and decimal part and 'e' or 'E' to delimit mantissa and exponent.<br/>Implementations shall write sufficient decimal places to precisely round-trip their internal level of precision.<br/>Infinities and not-a-number (NaN) are not permitted.<br/>Eg `1.5`, `3.9265e+2`|
| <span id="user-content-attrtype-bool"> Bool </span>        | A boolean value. When representing `true` inidcate with true, when `false` indicate with false. | 
| <span id="user-content-attrtype-string"> String </span>    | Any sequence of Unicode codepoints, encoded as necessary for XML.<br>Eg The following XML encodings (with their meaning in brackets):<br/>`&lt;` (\<), `&amp;` (&), `&gt;` (\>), `&quot;` ("), and `&apos;` (') |
| <span id="user-content-attrtype-enum"> Enum </span>        | Possible values are predefined |  
| <span id="user-content-attrtype-uuid"> UUID </span>        | A UUID to RFC4122 in text representation.<br/>The nil UUID (all zeros) is not permitted.<br/>Formatted as `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`.<br/> Used to link objects. |
| <span id="user-content-attrtype-vector">Vector</span>      | Three Float values separated by ',' defining a 3D vector's X, Y, and Z components.<br/>Eg `1.0,2.0,3.0`|
| <span id="user-content-attrtype-filename">FileName</span>  | The case-sensitive name of a file within the archive including the extension.<br/>The filename must not contain any FAT32 or NTFS reserved characters.<br/>The extension is delimited from the base name by full stop '.' and the base name shall not be empty.<br/>It is recommended to limit filenames to the POSIX "Fully Portable Filenames" character set: [A-Z], [a-z], [0-9], the symbols '\_' (U+005F), '-' (U+002D) and a maximum of one '.' (U+002E)<br/>Eg `My-Fixture_5.gdtf`|
| <span id="user-content-attrtype-ciecolor">CIE Color</span> | CIE 1931 xyY absolute color point.<br/>Formatted as three Floats `x,y,Y`<br/>Eg `0.314303,0.328065,87.699166`|
| <span id="user-content-attrtype-ipv4">IPv4 Address</span>  | Common IPv4 Address in the format of dotted decimal notation.<br/>Eg `192.168.1.10` |
| <span id="user-content-attrtype-ipv6">IPv6 Address</span>  | Common IPv6 Address in the format of hexadecimal notation.<br/>Eg `2001:0db8:85a3:0000:0000:8a2e:0370:7344` |


