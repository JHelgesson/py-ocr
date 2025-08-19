import sys
import os
from PIL import Image
import pytesseract

# Path to Tesseracts tessdata-mapp
os.environ["TESSDATA_PREFIX"] = "/opt/homebrew/share/tessdata"


def run_ocr(image_path, lang="fra"):
    """Do OCR on image and save text"""
    # Open image (webp/jpg/png funkar med Pillow)
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang=lang)
    return text

def main():
    # Check for image filename argument
    if len(sys.argv) < 2:
        print("❌ Usage: python ocr.py <path_to_picture>")
        sys.exit(1)

    # Get filename from argument
    image_path = sys.argv[1]

    # Check if image exists
    if not os.path.exists(image_path):
        print(f"❌ Could not find file: {image_path}")
        sys.exit(1)

    # Do OCR with Tesseract
    text = run_ocr(image_path, lang="fra")

    # Save result to file
    output_file = "result.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\n✅ Done! Result saved in {output_file}")

if __name__ == "__main__":
    main()
