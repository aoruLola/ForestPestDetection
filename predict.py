import os
import cv2
# import torch
from ultralytics import YOLO

# 加载模型
model = YOLO("./trained_model/weights/best.pt")

input_folder = './input_images'
output_folder = './output_images'
os.makedirs(output_folder, exist_ok=True)

for image_name in os.listdir(input_folder):
    if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):

        image_path = os.path.join(input_folder, image_name)
        image = cv2.imread(image_path)

        results = model(image)

        if len(results[0].boxes) == 0:
            print(f"No objects detected in: {image_name}")
            continue

        annotated_image = results[0].plot()

        output_path = os.path.join(output_folder, image_name)
        cv2.imwrite(output_path, annotated_image)

        print(f"Processed and saved: {output_path}")

print("All images have been processed. XD")
