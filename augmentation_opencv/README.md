# Image Augmentation Script

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This script performs **image augmentation** by applying **rotation** and **brightness adjustment** to images in the current directory. Users can choose which augmentation operations to apply.

## **Features**
- **Rotation**: Rotates images by a specified angle.
- **Brightness Adjustment**: Increases image brightness.
- **User Selection**: Users can enable or disable each augmentation operation.
- **Supports Multiple Formats**: Works with `.jpg`, `.jpeg`, and `.png`.

---

## **Folder Structure**
### **Before Processing**
```
/path/to/images/
    ├── image1.jpg
    ├── image2.png
    ├── image3.jpeg
```

### **After Processing (Example for Rotation and Brightness)**
```
/path/to/images/
    ├── image1.jpg
    ├── image1_rotated.jpg
    ├── image1_brighter.jpg
    ├── image2.png
    ├── image2_rotated.png
    ├── image2_brighter.png
```

---

## **Requirements**
- **Python 3.x**
- **Required Libraries:**
  ```sh
  pip install opencv-python numpy
  ```

---

## **How to Use**
1. Place the script in the directory containing the images.
2. Run the script:
   ```sh
   python image_augmentation.py
   ```
3. When prompted, choose whether to apply rotation and/or brightness adjustment.
4. Augmented images will be saved in the same directory with modified filenames.

---

## **Customization**
- Modify the rotation angle in `rotate_image(image, angle=20)`.  
- Adjust brightness intensity in `adjust_brightness(image, value=30)`.  
- Change supported image formats by modifying `valid_formats`.

---

## **Notes**
- The script automatically changes the working directory to the script’s location.
- It prevents overwriting by appending `_rotated` or `_brighter` to filenames.
- If an image fails to load, a warning is displayed.

