from glob import glob
from tqdm import tqdm
import os

import PIL
from PIL import Image, ImageOps


THUMB_MAX_SIZE = (256, 256)
FULL_MAX_SIZE = (2048, 1024)


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
    image_name, ext = image_name.split(".")
    try:
        # Make thumbnail
        image = Image.open(im_path)
        h, w = image.size
        crop_dim = min(h, w) / 2
        center = [h / 2, w / 2]
        image = image.crop((
            center[0] - crop_dim,  # left
            center[1] - crop_dim,  # top
            center[0] + crop_dim,  # right
            center[1] + crop_dim,  # bottom
        ))
        image.thumbnail(THUMB_MAX_SIZE)
        image.save(
            f"{path_head}/thumbnails/{image_name}-th.{ext}"
        )
        
        # Downsample for web
        s3_url = f"https://klywangwebsiteartworkfull.s3.us-east-2.amazonaws.com/downsampled/{image_name}-down.{ext}"
        image = Image.open(im_path)
        image.thumbnail(FULL_MAX_SIZE)
        image.save(
            f"{path_head}/downsampled/{image_name}-down.{ext}"
        )
        artwork_md += f"\n  - url: {s3_url}"
        artwork_md += f"\n    image_path: /assets/images/artwork/thumbnails/{image_name}-th.{ext}"
    except PIL.UnidentifiedImageError:
        print(image_name)

artwork_md += """

---

{% include gallery %}"""


with open("../_pages/artwork.md", "w") as f:
    for line in artwork_md:
        f.write(line)
