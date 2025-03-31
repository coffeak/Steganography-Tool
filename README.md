# Steganography Tool 🖼🔒  

![pr4](https://github.com/user-attachments/assets/56cae8f1-10e4-49c5-a197-f9f3c58b52c9)



A simple Python-based GUI application for hiding and extracting secret files within images using **LSB (Least Significant Bit) steganography**.

## Features 🚀  
- ✅ **Hide any file** (PDF, TXT, DOCX, etc.) inside an image (PNG).
- ✅ **Extract hidden files** with automatic file format detection.
- ✅ **User-friendly GUI** using `Tkinter`.
- ✅ **Preserves file extensions**, making extraction seamless.

## Requirements 📦  
Make sure you have **Python 3.7+** installed, then install dependencies:
```bash
pip install pillow stepic
```

## How to Use 🛠  

### Embedding Data:  
1. Click **"Browse"** and select a cover image (PNG).  
2. Click **"Browse"** and select the secret file (PDF, TXT, etc.).  
3. Click **"Embed Data"**, choose the output location, and save the modified image.  

### Extracting Data:  
1. Click **"Browse"** and select the image containing hidden data.  
2. Click **"Extract Data"**, and choose where to save the recovered file.  
3. The original file will be restored with the correct extension.  

## Developer 👨‍💻  
Developed by **[www.coffeak.com](https://www.coffeak.com)** ☕
