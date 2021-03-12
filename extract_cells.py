# Import Dependencies

import os
import glob
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List

# Import Local Modules

from utils.preprocess_image import preprocess_image
from utils.detect_lines import detect_lines
from utils.save_cell import save_cell
from utils.detect_cells import detect_cells

        
class TableAnalysis:
    global config
    config = {
        "flag": 0,
    }

    def process(self, filepath):

        # Read The Image
        image = cv2.imread(filepath, config["flag"])

        # PreProcess The Image
        (image, image_bin) = preprocess_image(image)

        # Detect Lines on an Image
        (thresh, image_vh) = detect_lines(image, image_bin)

        # Detect Cell on Image
        (finalboxes, bitnot, countcol) = detect_cells(image, image_vh)
        
        return finalboxes, bitnot, countcol

    
    def write_results(self,finalboxes, bitnot, countcol, filepath):
        
        status = save_cell(finalboxes, bitnot, countcol, filepath)
        if status != 1:
            return -1
        else :
            return 1
            
              
if __name__ == "__main__":
    table_analysis = TableAnalysis()
    
    for filepath in glob.glob(os.path.join("tables/*.png")):
        try:
            finalboxes, bitnot, countcol= table_analysis.process(filepath)
            status = table_analysis.write_results(finalboxes, bitnot, countcol, filepath)
            if status != 1 :
                print("Possible Error! Kindly check Image.")
            else:
                    print("Image processes Succesfully")
        except :
            print("Image Skipped : ", filepath)

