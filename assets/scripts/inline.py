#:'<,'>! inline.py
# converts an inline-in-text image to a shortcode
# superdeded by convert.py
# Text text text ![](../../img/Icon_Multiple_Download.png) text text

import sys
import re

data = sys.stdin.readlines()

for l in data:
    line = l.rstrip()
    image_pattern = r"(.*).\!\[\]\((.*)\)(.*)"
    start, image, end = re.findall(image_pattern, line)[0]
    new_line = f'{start} {{{{% image_inline src="{image.replace("/img/", "/media/")}" alt="" %}}}} {end}'
    print(new_line)
