import os
import sys

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # Running in a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in normal Python environment
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    full_path = os.path.normpath(os.path.join(base_path, relative_path))
    return full_path