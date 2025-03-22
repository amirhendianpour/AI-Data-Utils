import os
import shutil
from random import seed, shuffle

# Set the seed for reproducibility
seed(1)

# Define your dataset directory and the output directory for the split dataset
dataset_dir = "D:\data_orange\input"
output_dir = "D:\data_orange\out"

# Ratios for splitting
train_ratio = 0.7
valid_ratio = 0.2
# Test ratio is calculated as the remaining percentage
test_ratio = 0.1

# Create the output directories if they don't exist
for split in ['train', 'valid', 'test']:
    split_dir = os.path.join(output_dir, split)
    if not os.path.exists(split_dir):
        os.makedirs(split_dir)

# Function to split data
def split_data(class_name):
    # Create subdirectories for each class in train, valid, and test directories
    for split in ['train', 'valid', 'test']:
        class_dir = os.path.join(output_dir, split, class_name)
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)

    # Get all the images in the current class directory
    class_dir = os.path.join(dataset_dir, class_name)
    images = [img for img in os.listdir(class_dir) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Shuffle the images randomly
    shuffle(images)

    # Calculate the number of images for each split
    train_count = int(train_ratio * len(images))
    valid_count = int(valid_ratio * len(images))

    # Split the images
    train_images = images[:train_count]
    valid_images = images[train_count:train_count + valid_count]
    test_images = images[train_count + valid_count:]

    # Copy the images to their respective directories
    for img in train_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(output_dir, 'train', class_name))
    for img in valid_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(output_dir, 'valid', class_name))
    for img in test_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(output_dir, 'test', class_name))

# Get all class names from the dataset directory
classes = [d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d))]

# Split data for each class
for class_name in classes:
    split_data(class_name)

print('Data split complete!')
