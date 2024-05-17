import json
import os
from PIL import Image

def create_ai_camera_dataset(dataset.json):
    dataset = {
        "info": {
            "description": "Example Dataset",
            "version": "1.0",
            "year": 2024,
            "contributor": "Muhammed Adnan",
            "date_created": "2024-05-17"
        },
        "images": [],
        "annotations": [],
        "categories": [
            {
                "id": 1,
                "name": "object",
                "supercategory": "none"
            }
        ]
    }

    image_id = 1
    annotation_id = 1

    for image_file in os.listdir(image_folder):
        if image_file.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, image_file)
            with Image.open(image_path) as img:
                width, height = img.size

            image_info = {
                "id": image_id,
                "file_name": image_file,
                "width": width,
                "height": height
            }
            dataset["images"].append(image_info)

            # Example annotation - you need to replace this with your actual annotation logic
            annotation_info = {
                "id": annotation_id,
                "image_id": image_id,
                "category_id": 1,
                "bbox": [50, 50, 150, 150],
                "area": 22500,
                "iscrowd": 0
            }
            dataset["annotations"].append(annotation_info)

            image_id += 1
            annotation_id += 1

    with open('ai_camera_dataset.json', 'w') as file:
        json.dump(dataset, file, indent=4)

if __name__ == "__main__":
    image_folder = 'path/to/your/image/folder'
    create_ai_camera_dataset(image_folder)
    print("AI camera dataset created and saved to 'ai_camera_dataset.json'")


