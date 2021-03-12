# Import Dependencies

import os
import glob
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import Local Modules

from utils.preprocess_image import preprocess_image
from utils.detect_lines import detect_lines
from utils.save_cell import save_cell
from utils.detect_cells import detect_cells


def TableAnalysis(filepath):

    # Read The Image
    image = cv2.imread(filepath, 0)

    # PreProcess The Image
    (image, image_bin) = preprocess_image(image)

    # Detect Lines on an Image
    (thresh, image_vh) = detect_lines(image, image_bin)

    # Detect Cell on Image
    (finalboxes, bitnot, countcol) = detect_cells(image, image_vh)

    # Save every Cell
    status = save_cell(finalboxes, bitnot, countcol, filepath)
    if status != 1:
        print("Possible Error! Kindly check Image.")


if __name__ == '__main__':

    for filepath in glob.glob(os.path.join('tables/*.png')):

        try:

            TableAnalysis(filepath)
        except :
            print("Image Skipped : ", filepath)
