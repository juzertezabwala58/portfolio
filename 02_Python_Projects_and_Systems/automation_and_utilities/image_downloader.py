"""
Automated Batch Image Scraper & Downloader
Author: Juzer Tezabwala
Description: High-performance image downloader utilizing Bing Image API with customizable limits and query lists.
"""

import os
import argparse
from bing_image_downloader import downloader

def download_images(queries: list, limit: int = 10, output_dir: str = "downloaded_images", adult_filter_off: bool = True, timeout: int = 60):
    """
    Downloads images for a given list of search queries.
    """
    print("=" * 60)
    print(f"🚀 Starting Automated Image Downloader")
    print(f"📁 Output Directory : {output_dir}")
    print(f"🖼️ Images per Query : {limit}")
    print("=" * 60)

    for idx, query in enumerate(queries, 1):
        print(f"\n[{idx}/{len(queries)}] Fetching images for: '{query}'...")
        try:
            downloader.download(
                query,
                limit=limit,
                output_dir=output_dir,
                adult_filter_off=adult_filter_off,
                force_replace=False,
                timeout=timeout,
                verbose=True
            )
            print(f"✅ Successfully downloaded images for '{query}'.")
        except Exception as e:
            print(f"❌ Error downloading images for '{query}': {e}")

    print("\n" + "=" * 60)
    print(f"🎉 Download process completed. Files saved in '{os.path.abspath(output_dir)}'.")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description="Automated Image Downloader CLI")
    parser.add_argument("-q", "--query", type=str, nargs="+", help="One or more search terms to download images for.")
    parser.add_argument("-l", "--limit", type=int, default=5, help="Number of images to download per query (Default: 5).")
    parser.add_argument("-o", "--output", type=str, default="images", help="Target output folder name (Default: 'images').")
    
    args = parser.parse_args()

    # Default queries if none provided via command line
    queries = args.query if args.query else [
        "Virat Kohli cricket",
        "Sachin Tendulkar cricket",
        "Rahul Dravid cricket"
    ]

    download_images(queries, limit=args.limit, output_dir=args.output)

if __name__ == "__main__":
    main()
