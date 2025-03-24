# Object Detection Dataset Splitting Script

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

This script is designed for **splitting object detection datasets** into three sets: **Training (70%)**, **Validation (20%)**, and **Testing (10%)**. It organizes the data in a structure compatible with **YOLO and similar models**.

## **Features**
- **Randomly splits data** into `train`, `valid`, and `test` sets.
- **Structured organization:** Data is stored in **`images`** and **`labels`** folders.
- **Avoids duplicate filenames:** Uses **SHA-256 hashing** to rename files.
- **Progress tracking:** Displays a progress bar using **`tqdm`**.
- **Supports multiple image formats:** `.jpg`, `.png`, `.jpeg`.

---

## **Folder Structure**

### **Before Splitting**
```
/path/to/source/
    ├── Class1
    │   ├── image1.jpg
    │   ├── image1.txt
    │   ├── image2.png
    │   ├── ...
    ├── Class2
    │   ├── image1.jpg
    │   ├── image1.txt
    │   ├── ...
```

### **After Splitting**
```
/path/to/dataset/
    ├── train/
    │   ├── images/
    │   ├── labels/
    ├── valid/
    │   ├── images/
    │   ├── labels/
    ├── test/
    │   ├── images/
    │   ├── labels/
```

---

## **Requirements**
- **Python 3.x installed**
- Required libraries:
  ```sh
  pip install tqdm
  ```

---

## **Usage**
1. Download or clone this project.
2. Modify `source_directory` and `base_directory` paths in the code.
3. Run the script:
   ```sh
   python object-detection-dataset-splitter.py
   ```
4. The processed data will be stored in the specified output directory.

---

## **Customization**
- Adjust the split ratios by modifying `split_ratios=(0.7, 0.2, 0.1)`.
- To move files instead of copying, replace `shutil.copy` with `shutil.move`.

---

## **Important Notes**
- Filenames are hashed to **prevent duplication and conflicts**.
- `.txt` label files (containing **YOLO annotations**) are moved along with their corresponding images.
- A warning is displayed if a **label file is missing**.
