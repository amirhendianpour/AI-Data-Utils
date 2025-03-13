import cv2
import numpy as np
import os

file_path = os.path.dirname(os.path.realpath(__file__))
if not file_path == os.getcwd():
    os.chdir(file_path)

a = os.listdir()

# تابع برای چرخش تصویر
def rotate_image(image, angle):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)

# تابع برای اعمال تغییرات رنگی
def adjust_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


for i in a:
    if i[-3:]== "jpg" or i[-3:]== "JPG" or i[-4:]== "jpeg" or i[-3:]== "png":
        # بارگذاری تصویر
        image = cv2.imread(i)

        # اجرای دیتا اگمنتیشن و ذخیره تصاویر
        rotated = rotate_image(image, angle=20)  # چرخش 45 درجه
        cv2.imwrite(i[:-4]+"(1)"+i[-4:], rotated)  # ذخیره تصویر چرخش یافته


# # نمایش تصاویر
# cv2.imshow('Original', image)
# cv2.imshow('Rotated', rotated)
# # cv2.imshow('Brighter', brighter)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
