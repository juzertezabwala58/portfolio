"""
YouTube Video & Playlist Downloader CLI
Author: Juzer Tezabwala
Description: Fast, flexible YouTube single video and playlist downloader with format selection and yt-dlp / pytube support.
"""

import os
import sys
import subprocess
import argparse

def download_with_ytdlp(url: str, output_dir: str = "downloads", is_audio_only: bool = False, quality: str = "best"):
    """
    Downloads YouTube videos or playlists using yt-dlp engine.
    """
    os.makedirs(output_dir, exist_ok=True)
    out_template = os.path.join(output_dir, "%(playlist_index|00)s - %(title)s.%(ext)s" if "playlist" in url else "%(title)s.%(ext)s")

    cmd = ["yt-dlp", "-o", out_template]

    if is_audio_only:
        cmd.extend(["-x", "--audio-format", "mp3", "--audio-quality", "0"])
    else:
        if quality == "best":
            cmd.extend(["-f", "bestvideo+bestaudio/best"])
        else:
            cmd.extend(["-f", f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]"])

    cmd.append(url)

    print("=" * 60)
    print("🎬 Starting YouTube Media Download")
    print(f"🔗 Target URL : {url}")
    print(f"📁 Destination: {os.path.abspath(output_dir)}")
    print(f"🎵 Audio Only : {is_audio_only}")
    print("=" * 60)

    try:
        subprocess.run(cmd, check=True)
        print("\n✅ Download completed successfully!")
    except FileNotFoundError:
        print("\n⚠️ 'yt-dlp' is not found in PATH. Attempting fallback via PyTube...")
        download_with_pytube(url, output_dir, is_audio_only)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Download failed: {e}")

def download_with_pytube(url: str, output_dir: str = "downloads", is_audio_only: bool = False):
    """
    Fallback downloader utilizing pytube library.
    """
    try:
        from pytube import YouTube, Playlist
        if "playlist" in url:
            pl = Playlist(url)
            print(f"Downloading Playlist: {pl.title} ({len(pl.videos)} videos)")
            for video in pl.videos:
                print(f"Downloading: {video.title}")
                stream = video.streams.get_audio_only() if is_audio_only else video.streams.get_highest_resolution()
                if stream:
                    stream.download(output_path=output_dir)
        else:
            yt = YouTube(url)
            print(f"Downloading Video: {yt.title}")
            stream = yt.streams.get_audio_only() if is_audio_only else yt.streams.get_highest_resolution()
            if stream:
                stream.download(output_path=output_dir)
        print("\n✅ Download completed via PyTube!")
    except ImportError:
        print("❌ Neither yt-dlp nor pytube are installed. Install via 'pip install yt-dlp pytube'.")
    except Exception as e:
        print(f"❌ PyTube error: {e}")

def main():
    parser = argparse.ArgumentParser(description="YouTube Video & Playlist Downloader")
    parser.add_argument("url", nargs="?", help="YouTube video or playlist URL.")
    parser.add_argument("-o", "--output", default="downloads", help="Output directory path (Default: 'downloads').")
    parser.add_argument("-a", "--audio", action="store_true", help="Download audio only in MP3 format.")
    parser.add_argument("-q", "--quality", default="best", choices=["best", "1080", "720", "480", "360"], help="Max video resolution.")
    
    args = parser.parse_args()

    url = args.url
    if not url:
        url = input("Enter YouTube Video or Playlist URL: ").strip()
        if not url:
            print("❌ No URL provided. Exiting.")
            sys.exit(1)

    download_with_ytdlp(url, output_dir=args.output, is_audio_only=args.audio, quality=args.quality)

if __name__ == "__main__":
    main()
