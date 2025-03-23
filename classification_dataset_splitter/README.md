# Classification Dataset Splitter Script

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This script is used to split an image dataset into three subsets: **Training (70%)**, **Validation (20%)**, and **Testing (10%)**. The dataset is assumed to be organized into subdirectories where each subdirectory represents a class.

## Features
- Randomly splits images into training, validation, and test sets.
- Ensures reproducibility using a fixed random seed.
- Creates the necessary output directories automatically.
- Supports `.png`, `.jpg`, and `.jpeg` image formats.

## Directory Structure
### Input Structure (Before Splitting)
```
D:\data_orange\input\
    ├── Class1
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   ├── ...
    ├── Class2
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   ├── ...
```
### Output Structure (After Splitting)
```
D:\data_orange\out\
    ├── train
    │   ├── Class1
    │   │   ├── img1.jpg
    │   │   ├── ...
    │   ├── Class2
    │   │   ├── img1.jpg
    │   │   ├── ...
    ├── valid
    │   ├── Class1
    │   ├── Class2
    ├── test
    │   ├── Class1
    │   ├── Class2
```

## Requirements
- Python 3.x
- Required modules: `os`, `shutil`, `random`

## Usage
1. Clone or download this repository.
2. Update the `dataset_dir` and `output_dir` variables in the script to match your dataset paths.
3. Run the script:
   ```sh
   python classification-dataset-splitter.py
   ```
4. The images will be split and stored in the specified output directory.

## Customization
- Modify `train_ratio`, `valid_ratio`, and `test_ratio` to change the split percentages.
- Change `shutil.copy` to `shutil.move` if you want to move files instead of copying them.

## Notes
- The script ensures that the sum of ratios equals 100%.
- If a class folder contains no images, a warning will be displayed.

## License
