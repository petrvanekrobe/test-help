#:'<,'>! python md_to_html.py
# converts tables with images into html tables with images better scaled
# used mostly on mvr-xchange image tables

import sys
import re

data = sys.stdin.readlines()
t1 = t2 = i1 = i2 = ""
regex = r"\((.*)\)"
short = False

for l in data:
    line = l.rstrip()
    if "|---|" in line:
        continue
    s = line.split("|")
    if len(s) == 3:  # single image
        short = True
        _, tx1, _ = line.split("|")
        if "png" in tx1:
            i1 = re.findall(regex, tx1)[0]
        else:
            t1 = tx1
    else:
        _, tx1, tx2, _ = line.split("|")
        if "png" in tx1:
            i1 = re.findall(regex, tx1)[0]
            i2 = re.findall(regex, tx2)[0]
        else:
            t1, t2 = tx1, tx2

if short:
    print(
        f"""
<div class="container">
 <div class="row">
  <div class="col-sm border border-dark">
    <div class="text-center border-bottom border-dark font-weight-bold">
        {t1}
    </div>
    <div class="text-center">
        <a href="{i1}"><img src="{i1}" width="270px" /></a>
   </div>
   </div>
  </div>
</div>"""
    )
else:
    print(
        f"""
<div class="container">
 <div class="row">
  <div class="col-sm border border-dark">
    <div class="text-center border-bottom border-dark font-weight-bold">
        {t1}
    </div>
    <div class="text-center">
        <a href="{i1}"><img src="{i1}" width="270px" /></a>
   </div>
   </div>
  <div class="col-sm border border-dark">
    <div class="text-center border-bottom border-dark font-weight-bold">
        {t2}
    </div>
    <div class="text-center">
        <a href="{i2}"><img src="{i2}" width="270px" /></a>
   </div>
   </div>
  </div>
</div>"""
    )
