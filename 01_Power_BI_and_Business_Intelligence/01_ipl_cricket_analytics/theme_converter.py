import base64
import json
import os

# This script creates a valid Power BI Report Theme JSON
current_folder = os.path.dirname(os.path.abspath(__file__))
files_in_folder = os.listdir(current_folder)

# Find the first PNG file
target_image = next((f for f in files_in_folder if f.lower().endswith(".png")), None)

if target_image:
    print(f"Found image: {target_image}")
    try:
        image_path = os.path.join(current_folder, target_image)
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        # This is the exact schema Power BI expects
        theme_json = {
            "name": "Cricket Dashboard Theme",
            "visualStyles": {
                "page": {
                    "*": {
                        "background": [
                            {
                                "image": {
                                    "name": "Background",
                                    "scaling": "Fit",
                                    "url": "data:image/png;base64," + encoded_string
                                },
                                "transparency": 0
                            }
                        ]
                    }
                }
            }
        }

        output_path = os.path.join(current_folder, "cricket_theme.json")
        with open(output_path, "w") as json_file:
            json.dump(theme_json, json_file, indent=2)

        print("-" * 30)
        print("SUCCESS! Valid Theme Created.")
        print(f"File: cricket_theme.json")
        print("-" * 30)
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("ERROR: No PNG image found in the folder.")