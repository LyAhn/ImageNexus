import cv2
import numpy as np

def pixelate(image, blocks=8):
    """
    Pixelate the given image region.
    
    :param image: numpy array of the image
    :param blocks: int, number of pixels per block
    :return: pixelated image
    """
    (h, w) = image.shape[:2]
    x_steps = max(1, w // blocks)
    y_steps = max(1, h // blocks)
    for y in range(0, h, y_steps):
        for x in range(0, w, x_steps):
            roi = image[y:y + y_steps, x:x + x_steps]
            if roi.size == 0:
                continue
            color = roi.mean(axis=(0, 1)).astype(int)
            image[y:y + y_steps, x:x + x_steps, :3] = color[:3]
    return image

def draw_eye_bars(image, x, y, w, h):
    """
    Draw horizontal black bars over the eyes region of the face.
    
    :param image: numpy array of the image
    :param x, y, w, h: int, coordinates and dimensions of the face
    :return: image with eye bars drawn
    """
    # Ensure the image has an alpha channel
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    
    eye_y = y + int(h * 0.3)
    eye_h = int(h * 0.16)
    bar_w = int(w * 1.0)
    bar_x = x
    cv2.rectangle(image, (bar_x, eye_y), (bar_x + bar_w, eye_y + eye_h), (0, 0, 0, 255), -1)
    return image

def apply_gaussian_blur(image, kernel_size=(119, 119), sigma=60):
    """
    Apply Gaussian blur to the image.
    
    :param image: numpy array of the image
    :param kernel_size: tuple, size of the Gaussian kernel
    :param sigma: int, standard deviation in X and Y directions
    :return: blurred image
    """
    return cv2.GaussianBlur(image, kernel_size, sigma)