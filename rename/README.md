
# Image Renaming Script

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This Python script renames all JPG images in the directory where the script is located.

## Functionality

The script performs the following actions:

1.  Gets the directory where the script is located.

2.  Changes the current working directory to the script's directory.

3.  Lists all files in the directory.

4.  Iterates through the files, renames JPG files to `cls1.jpg`, `cls2.jpg`, and so on.

## Requirements

* Python 3.x

## How to Use

1.  Save the script to a file (e.g., `rename_images.py`).

2.  Place the script in the directory containing the JPG images you want to rename.

3.  Run the script from the command line:

    `python rename_images.py`

## Example

For example, if the directory contains the following files:

* `image1.jpg`

* `image2.JPG`

* `image3.png`

* `data.txt`

After running the script, the directory will contain the following files:

* `cls1.jpg`

* `cls2.jpg`

* `image3.png`

* `data.txt`
