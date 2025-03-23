import cv2
import numpy as np
import os

# دریافت مسیر جاری اسکریپت
file_path = os.path.dirname(os.path.realpath(__file__))
if file_path != os.getcwd():
    os.chdir(file_path)

# دریافت لیست فایل‌ها در مسیر جاری
file_list = os.listdir()

# فرمت‌های معتبر تصاویر
valid_formats = ('.jpg', '.jpeg', '.png')

# دریافت ورودی از کاربر برای نوع پردازش
rotate = input("Apply rotation? (yes/no): ").strip().lower() == "yes"
brighten = input("Apply brightness adjustment? (yes/no): ").strip().lower() == "yes"

# تابع چرخش تصویر
def rotate_image(image, angle):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)

# تابع افزایش روشنایی
def adjust_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

# پردازش تصاویر
for file_name in file_list:
    if file_name.lower().endswith(valid_formats):
        image_path = os.path.join(file_path, file_name)
        image = cv2.imread(image_path)

        # بررسی موفقیت بارگذاری تصویر
        if image is None:
            print(f"Warning: Unable to read {file_name}")
            continue

        # جدا کردن نام و پسوند فایل
        file_base, file_ext = os.path.splitext(file_name)

        # اعمال عملیات مورد نظر
        if rotate:
            rotated = rotate_image(image, angle=20)
            rotated_path = os.path.join(file_path, f"{file_base}_rotated{file_ext}")
            cv2.imwrite(rotated_path, rotated)
            print(f"Saved rotated image: {rotated_path}")

        if brighten:
            brighter = adjust_brightness(image, value=30)
            brighter_path = os.path.join(file_path, f"{file_base}_brighter{file_ext}")
            cv2.imwrite(brighter_path, brighter)
            print(f"Saved brightened image: {brighter_path}")

print("\n✅ Image augmentation completed!")
