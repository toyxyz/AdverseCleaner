import os
import numpy as np
import cv2
from cv2.ximgproc import guidedFilter

# Function to process a single image
def process_image(input_path, output_path):
    img = cv2.imread(input_path).astype(np.float32)
    y = img.copy()

    for _ in range(64):
        y = cv2.bilateralFilter(y, 5, 8, 8)

    for _ in range(4):
        y = guidedFilter(img, y, 4, 16)

    cv2.imwrite(output_path, y.clip(0, 255).astype(np.uint8))

# Path to the folder containing input images
input_folder = 'input'

# Path to the folder where processed images will be saved
output_folder = 'out'

# List all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Process each image
for image_file in image_files:
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)
    process_image(input_path, output_path)
