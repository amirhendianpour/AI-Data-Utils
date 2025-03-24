# AI-Data-Utils

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

### 🛠️ A collection of data processing scripts for AI

This repository contains a set of Python scripts for various data processing tasks. These scripts help you prepare your data for machine learning and AI projects.

## 📌 Features
- **File renaming**: Automatically rename files in a folder to a simple, numbered format.
- **Image resizing**: Resize images in a folder to specified dimensions.
- **CSV data cleaning**: Remove rows with invalid values and clean textual data.
- **And more...**

## About the Project
AI-Data-Utils is a collection of useful tools for processing and managing image data in the field of artificial intelligence. These tools include dataset splitting, data augmentation, file and folder renaming, file searching, and image resizing.

## Project Structure

```
AI-Data-Utils/
├── aug-cv2/
│   ├── image_augmentation.py
│   ├── requirements.txt
├── classification-dataset-splitter/
│   ├── classification-dataset-splitter.py
├── image_object/
│   ├── image_object.py
├── object-detection-dataset-splitter/
│   ├── object-detection-dataset-splitter.py
├── rename/
│   ├── rename_images.py
├── rename_file_folder/
│   ├── rename_file_folder.py
├── rename_name_folder/
│   ├── rename_folders.py
├── search/
│   ├── search.py
├── square_and_resize/
│   ├── resize_and_square_images.py
│   ├── requirements.txt
```

## Tools

### 1. **Image Data Augmentation** (`aug-cv2`)
This module includes tools for augmenting image data using OpenCV.

### 2. **Classification Dataset Splitter** (`classification-dataset-splitter`)
A tool for splitting classification datasets into training, validation, and test sets.

### 3. **Image Management** (`image_object`)
Includes tools for working with and processing images.

### 4. **Object Detection Dataset Splitter** (`object-detection-dataset-splitter`)
A tool for splitting datasets used in object detection.

### 5. **Image Renaming** (`rename`)
A tool to rename images in a specific folder.

### 6. **File and Folder Renaming** (`rename_file_folder`)
A tool for automatically renaming files and folders.

### 7. **Folder Renaming** (`rename_name_folder`)
A tool to rename folders based on specific rules.

### 8. **File Searching** (`search`)
A tool for searching within files and folders.

### 9. **Image Resizing and Squaring** (`square_and_resize`)
A tool to resize and square images, along with a requirements file.

## Usage
For each tool, navigate to the respective folder and check its `README.md` for execution details.

## Installing Dependencies
Some tools require specific libraries. To install dependencies for each tool, navigate to the respective folder and run:

```bash
pip install -r requirements.txt
```

## Contribution
If you’d like to contribute to this project, feel free to submit a pull request or report issues in the Issues section.

## License
