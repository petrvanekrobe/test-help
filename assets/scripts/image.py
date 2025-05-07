#:'<,'>! python image.py
# converts standalone image to a shortcode
# ![](../../img/Icon_Multiple_Download.png)
# superseded by convert.py

import sys
import re

data = sys.stdin.readlines()

for l in data:
    line = l.rstrip()
    image_pattern = r"\!\[(.*)\]\((.*)\)"
    result = re.findall(image_pattern, line)[0]
    title, image = (result + (None,))[:2]
    if not image:
        image = title
        title = ""

    new_line = f'{{{{% figure src="{image.replace("/img/", "/media/")}" caption="{title}" %}}}}'
    print(new_line)
