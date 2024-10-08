import os
import cv2

def initialize_face_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Point application to app root directory
    root_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '.'))
    prototxt_path = os.path.join(
        root_dir, 'resources', 'models', 'facedetection', 'deploy.prototxt'
    )
    model_path = os.path.join(
        root_dir, 'resources', 'models', 'facedetection', 'res10_300x300_ssd_iter_140000.caffemodel'
    )

    print(f"Attempting to load prototxt from: {prototxt_path}")
    print(f"Attempting to load model from: {model_path}")

    if not os.path.exists(prototxt_path):
        raise FileNotFoundError(f"Prototxt file not found at {prototxt_path}")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    face_net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    print("Face detection model loaded successfully.")
    return face_net

# Additional model initializations can be added here in the future