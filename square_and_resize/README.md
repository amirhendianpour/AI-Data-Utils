# Image Square & Resize

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This Python script processes image files in the current directory by performing two main operations:
1. Converts rectangular images into square images by adding padding (white space).
2. Resizes images to a specified size (default: 640x640).

It supports the following image formats:
- `.jpg`
- `.jpeg`
- `.png`

## Features
- Converts rectangular images to square by adding padding (white space).
- Resizes all images to a specified size (default: 640x640 pixels).
- Supports `.jpg`, `.jpeg`, and `.png` image formats.
- Uses `Pillow` (PIL) and `tqdm` libraries for image processing and progress tracking.

## Prerequisites
- Python 3.x
- `Pillow` library
- `tqdm` library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/amirhendianpour/[project-name].git
   ```
2. Navigate to the project directory:
   ```bash
   cd [project-name]
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file contains the following dependencies:
   ```
   Pillow
   tqdm
   ```

## Usage
1. Place your images in the project folder (or specify the path to the folder).
2. Run the script:
   ```bash
   python resize_and_square_images.py
   ```
3. The processed images will be saved with the same name, overwriting the original files.

### Example
- Input Image: `image1.jpg`  
  If it's rectangular, the script will add white padding and convert it into a square.
- Output Image: `image1.jpg`  
  The image will then be resized to `640x640` pixels.

## Project Structure
```
[project-name]/
│
├── resize_and_square_images.py  # Main script
├── README.md                    # Documentation
└── sample_images/               # Example images (optional)
```

## Developer
- [Amir] - [Your Email](mailto:amir.hendianpour@gmail.com)
