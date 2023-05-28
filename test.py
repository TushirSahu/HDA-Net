import os
import shutil
def move_images_to_data_directory(txt_file_path, source_directory, destination_directory):
    with open(txt_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            image_name, label = line.split()
            image_path = os.path.join(source_directory, image_name)
            dest_directory = os.path.join(destination_directory, label)
            
           
            if not os.path.exists(dest_directory):
                os.makedirs(dest_directory)

            
            if os.path.exists(image_path):
                new_image_path = os.path.join(dest_directory, image_name)
                shutil.move(image_path, new_image_path)
                print(f"Moved {image_name} to {dest_directory}")
            else:
                continue


# Usage example
txt_file = "train.txt"
source_directory = "DR_grading"
destination_directory = "train"

move_images_to_data_directory(txt_file, source_directory, destination_directory)
