# Multi-Folder Image Renaming Script

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This Python script renames all `.jpg`, `.jpeg`, and `.png` images inside multiple subdirectories.  
It processes each folder and renames images sequentially as `lol1.jpg`, `lol2.jpg`, etc.

## Features
- Recursively renames images inside multiple folders.
- Automatically detects and processes all subdirectories.
- Prevents file name conflicts by checking for existing names.

## Prerequisites
- Python 3.x

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/amirhendianpour/[project-name].git
   ```

2. Navigate to the project directory:
   ```bash
   cd [project-name]
   ```

## Usage
1. Place the script in the main directory containing subdirectories with images.
2. Run the script using:
   ```bash
   python rename_folders.py
   ```
3. The images in each folder will be renamed as `lol1.jpg`, `lol2.jpg`, and so on.

## Project Structure
```
[project-name]/
│
├── rename_folders.py  # Main script
├── README.md          # Documentation
└── folders/           # Folder containing subdirectories with images
    ├── folder1/
    │   ├── image1.jpg → lol1.jpg
    │   ├── image2.jpg → lol2.jpg
    ├── folder2/
    │   ├── img1.png → lol1.jpg
    │   ├── img2.jpeg → lol2.jpg
```

## Developer
- [Amir] - [Your Email](mailto:amir.hendianpour@gmail.com)
