# OCR Project for macOS

This project allows you to extract text from images using Tesseract OCR. It supports `.webp`, `.png`, `.jpg`, `.tiff`, and other formats supported by Pillow.

---

## Features

- Works with multiple image formats.
- Supports multiple languages (Swedish, English, or both).
- Saves OCR output to a text file.
- Easy to run on macOS with Python.

---

## 1. Clone the repository

```bash
git clone https://github.com/JHelgesson/py-ocr
cd py-ocr
```

---

## 2. Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## 3. Install Tesseract OCR

```bash
brew install tesseract
```

For Swedish language support:

```bash
brew install tesseract-lang
```

Check the installation:

```bash
tesseract --version
```

> ⚠️ On Intel Macs, Tesseract is usually at `/usr/local/bin/tesseract`.  
> On M1/M2 Macs, it is usually at `/opt/homebrew/bin/tesseract`.

---

## 4. Create a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 5. Install Python dependencies

```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```
---

## 6. Add your images

Place images in the `img/` folder:

```
img/example.webp
```

---

## 7. Run the OCR script

```bash
python ocr.py img/example.webp
```
or 
```bash
python3 ocr.py img/example.webp
```

- Extracted text is printed in the terminal.  
- Text is also saved to `result.txt`.

---

## 8. If Python cannot find Tesseract

Add the following line **above** `image_to_string` in `ocr.py`:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"  # or /usr/local/bin/tesseract on Intel Macs
```

---

## 9. Tips

- Change language:  
  - `lang="swe"` → Swedish  
  - `lang="eng"` → English  
  - `lang="swe+eng"` → Both  

- Supports `.webp`, `.png`, `.jpg`, `.tiff`, etc.  
- To save the text file with the same name as the image, the script can be extended.

---

## Example Workflow

```bash
# Activate virtual environment
source .venv/bin/activate

# Run OCR on a WebP image
python ocr_test.py img/example.webp

# Check the results
cat resultat.txt
```
