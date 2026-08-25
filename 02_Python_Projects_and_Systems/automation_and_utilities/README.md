# ⚡ Python Automation & Web Scraping Utilities

## 📌 Overview
A collection of standalone, command-line automation and utility tools designed to simplify media acquisition, web scraping, and digital asset generation.

---

## 🛠️ Included Utilities

### 1. `image_downloader.py` (Automated Image Scraper)
- **Features**: Multi-query batch downloader utilizing Bing Image API, customizable image counts, output directories, and timeout controls.
- **Usage**:
  ```bash
  # Download 10 images for specific search queries
  python image_downloader.py -q "Machine Learning" "Artificial Intelligence" -l 10 -o "tech_images"
  ```

### 2. `youtube_downloader.py` (Media Stream Downloader)
- **Features**: Fast video & full playlist downloader utilizing `yt-dlp` (with `pytube` fallback), supporting 1080p, 720p, or high-bitrate MP3 audio extraction.
- **Usage**:
  ```bash
  # Download highest quality video
  python youtube_downloader.py "https://www.youtube.com/watch?v=EXAMPLE_ID"

  # Extract audio only in MP3 format
  python youtube_downloader.py "https://www.youtube.com/watch?v=EXAMPLE_ID" -a
  ```

### 3. `qr_code_generator.py` (Dynamic QR Generator)
- **Features**: Generates high-density QR codes for URLs, contact cards, and Wi-Fi credentials with customizable foreground and background color palettes.
- **Usage**:
  ```bash
  python qr_code_generator.py "https://github.com/juzertezabwala58/portfolio" -o "my_portfolio_qr.png" -f "darkblue"
  ```
