import cv2

# مسیر تصویر
image_path = '3.jpg'

try:
    # خواندن تصویر با استفاده از OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("تصویر پیدا نشد!")
    
    # تبدیل تصویر به سیاه و سفید برای تشخیص بهتر حاشیه‌ها
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)

    # استخراج حاشیه‌ها
    contours, _ = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # ایجاد یک کپی از تصویر برای نمایش نتایج
    output_image = image.copy()

    # محاسبه مساحت کل تصویر
    img_height, img_width = image.shape[:2]
    img_area = img_height * img_width

    # تعریف آستانه حداقل مساحت (مثلاً 1% از مساحت کل تصویر)
    min_area = 0.01 * img_area

    # حلقه برای پردازش هر حاشیه
    for contour in contours:
        # محاسبه مختصات مستطیل احاطه‌کننده
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h

        # نادیده گرفتن اشیاء خیلی بزرگ (بیش از 90% مساحت تصویر)
        if area > 0.9 * img_area:
            continue

        # فیلتر کردن اشیاء بر اساس حداقل مساحت
        if area > min_area:
            # رسم مستطیل دور اشیاء تشخیص‌داده‌شده
            cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # نمایش تصویر نهایی با مستطیل‌ها
    cv2.imshow('Detected Objects', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # ذخیره مختصات نسبی در فایل متنی برای YOLO
    with open('coordinates.txt', 'w') as file:
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            area = w * h

            # نادیده گرفتن اشیاء خیلی بزرگ یا خیلی کوچک
            if area > 0.9 * img_area or area < min_area:
                continue

            # تبدیل مختصات به فرمت نسبی برای YOLO
            x_center = (x + w / 2) / img_width
            y_center = (y + h / 2) / img_height
            width = w / img_width
            height = h / img_height

            # ذخیره مختصات با فرمت YOLO (کلاس فرضی 0)
            file.write(f'0 {x_center} {y_center} {width} {height}\n')

except Exception as e:
    print(f"خطا: {e}")
