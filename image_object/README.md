# Object Detection with OpenCV and YOLO

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This Python script uses OpenCV to detect objects in images and saves their coordinates in a format suitable for use with YOLO (You Only Look Once).

## Description

This script is designed to identify objects within an input image and then extract their bounding box coordinates for further processing or model training. Here's a breakdown of how it works:

1.  **Import Libraries:** The script begins by importing the necessary libraries: OpenCV (`cv2`) and PIL for image operations.

2.  **Read Image:** The input image is read using `cv2.imread()` from the path specified by the `image_path` variable.

3.  **Pre-processing:**
    * The color image is converted to grayscale to simplify edge detection.
    * An inverse binary threshold is applied to the grayscale image to obtain clear edges for contour detection.

4.  **Contour Detection:** The `cv2.findContours()` function is used to extract the contours of objects in the thresholded image. These contours represent the boundaries of the objects.

5.  **Bounding Box Filtering and Drawing:**
    * The script iterates through the detected contours.
    * Contours smaller than 100x100 pixels and larger than 640x640 pixels are ignored to filter out noise or irrelevant objects.
    * For each remaining contour, the script calculates a rectangular bounding box using `cv2.boundingRect()`.
    * This bounding box is then drawn on the original image as a green rectangle with a thickness of 2 pixels.

6.  **Display Results:** The modified image with the bounding boxes is displayed in a window using `cv2.imshow()`. The script waits for a key press (`cv2.waitKey(0)`) before closing all open windows (`cv2.destroyAllWindows()`).

7.  **Save Coordinates:**
    * Finally, the script saves the coordinates of the bounding boxes to a text file named `coordinates.txt`.
    * Each line in the file represents one detected object and contains its coordinates (x, y, width, height) separated by commas. This format is suitable for use with object detection algorithms like YOLO, which require bounding box coordinates for training or prediction.

## Requirements

* Python 3.x
* OpenCV (`cv2`)
* PIL (Pillow)

## How to Use

1.  Ensure you have Python 3.x installed.
2.  Install OpenCV and PIL via pip:

    \`\`\`
    pip install opencv-python
    pip install Pillow
    \`\`\`
3.  Run the Python script.

## Input

* The script takes an input image, the path to which is specified by the `image_path` variable. By default, it is set to '3.jpg'.

## Output

The script produces two forms of output:

1.  **Visual Display:** A window will appear, showing the original image with green bounding boxes drawn around the detected objects.
2.  **Text File Output:** A text file named `coordinates.txt` is created in the same directory as the script. This file contains the coordinates of the detected bounding boxes, with each object on a new line in the format "x, y, width, height".

## Parameters

* `image_path`: The path to the input image.
* `cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)`: The threshold value (128) might need adjustment.
* `if w - x > 100 and h - y > 100:`: The minimum bounding box size.
* `if w - x == 640 and h - y == 640:`: The maximum bounding box size.
* `cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)`: The rectangle color and thickness.
* `with open('coordinates.txt', 'w') as file:`: The output file name.
