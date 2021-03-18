# Import Dependencies

import os
import glob
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shutil
import yaml
import sys

# Import Local Modules

from utils.preprocess_image import preprocess_image
from utils.detect_lines import detect_lines
from utils.save_cell import save_cell


# Define the Path to the Config File.
path_to_config_file = "config.yaml"


""" 
method name : config_params
method description : To Load the Configuration Paramaters.
input args : 
    None
return :
    None

"""
def config_params():
    global flag, path_to_process
    global lang, config_tesseract, threshold_length_text
    global no_columns, special_words
    global json_save

    with open(path_to_config_file, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    
    flag = cfg["preprocess_paramaters"]["flag"]
    path_to_process = cfg["paths"]["path_to_process"]
    lang = cfg["pytesseract"]["lang"]
    config_tesseract = cfg["pytesseract"]["config"]
    threshold_length_text = cfg["pytesseract"]["threshold_length_text"]
    delete_results = cfg["paths"]["delete_results"]
    no_columns = cfg["table_dimensions"]["no_columns"]
    json_save = cfg["json_saver"]["json_save"]
    special_words = cfg["special"]["special_words"]

    try:
        if delete_results.lower() == "yes":
            shutil.rmtree('results/', ignore_errors=True)
            print("Existing Results Folder Deleted!")
    except:
        print("No Existing Results Folder!")
  

class TableAnalysis:

    """ 
    method name : purpose
    method description : To Preprocess and perform all operations on the input image.
    input args : 
        filepath : Path to each input image
    return :
        finalboxes : Cordinates of extracted boxes/cells.
        bitnot : Detected Image with only column and row lines.
        countcol : Number of Columns in the Image Table.
        count_rows :Number of Rows in the Image Table.

    """
    def process(self, filepath):

        # Read The Image
        image = cv2.imread(filepath, flag)

        # PreProcess The Image
        (image, image_bin) = preprocess_image(image)

        # Detect Lines and Cells on an Image
        (finalboxes, bitnot, countcol, count_rows, cell_detector_status) = detect_lines(image, image_bin, no_columns)    
        
        return finalboxes, bitnot, countcol, count_rows, cell_detector_status


    """ 
    method name : write_results
    method description : To Process the extracted cells and store them if required.
    input args : 
        Output args from Previous Function purpose.
    return :
        status : Status of Each Image Cell Extraction : -1 in case of Error.

    """
    def write_results(self,finalboxes, bitnot, countcol, count_rows, filepath):
        
        status = save_cell(finalboxes, bitnot, countcol, count_rows, filepath, lang, config_tesseract, threshold_length_text, json_save, special_words)
        if status != 1:
            return -1
        else :
            return 1


""" 
method name : main
method description : Driver Function for the Program.
input args : 
    None
return :
    None

"""
def main():

    # Check if Config variables are loaded
    try :
        path_to_process
    except:
        print("Config Function is to be called before Class Table Analysis")
        print("System Exit...")
        sys.exit(1)

    table_analysis = TableAnalysis()
    
    for filepath in glob.glob(os.path.join(path_to_process)):
        try:
            if filepath.split("\\")[-1].split(".")[0] == str(27):
                finalboxes, bitnot, countcol, count_rows, cell_detector_status = table_analysis.process(filepath)
                if cell_detector_status == -1:
                    print("Image Dropped due to Dimension Error ", filepath.split("\\")[-1])
                else:
                    status = table_analysis.write_results(finalboxes, bitnot, countcol, count_rows, filepath)
                    if status != 1:
                        print("Possible Error! Kindly check Image.")
                    else:
                        print("Image Processed Succesfully")
        except :
            print("Image Skipped : ", filepath)         


if __name__ == "__main__":
    config_params()
    main()
