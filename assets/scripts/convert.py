# usage in vim: select text and run:
#:'<,'>! python convert.py
# converts images and links from markdown to markdown/hugo shortcodes
# handles inline images:
# Text text text ![](../../img/Icon_Multiple_Download.png) text text
# standalone images:
# ![](../../img/Icon_Multiple_Download.png)
# cleans-up links:
# [Favorite files topic](key_favorite_files.html)


import sys
import re

data = sys.stdin.readlines()

for l in data:
    line = l.rstrip().replace("(key_", "(").replace(".html)", ")")
    image_pattern = r"(.*).\!\[\]\((.*)\)(.*)"
    image_pattern = r"\!\[(.*)\]\((.*)\)"
    image_pattern = r"(.*)?.?\!\[\]\((.*)\)(.*)?"
    result = re.findall(image_pattern, line)
    if not result:
        print(line)
        continue
    findings = result[0]
    start, image, end = re.findall(image_pattern, line)[0]
    new_line = f'{start} {{{{% image_inline src="{image.replace("/img/", "/media/")}" alt="" %}}}} {end}'

    print(new_line)
