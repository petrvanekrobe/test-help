---
title : "Preparing PNG assets"
description: "Rasterized PNG images are used in GDTF in several places - as a device thumbnail or as a MediaFileName in slots for gobo wheels and animation wheels."
lead: ""
date: 2025-05-02T09:04:34+0200
lastmod: 2025-05-02T09:04:28+0200
draft: false
images: []
weight: 70
---

## Preparing PNG assets

Rasterized PNG images are used in GDTF in several places - as a device thumbnail or as a MediaFileName in slots for gobo wheels and animation wheels. While the GDTF specified definition of a device thumbnail is quite simple (_a png file to provide the rasterized picture with maximum resolution of picture 1024 x 1024_), definition for a gobo slot image is more involved:

_Gobo images shall be in PNG format with an alpha channel. Indexed, Greyscale and Alpha, 8-bit RGB and Alpha, or 16-bit RGB and Alpha are accepted pixel formats. The Background shall be fully transparent and should be considered to be the equivalent of a gobo holder. The Image region shall be fully opaque aside from anti-aliasing and shall be as large as possible. The Background region, the equivalent of gobo holder, is defined by full transparency (Alpha 0). In the Image region, Pure Black (RGB 0,0,0) is opaque (2), and Pure White (RGB 255,255,255) is transparent (GDTF). Colored gobos (3) shall use an RGB approximation. The RGB approximation shall be calculated on the basis of Pure White being the CCT of the fixture light source and the ICC color profile embedded within the PNG. The default shall be sRGB._

![image.png.c884f4d2aa74478dab36559157d0d940.png](../media/png_assets_01.png)

_\- Maximum resolution of picture: 1024x1024;
\- Recommended resolution of gobo: 256x256;
\- Recommended resolution of animation wheel: 256x256_

So for thumbnail images, one can use pretty much any png image with the given dimensions. Ideally, the image should be a square, to make the result more predictable when used in applications.

This is the default image provided by the builder:

![image.png.f3d99fa1877fc0286352e049d67bbb18.png](../media/png_assets_02.png)

What we like to do, however, is to ensure that the image is actually trimmed on a transparent background, so it can better fit into any UI (checker board indicating the transparency):

![image.png.6065458bd201a0844db4698a0bed03e6.png](../media/png_assets_03.png)

With the transparency:

![image.png.c99cc56594b5824d56aa0f0f87aded53.png](../media/png_assets_04.png)

For wheel slot images, you have ensure that the non-transparent (opaque) and transparent (white, colored) portions are correctly defined and that transitions between them are also correct.

Here is a 256x256 example:

![image.png.9af5aac506c0a7b6984941c145d6a964.png](../media/png_assets_05.png)

Critical parts are the transitions on the edge of the gobo image. On the edge between alpha and color, you should have no extra color (due to antialiasing), it must contain just the alpha (transparency):

![image.png.04df5880ddef884330465314814a412f.png](../media/png_assets_06.png)

On the edge between white and black, you need to have only colors and no transparency:

![image.png.343e5ca513c25cd245a034c0e1059c20.png](../media/png_assets_07.png)

Same rules apply for the animation wheel, here is an example:

![image.png.624b27e106b0b18f610338710acbc605.png](../media/png_assets_08.png)

Now you have basic understanding of how PNG images need to be prepared for GDTF files.

Hope this helps
