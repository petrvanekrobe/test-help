---
title: "MVR Spec"
description: "File Format Definition"
lead: "File Format Definition"
date: 2023-11-26T14:00:06+0100
lastmod: 2023-11-26T14:00:09+0100
draft: false
images: []
weight: 20
toc: true
---

This document describes the [DIN SPEC 15801:2023-12](https://www.beuth.de/en/technical-rule/din-spec-15801/373968511) also known as MVR Version 1.6.

{{% badge style="primary" title="MVR Version" %}}1.6{{% /badge %}} {{% badge style="primary" title="DIN SPEC" %}}15801:2023-12{{% /badge %}}

## Introduction

MVR - My Virtual Rig - specified in this DIN SPEC will unify the information
exchange between different applications within the entertainment industry.
Based on GDTF, as specified in DIN SPEC 15800, MVR allows the exchange of
scenic and environmental information and complete show setups as planning
status. Furthermore the MVR file format allows programs to share data and
geometry for a scene. A scene is a set of parametric objects such as fixtures,
trusses, video screens, and other objects that are used secifically in the
entertainment industry.

Typical workflow
1.  Program A saves an MVR file containing a scene;
2.  Program B imports this file;
3.  Program B changes some parametric data in the scene;
4.  Program B saves an MVR containing the scene;
5.  Program A imports this file and applies the changes to the existing objects.


## Scope

This document specifies "My Virtual Rig" (MVR), which is designed to provide a
unified way of listing and describing the hierarchical and logical structure
based on DIN SPEC 15800 "General Device Type Format" (GDTF) - and further
environmental information of a show setup in the entertainment business. It
will be used as a foundation for the exchange of extended device and
environmental data between lighting consoles, CAD and 3D-pre-visualization
applications. The purpose of an MVR-file is to reflect the real-world physical
components of a show setup and the logical patch information of the devices
while maintaining the kinematic chain.

## Normative references

The following documents are referred to in the text in such a way that some or all of their content constitutes
requirements of this document. For dated references, only the edition cited applies. For undated references,
the latest edition of the referenced document (including any amendments) applies.

- [DIN SPEC 15800:2022-02, Entertainment Technology— General Device Type Format (GDTF)](https://www.beuth.de/en/technical-rule/din-spec-15800/349717520)
- [ISO/IEC 21778:2017, Information technology— The JSON data interchange syntax](https://standards.iso.org/ittf/PubliclyAvailableStandards/c071616_ISO_IEC_21778_2017.zip)
- [Extensible Markup Language (XML) 1.0](https://www.w3.org/TR/2008/REC-xml-20081126/)
- [PKWARE 6.3.3](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)
- [Domain Names— Implementation and Specification](https://www.ietf.org/rfc/rfc1035.txt)
- [RFC3629, UTF-8, a transformation format of ISO 10646](https://datatracker.ietf.org/doc/html/rfc3629)
- [RFC4122, A Universally Unique IDentifier (UUID) URN Namespace](https://www.rfc-editor.org/rfc/rfc4122)
- [RFC6455, The WebSocket Protocol](https://www.ietf.org/rfc/rfc6455.txt)
- [RFC6762, Multicast DNS](https://www.ietf.org/rfc/rfc6762.txt)
- [RFC6763, DNS-Based Service Discovery](https://www.ietf.org/rfc/rfc6763.txt)

## Terms and definitions

For the purposes of this document, the following terms and definitions apply.
DIN and DKE maintain terminological databases for use in standardization at the following addresses:

  - DIN-TERMinologieportal: available at
    <https://www.din.de/go/din-term>
  - DKE-IEV: available at <http://www.dke.de/DKE-IEV>


### My Virtual Rig, MVR
descriptive name of the specification

### MVR-xchange
protocol to share MVR files over the network

### MVR-xchange client
application that participates in the MVR-xchange

### MVR-xchange group
group of MVR-xchange clients that work on the same project and communicate together

### TCP Mode
MVR-xchange communication via TCP packages and discovery via mDNS

### WebSocket Mode
MVR-xchange communication via WebSockets and discovery via DNS



## MVR Definitions

### General

MVR consists of two parts to enable any application to exchange GDTF but also general information in the same
common format. Firstly the MVR file format as described in the following section. Secondly a MVR communication format to simplify exchange between applications.


### File Format Definition

To describe all information within one file, a zip file according to PKWARE 6.3.3 with the extension `*.mvr` is used. The archive shall contain one root file named `GeneralSceneDescription.xml`, along with all other resource files referenced via this Root File. The root file `GeneralSceneDescription.xml` is mandatory inside the archive to be a valid MVR file.

UTF-8 according to RFC3629 has to be used to encode the XML file. Each XML file internally consists of XML nodes. Each XML node could have XML attributes and XML node children. Each XML attribute has a value. If a XML attribute is not specified, the default value of this XML attribute will be used. If the XML attribute value is
specified as a string, the format of the string will depend on the XML attribute type.

- The archive shall not use encryption or password protection.
- All files referenced by the Root File shall be placed at the root level. They shall not be placed in folders.
- Files shall be placed using either STORE (uncompressed) or DEFLATE compression. No other compression algorithms are supported.
- Files may be placed into the archive in any order.
- A `Universal.gdtt` GDTF template file with a `.gdtt` extension can be added to define Gobos, Emitters, Filter and such for referencing.
- Filenames within the archive must not differ only by case. Eg it is prohibited to have the files `GEO1.glb` and `geo1.glb` within the same archive.
- The file name of the ZIP archive can be chosen freely.

All objects used have a persistent unique ID to track changes between the different applications. If there are no changes to the original GDTF file it is mandatory to keep it in the MVR during export. If there are changes to the GDTF file it is mandatory to add a revision to the GDTF file in order to reflect it.

Only user-intended modifications of any part of the MVR file shall be processed. This is particular important if applications in the workflow do not need or accept all data of the MVR file. Such behaviour guarantees that all later steps in the workflow have access to the original intended data.

- EXAMPLE An example of a typical MVR archive is shown below:

```
GeneralSceneDescription.xml
Custom@Fixture1.gdtf
Custom@Fixture2.gdtf
geo1.3ds
geo1.glb
Textr12.png
Universal.gdtt
```
