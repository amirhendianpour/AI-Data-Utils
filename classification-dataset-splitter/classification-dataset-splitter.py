import os
import shutil
from random import seed, shuffle

# Set the seed for reproducibility
seed(1)

# Define dataset and output directories
dataset_dir = r"D:\data_orange\input"  # Use raw string (r"...") to avoid escape issues
output_dir = r"D:\data_orange\out"

# Split ratios
train_ratio, valid_ratio = 0.7, 0.2
test_ratio = 1 - (train_ratio + valid_ratio)  # Ensures sum is 1.0

# Create output directories
for split in ['train', 'valid', 'test']:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Function to split data
def split_data(class_name):
    class_dir = os.path.join(dataset_dir, class_name)
    images = [img for img in os.listdir(class_dir) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not images:  # Skip empty classes
        print(f"⚠ Warning: No images found for class '{class_name}'")
        return

    shuffle(images)  # Shuffle for randomness

    # Split indices
    train_count = int(train_ratio * len(images))
    valid_count = int(valid_ratio * len(images))

    split_dict = {
        "train": images[:train_count],
        "valid": images[train_count:train_count + valid_count],
        "test": images[train_count + valid_count:]
    }

    for split, split_images in split_dict.items():
        split_class_dir = os.path.join(output_dir, split, class_name)
        os.makedirs(split_class_dir, exist_ok=True)

        for img in split_images:
            src_path = os.path.join(class_dir, img)
            dest_path = os.path.join(split_class_dir, img)
            shutil.copy(src_path, dest_path)  # Use shutil.move(src_path, dest_path) if you want to move instead of copy

    print(f"✅ Processed class '{class_name}': {len(images)} images")

# Get all class names and split data
classes = [d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d))]

for class_name in classes:
    split_data(class_name)

print("🎉 Data split complete!")
