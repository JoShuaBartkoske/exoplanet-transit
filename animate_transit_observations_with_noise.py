'''
Animate Transit Observations with Noise
Author: Joshua Thomas Bartkoske
DoC: August 8, 2025
Based on other work done for animating all sky camera snapshots
'''


import os
import imageio
import numpy as np
from PIL import Image
from PIL import ImageDraw

def create_animation(image_folder, output_filename="animation.gif", frame_duration=0.1):
    """
    Creates an animation (GIF) from a sequence of images in a folder.

    Args:
        image_folder (str): Path to the folder containing the images.
        output_filename (str, optional): Name of the output GIF file. Defaults to "animation.gif".
        frame_duration (float, optional): Duration of each frame in seconds. Defaults to 0.1.
    """
    images = []
    filenames = sorted((f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))))

    for i,filename in enumerate(filenames):

        filepath = os.path.join(image_folder, filename)
        try:
            image = imageio.imread(filepath)
            images.append(image)
        except Exception as e:
            print(f"Error reading {filename}: {e}")
    
    if images:
        if ".mp4" in output_filename:
            imageio.mimsave(output_filename, images, fps=int(1/frame_duration))
        else:
            imageio.mimsave(output_filename, images, duration=frame_duration)
        print(f"Animation saved as {output_filename}")
    else:
        print("No valid images found in the folder.")
if __name__ == "__main__":
    folder_path = "/Users/joshuabartkoske/Desktop/Exoplanets/screenshots_transit_noise_varying"

    create_animation(folder_path, output_filename="TOI2109-transit-noise-varying.mp4", frame_duration=0.2)

