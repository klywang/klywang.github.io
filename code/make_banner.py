#!usr/bin/env python3
import argparse

import numpy as np
import matplotlib.pyplot as plt

import style

style.set_style()


parser = argparse.ArgumentParser()
parser.add_argument(
    "--k", "-k",
    help="Rotational symmetry. Default is k = 5.",
    type=int,
    default=5
)
parser.add_argument(
    "--x", "-x",
    help="Image dimensions in x (units = px). Default is x = 250",
    type=int,
    default=2048
)
parser.add_argument(
    "--y", "-y",
    help="Image dimensions in y (units = px). Default is y = 250",
    type=int,
    default=1024
)
parser.add_argument(
    "--n_repeat", "-n",
    help="How many cycles to plot. Default is n = 64.",
    type=int,
    default=64
)
parser.add_argument(
    "--cmap", "-c",
    help="Colormap. Default is twilight.",
    type=str,
    default="twilight"
)
args = parser.parse_args()

img_dimensions = np.array([args.x, args.y])
aspect = np.array([1., img_dimensions[1] / img_dimensions[0]])
center = [dim // 2 for dim in img_dimensions]

xy = np.r_[np.mgrid[
    -center[0]:center[0], -center[1]:center[1]
]].reshape(2, -1) * 2  * args.n_repeat * aspect[:, np.newaxis] / img_dimensions[:, np.newaxis]

grating = np.zeros(img_dimensions)

for n in range(args.k):
    angle = n * 2 * np.pi / args.k
    rotation = np.array([
        [np.cos(angle), -np.sin(angle)],
        # [np.sin(angle), np.cos(angle)]
    ])
    _grating = np.cos(rotation @ xy)
    # _grating = np.sum(_grating, axis=0)

    grating += _grating.reshape(*img_dimensions) 

grating /= args.k

plt.imsave("../assets/images/banner.png", grating.T, cmap=args.cmap)
