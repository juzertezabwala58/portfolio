"""
Dynamic QR Code Generator Utility
Author: Juzer Tezabwala
Description: Generates high-resolution, custom-styled QR codes for URLs, text, Wi-Fi credentials, and contact info.
"""

import os
import argparse
import qrcode
from PIL import Image

def generate_qr(data: str, output_file: str = "qrcode.png", fill_color: str = "black", back_color: str = "white", box_size: int = 10, border: int = 4):
    """
    Generates and saves a customizable QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_file)

    print("=" * 60)
    print(f"✅ QR Code generated successfully!")
    print(f"📄 Encoded Content : {data}")
    print(f"🎨 Colors          : Fill='{fill_color}', Background='{back_color}'")
    print(f"💾 Saved To        : {os.path.abspath(output_file)}")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description="Custom QR Code Generator")
    parser.add_argument("data", nargs="?", help="Text or URL to encode in the QR code.")
    parser.add_argument("-o", "--output", default="generated_qrcode.png", help="Output image filename (Default: 'generated_qrcode.png').")
    parser.add_argument("-f", "--fill", default="black", help="QR code pattern color (Default: 'black').")
    parser.add_argument("-b", "--back", default="white", help="Background color (Default: 'white').")
    parser.add_argument("-s", "--size", type=int, default=10, help="Box size in pixels (Default: 10).")
    
    args = parser.parse_args()

    data = args.data
    if not data:
        data = input("Enter Text or URL to encode into QR code: ").strip()
        if not data:
            data = "https://github.com/juzertezabwala58/portfolio"

    generate_qr(data, output_file=args.output, fill_color=args.fill, back_color=args.back, box_size=args.size)

if __name__ == "__main__":
    main()
