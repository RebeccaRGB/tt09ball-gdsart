# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2024 Uri Shaked

import gdspy
import sys
from PIL import Image

PNG_NAME = "high_voltage.png"
CELL_NAME = "high_voltage_logo"
GDS_NAME = "high_voltage.gds"

BOUNDARY_LAYERS = [
    (235, 4), # prBndry, boundary
    (62, 24), # cmm1, waffle-drop
    (105, 52), # cmm2, waffle-drop
    (107, 24), # cmm3, waffle-drop
    (112, 4), # cmm4, waffle-drop
    (117, 4), # cmm5, waffle-drop
]
PIXEL_LAYERS = [
    (68, 20), # met1, drawing
    (69, 20), # met2, drawing
    # (70, 20), # met3, drawing
    # (71, 20), # met4, drawing
]
PIXEL_SIZE = 0.28 # um

# Process arguments
args = sys.argv[1:]
while args:
    arg = args.pop(0)
    if arg == '-u' and args:
        PIXEL_SIZE = float(args.pop(0))
    elif arg == '-i' and args:
        PNG_NAME = args.pop(0)
    elif arg == '-c' and args:
        CELL_NAME = args.pop(0)
    elif arg == '-o' and args:
        GDS_NAME = args.pop(0)
    else:
        print('Unknown argument: %s' % arg)
        exit(1)

# Open the image
img = Image.open(PNG_NAME)

# Convert the image to grayscale
img = img.convert("L")

layout = gdspy.Cell(CELL_NAME)
for layer, datatype in BOUNDARY_LAYERS:
    layout.add(
        gdspy.Rectangle((0, 0),
                        (img.width * PIXEL_SIZE, img.height * PIXEL_SIZE),
                        layer=layer, datatype=datatype))
for layer, datatype in PIXEL_LAYERS:
    for y in range(img.height):
        for x in range(img.width):
            color = img.getpixel((x, y))
            if color < 128:
                # Adjust y-coordinate to flip the image vertically
                flipped_y = img.height - y - 1
                layout.add(
                    gdspy.Rectangle((x * PIXEL_SIZE, flipped_y * PIXEL_SIZE),
                                    ((x + 1) * PIXEL_SIZE, (flipped_y + 1) * PIXEL_SIZE),
                                    layer=layer, datatype=datatype))

# Save the layout to a file
gdspy.write_gds(GDS_NAME)
