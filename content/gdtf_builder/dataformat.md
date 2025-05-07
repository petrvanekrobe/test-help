---
title : "Data Format"
description: ""
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 20
---

A GDTF file is a ZIP archive without compression which has the file extension \*.gdtf.

 {{% image_inline src="../media/window_zip_file_v1-0.PNG" alt="" %}} 

_GDTF file_

A GDTF file consists of an XML file which contains the description and several resource files such as 3D model files and gobo images.

 {{% image_inline src="../media/window_xml_emitters_v1-0.PNG" alt="" %}} 

_XML file_

The ZIP archive contains a description.xml file and resource files. Some of the resource files are located in a folder structure. A characteristic GDTF file looks like this:

*   ./description.xml
*   ./thumbnail.png
*   ./thumbnail.svg
*   ./wheels/gobo1.png
*   ./wheels/gobo2.png
*   ./models/3ds/base.3ds
*   ./models/3ds/yoke.3ds
*   ./models/svg/base.svg
*   ./models/svg/yoke.svg

The GDTF file can be unzipped after changing the file extension to \*.zip to inspect its content.
