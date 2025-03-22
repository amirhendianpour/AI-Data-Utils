import cv2
from PIL import Image

# فرض کنید 'image_path' مسیر تصویر شماست
image_path = '3.jpg'

# تصویر را با استفاده از OpenCV بخوانید
image = cv2.imread(image_path)

# تبدیل تصویر به سیاه و سفید برای ساده‌سازی تشخیص حاشیه‌ها
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)

# استخراج حاشیه‌ها و مختصات
contours, _ = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# ایجاد یک تصویر جدید برای نمایش نتایج
output_image = image.copy()

# حلقه برای رسم مستطیل دور هر حاشیه
for contour in contours:
    # محاسبه مختصات مستطیل احاطه‌کننده
    x, y, w, h = cv2.boundingRect(contour)
    if w - x > 100 and h - y > 100:  
        if w - x == 640 and h - y == 640:
            continue
    # رسم مستطیل دور حاشیه
        cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# نمایش تصویر نهایی
cv2.imshow('Detected Objects', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ذخیره مختصات در یک فایل متنی برای استفاده در YOLO
with open('coordinates.txt', 'w') as file:
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        file.write(f'{x},{y},{w},{h}\n')
