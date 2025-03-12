# AI-Data-Utils

[🇬🇧 English Version](#english-version) | [🇮🇷 نسخه فارسی](#نسخه-فارسی)

---

## 🇮🇷 نسخه فارسی

### 🛠️ مجموعه اسکریپت‌های پردازش داده برای هوش مصنوعی

این ریپازیتوری شامل مجموعه‌ای از اسکریپت‌های پایتونی برای انجام کارهای مختلف پردازش داده است. این اسکریپت‌ها به شما کمک می‌کنند تا داده‌های خود را برای پروژه‌های یادگیری ماشین و هوش مصنوعی آماده‌سازی کنید.

## 📌 قابلیت‌ها
- **تغییر نام فایل‌ها**: تغییر نام خودکار فایل‌های یک پوشه به فرمت ساده و شماره‌گذاری‌شده
- **تغییر اندازه تصاویر**: تغییر اندازه تصاویر در یک پوشه به ابعاد مشخص‌شده
- **پاک‌سازی داده‌های CSV**: حذف سطرهای دارای مقادیر نامعتبر و پاک‌سازی داده‌های متنی
- **و موارد دیگر...**

## 📂 ساختار پروژه
```
AI-Data-Utils/
│── scripts/               # شامل تمام اسکریپت‌ها
│   │── rename_files.py    # اسکریپت تغییر نام فایل‌ها
│   │── resize_images.py   # اسکریپت تغییر اندازه تصاویر
│   │── csv_cleaner.py     # اسکریپت پاک‌سازی فایل‌های CSV
│   └── ...                # سایر اسکریپت‌ها
│
│── examples/              # نمونه داده‌ها یا نحوه اجرای اسکریپت‌ها
│   │── sample_data/       # چند فایل تستی
│   └── usage_examples.md  # توضیح نحوه اجرای اسکریپت‌ها
│
│── docs/                  # مستندات (در صورت گسترش پروژه)
│   └── guide.md           # راهنمای استفاده کلی
│
│── LICENSE                # فایل لایسنس (مثلاً MIT)
│── README.md              # توضیحات کلی پروژه و نحوه استفاده
│── requirements.txt       # لیست وابستگی‌های پایتون (در صورت نیاز)
└── .gitignore             # برای نادیده گرفتن فایل‌های غیرضروری
```

## 🚀 نحوه استفاده
۱. ابتدا این ریپازیتوری را کلون کنید:
```bash
git clone https://github.com/amirhendianpour/AI-Data-Utils.git
cd AI-Data-Utils
```
۲. اگر اسکریپت‌های شما نیاز به وابستگی‌های خاصی دارند، می‌توانید آنها را با استفاده از `requirements.txt` نصب کنید:
```bash
pip install -r requirements.txt
```
۳. اجرای یک اسکریپت نمونه، مثلا تغییر نام فایل‌ها:
```bash
python scripts/rename_files.py --path /path/to/folder
```

## 📝 لایسنس
این پروژه تحت لایسنس **MIT** منتشر شده است. شما می‌توانید از آن به‌صورت رایگان استفاده کنید، اما مسئولیت استفاده از کد بر عهده‌ی خود شما است.

## 🤝 مشارکت
اگر مایل به بهبود این ریپازیتوری هستید، می‌توانید **Pull Request** ارسال کنید یا یک **Issue** باز کنید. هرگونه پیشنهاد یا بهینه‌سازی پذیرفته می‌شود! 😊

---

## 🇬🇧 English Version

### 🛠️ AI Data Processing Scripts

This repository contains a collection of Python scripts for various data processing tasks. These scripts help you prepare your data for machine learning and AI projects.

## 📌 Features
- **File Renaming**: Automatically renames files in a folder to a simple numbered format
- **Image Resizing**: Resizes images in a folder to specified dimensions
- **CSV Cleaning**: Removes invalid rows and cleans textual data in CSV files
- **And more...**

## 📂 Project Structure
```
AI-Data-Utils/
│── scripts/               # All scripts
│   │── rename_files.py    # File renaming script
│   │── resize_images.py   # Image resizing script
│   │── csv_cleaner.py     # CSV cleaning script
│   └── ...                # Other scripts
│
│── examples/              # Sample data and usage examples
│   │── sample_data/       # Test files
│   └── usage_examples.md  # Instructions for running scripts
│
│── docs/                  # Documentation (if extended)
│   └── guide.md           # General usage guide
│
│── LICENSE                # License file (e.g., MIT)
│── README.md              # Project description and usage
│── requirements.txt       # Python dependencies (if needed)
└── .gitignore             # Ignore unnecessary files
```

## 🚀 Usage
1. Clone the repository:
```bash
git clone https://github.com/amirhendianpour/AI-Data-Utils.git
cd AI-Data-Utils
```
2. If your scripts require dependencies, install them using `requirements.txt`:
```bash
pip install -r requirements.txt
```
3. Run a sample script, e.g., renaming files:
```bash
python scripts/rename_files.py --path /path/to/folder
```

## 📝 License
This project is released under the **MIT License**. You are free to use it, but usage is at your own risk.

## 🤝 Contributing
If you’d like to contribute, feel free to submit a **Pull Request** or open an **Issue**. Any suggestions or improvements are welcome! 😊

---

**📧 Contact Me:**
- GitHub: [amirhendianpour](https://github.com/amirhendianpour)
- Email: amir.hendianpour@gmail.com

