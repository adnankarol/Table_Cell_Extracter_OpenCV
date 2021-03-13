# Module to Save detected cells
import pytesseract
from PIL import Image
import cv2
import numpy as np
import os

# Function to Check if Image/Cell is Empty
def check_empty_image(finalimage):
    try:
        #im = cv2.imread(finalimage)
        image = cv2.resize(finalimage, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        retval, threshold = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

        text = pytesseract.image_to_string(threshold)
        if len(text) > 1:
            return 1
        else :
            print("Passed")
            return 0
    except:
        print("Skipped")
        return 1


def save_cell(finalboxes, bitnot, countcol, filepath):
    outer = []
    row_nr = 0
    column_nr = 0

    try:
        for i in range(len(finalboxes)):
            for j in range(len(finalboxes[i])):
                inner = ''
                if len(finalboxes[i][j]) == 0:
                    outer.append(' ')
                else:
                    for k in range(len(finalboxes[i][j])):
                        (y, x, w, h) = (finalboxes[i][j][k][0],
                                finalboxes[i][j][k][1],
                                finalboxes[i][j][k][2],
                                finalboxes[i][j][k][3])
                        finalimage = bitnot[x:x + h, y:y + w]
                        if column_nr == countcol:
                            row_nr = row_nr + 1
                            column_nr = 0

                        Folder_Path = 'results/' + filepath.split('\\')[-1].split('.')[0]
                        if not os.path.exists(Folder_Path):
                            print(' Creating Results Folder : ', Folder_Path)
                            os.makedirs(Folder_Path)
                        file_to_be_saved = Folder_Path + '/' + 'cell_' + str(row_nr) + '_' + str(column_nr) + '.png'
                        empty_status = check_empty_image(finalimage)
                        if empty_status == 1:
                            cv2.imwrite(img=finalimage, filename=file_to_be_saved)
                        column_nr = column_nr + 1
        return 1
    except:
        return -1
