import os
import random
import hashlib
import shutil
from tqdm import tqdm

# Function to hash filenames uniquely using class name
def hash_filename(filename, class_name):
    return hashlib.sha256((class_name + filename).encode()).hexdigest()[:10]  # Short hash for practicality

# Organizing dataset structure as train/valid/test -> images/labels
def separate_and_split_with_structure(source_dir, base_dest, split_ratios=(0.7, 0.2, 0.1)):
    for split in ['train', 'valid', 'test']:
        os.makedirs(os.path.join(base_dest, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(base_dest, split, 'labels'), exist_ok=True)

    for class_dir in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_dir)
        if os.path.isdir(class_path):
            files = [f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
            
            # Shuffle and split files
            random.shuffle(files)
            train_split = int(len(files) * split_ratios[0])
            valid_split = int(len(files) * (split_ratios[0] + split_ratios[1]))

            train_files = files[:train_split]
            valid_files = files[train_split:valid_split]
            test_files = files[valid_split:]

            # Function to copy files with hashed names
            def copy_files(file_list, split_type):
                for file in tqdm(file_list, desc=f'Copying {split_type} files'):
                    image_path = os.path.join(class_path, file)
                    label_path = os.path.join(class_path, file.rsplit('.', 1)[0] + ".txt")  # Dynamic extension handling
                    
                    hashed_name = hash_filename(file, class_dir)  # Include class name
                    image_dest_path = os.path.join(base_dest, split_type, 'images', hashed_name + os.path.splitext(file)[1])
                    label_dest_path = os.path.join(base_dest, split_type, 'labels', hashed_name + ".txt")
                    
                    shutil.copy(image_path, image_dest_path)
                    if os.path.exists(label_path):
                        shutil.copy(label_path, label_dest_path)
                    else:
                        print(f"⚠ هشدار: لیبل برای {file} یافت نشد!")

            # Copy files for train, valid, and test
            copy_files(train_files, 'train')
            copy_files(valid_files, 'valid')
            copy_files(test_files, 'test')

# Example usage
source_directory = "/path/to/source"
base_directory = "/path/to/dataset"
separate_and_split_with_structure(source_directory, base_directory, split_ratios=(0.7, 0.2, 0.1))
