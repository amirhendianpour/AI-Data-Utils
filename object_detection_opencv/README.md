# Object Detection and YOLO Coordinate Extraction with OpenCV

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This project is a Python script that uses the OpenCV library to detect objects in an image, draw bounding boxes around them, and save their relative coordinates in the YOLO format.

## Prerequisites

To run this code, you need the following installed:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (installed by default with OpenCV)

### Installation
Run the following command in your terminal or command line:
```bash
pip install opencv-python
```

## How the Code Works

1. **Input**: An image in JPG format (in this code, `3.jpg` is used as the input).
2. **Processing**:
   - The image is converted to grayscale for better edge detection.
   - Contours are extracted using thresholding.
   - Bounding boxes are drawn around detected objects.
3. **Filtering**:
   - Objects that are too small (less than 1% of the image area) or too large (more than 90% of the image area) are ignored.
4. **Output**:
   - The final image with green bounding boxes around objects is displayed.
   - Relative coordinates of the objects are saved in the `coordinates.txt` file in YOLO format.

## Output File Structure (`coordinates.txt`)
Coordinates are saved in the following format, suitable for YOLO:
```
<class_id> <x_center> <y_center> <width> <height>
```
- `<class_id>`: Class identifier (defaulted to 0 in this code).
- `<x_center>` and `<y_center>`: Relative center coordinates of the bounding box based on image width and height.
- `<width>` and `<height>`: Relative width and height of the bounding box.

Example:
```
0 0.45 0.50 0.20 0.30
```

## How to Run

1. Place your desired image (e.g., `3.jpg`) in the same directory as the script.
2. Run the code:
   ```bash
   python script.py
   ```
3. The output image with detected bounding boxes will be displayed. Press any key to close the window.
4. The `coordinates.txt` file will be created in the same directory.

## Important Notes
- Update the image file path (`image_path`) as needed.
- The minimum area threshold (`min_area`) and maximum area (90% of the image) can be adjusted.
- If an error occurs (e.g., image not found), an error message will be displayed.

## Troubleshooting
- **"Image not found" error**: Ensure the `3.jpg` file exists in the correct directory.
- **"cv2 module not found" error**: Install OpenCV using `pip install opencv-python`.

## Future Improvements
- Add support for assigning different classes to objects.
- Enable processing of multiple images (e.g., from a folder).
- Enhance object filtering with more advanced algorithms.

## Author
This code was written by Amir Hendianpour. For questions or suggestions, feel free to contact me!
