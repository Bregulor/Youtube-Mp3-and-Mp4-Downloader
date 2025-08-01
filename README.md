# Youtube-MP3-and-MP4-Downloader
This is a simple program for downloading Youtube videos in MP3 and MP4 format.

#  YouTube Music Downloader

YouTube Music Downloader is a desktop application that allows users to download content from YouTube in audio (MP3) and video (MP4) formats. Developed using BeeWare, the app can run independently on any Windows computer with an internet connection.


---

## Features

* Download MP3 and MP4 files from YouTube

---

##  Built With

* [Python](https://python.org/)
* [BeeWare / Toga](https://beeware.org/)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [ffmpeg (embedded)](https://ffmpeg.org/)
* [Briefcase](https://beeware.org/project/projects/tools/briefcase/)

---

##  Installation

### Requirements

* Python 3.10 or higher
* `pip`, `git`, and `briefcase`

```bash
pip install briefcase
```

### Setup Steps

1. Clone this project:

```bash
git clone https://github.com/your_username/youtube-music-downloader.git
cd youtube-music-downloader
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Optionally, add `ffmpeg.exe` and an icon file to your `pyproject.toml`, then update:

```bash
briefcase update -r
```

4. Run the app in development mode:

```bash
briefcase dev
```

5. Build a distributable version of the app:

```bash
briefcase build
briefcase package
```

6. Your desktop application is now ready along with the output file.

---

## How to Use

* Enter a YouTube URL
* Choose MP3 or MP4
* Click the “Download” button
* The converted file will be saved in the `indirilenler` folder on your desktop

---

##  Contact

**Developer:** Sarp Erdoğan
**Email:** [sarpindcsi@gmail.com](mailto:sarpindcsi@gmail.com)

