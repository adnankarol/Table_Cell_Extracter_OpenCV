# Module to perform preprocessing on the image and to Check Orientation of Cells
import cv2
import pytesseract


def check_orientation(image):
    try:
        orientation_details = pytesseract.image_to_osd(image)
        angle = int(orientation_details.split("\n")[2].split(":")[-1])
        if angle == 90 :
            image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE) 
        elif angle == 180 :
            image = cv2.rotate(image, cv2.ROTATE_180) 
        return image
    except :
        return image


def preprocess_image(image):

    # Check Orientation of Image
    image = check_orientation(image)

    # thresholding the image to a binary image
    (thresh, img_bin) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # inverting the image
    img_bin = 255 - img_bin

    return (image, img_bin)
