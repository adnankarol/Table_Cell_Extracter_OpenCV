# Module to Handle Exception Cases
import cv2
import numpy as np


def exception_handler(img, img_bin):

    # Length(width) of kernel as 100th of total width
    kernel_len = np.array(img).shape[1] // 20
    kernel_len_2 = np.array(img).shape[0] // 11

    # Defining a vertical kernel to detect all vertical lines of image
    ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len_2))

    # Defining a horizontal kernel to detect all horizontal lines of image
    hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))

    # A kernel of 2x2
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    # Use vertical kernel to detect and save the vertical lines in a jpg
    image_1 = cv2.erode(img_bin, ver_kernel, iterations=5)
    vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=5)

    # Use horizontal kernel to detect and save the horizontal lines in a jpg
    image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
    horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)

    # Combine horizontal and vertical lines in a new third image, with both having same weight.
    img_vh = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)

    # Eroding and thesholding the image
    img_vh = cv2.erode(~img_vh, kernel, iterations=2)
    (thresh, img_vh) = cv2.threshold(img_vh, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)   
    cv2.imshow("f",  cv2.resize(img_vh, (0,0), fx=0.5, fy=0.5) )
    cv2.waitKey(0)
    return (thresh, img_vh)