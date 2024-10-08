import cv2
import numpy as np

def save_image(image, file_path):
    """
    Save an image to a file.
    
    :param image: numpy array of the image
    :param file_path: str, path where the image should be saved
    :return: bool, True if successful, False otherwise
    """
    try:
        # Ensure the image is in BGRA format
        if image.shape[2] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        # Save the image
        cv2.imwrite(file_path, image)
        return True
    except Exception as e:
        print(f"Error saving image: {str(e)}")
        return False

def load_image(file_path):
    """
    Load an image from a file.
    
    :param file_path: str, path of the image to load
    :return: numpy array of the loaded image, or None if loading fails
    """
    try:
        image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise ValueError("Failed to load image")
        # Ensure the image has an alpha channel
        if image.shape[2] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
        return image
    except Exception as e:
        print(f"Error loading image: {str(e)}")
        return None