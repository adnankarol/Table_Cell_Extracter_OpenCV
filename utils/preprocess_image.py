# Module to perform preprocessing on the image
import cv2


def preprocess_image(image):

    # thresholding the image to a binary image
    (thresh, img_bin) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # inverting the image
    img_bin = 255 - img_bin

    return (image, img_bin)
