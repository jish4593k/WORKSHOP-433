import sys
import os
from PIL import Image
import torch
from torchvision import transforms

def jpeg_to_png(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            img = Image.open(image_path)

           
            transform = transforms.Compose([transforms.RGBTransform()])
            img_rgb = transform(img)

            
            filtered = os.path.splitext(filename)[0]
            img_rgb.save(os.path.join(output_folder, f'{filtered}.png'), 'PNG')

if __name__ == "__main__":
    image_folder_path = sys.argv[1]
    output_folder_path = sys.argv[2]

    jpeg_to_png(image_folder_path, output_folder_path)

    print("Conversion from JPEG to PNG complete.")
