from glob import glob
from tqdm import tqdm
import os

import PIL
from PIL import Image, ImageOps


MAX_SIZE = (400, 400)


artwork_md = """---
title: "Artwork"
permalink: /artwork/
author_profile: true
gallery:"""


for im_path in tqdm(glob("../assets/images/artwork/full/*")):
    im_path = os.path.abspath(im_path)
    path_head = im_path.split("/")[:-2]
    path_head = '/'.join(path_head)
    image_name = im_path.split("/")[-1]
    try:
        image = Image.open(im_path)
        image.thumbnail(MAX_SIZE)
        image.save(
            f"{path_head}/thumbnails/{image_name}"
        )
        artwork_md += f"\n  - url: /assets/images/artwork/full/{image_name}"
        artwork_md += f"\n    image_path: /assets/images/artwork/thumbnails/{image_name}"
    except PIL.UnidentifiedImageError:
        print(image_name)

artwork_md += """

---

{% include gallery %}"""


with open("../_pages/artwork.md", "w") as f:
    for line in artwork_md:
        f.write(line)
