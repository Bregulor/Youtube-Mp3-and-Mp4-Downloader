import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import yt_dlp
import os

class MuzikIndirici(toga.App):
    def startup(self):
        self.linkInput = toga.TextInput(style=Pack(direction=COLUMN, flex=1))
        self.mp3Buton = toga.Button(
            "Mp3 olarak indir",
            on_press=self.mp3fonk,
            style=Pack(direction=ROW, flex=1)
        )
        self.mp4Buton = toga.Button(
            "Mp4 olarak indir",
            on_press=self.mp4fonk,
            style=Pack(direction=ROW, flex=1)
        )
        self.label = toga.Label("", style=Pack(flex=1))
        self.butonBox = toga.Box(style=Pack(direction=ROW, flex=1))
        self.butonBox.add(self.mp3Buton)
        self.butonBox.add(self.mp4Buton)

        self.inputBox = toga.Box(style=Pack(direction=COLUMN, flex=1, padding=10))
        self.inputBox.add(self.linkInput)
        self.inputBox.add(self.butonBox)
        self.inputBox.add(self.label)

        main_box = toga.Box(style=Pack(direction=COLUMN, flex=1))
        main_box.add(self.inputBox)

        self.main_window = toga.MainWindow(title="YouTube Müzik İndirici")
        self.main_window.content = main_box
        self.main_window.show()

    def get_ffmpeg_path(self):
        return os.path.join(
            os.path.dirname(__file__),
            'resources', 'ffmpeg', 'ffmpeg-7.1.1-essentials_build', 'bin', 'ffmpeg.exe'
        )

    def mp3fonk(self, widget):
        link = self.linkInput.value.strip()
        if not link:
            self.label.text = "Lütfen bir link girin!"
            return

        klasor = os.path.expanduser("~/Desktop/İndirilen videolar ve müzikler")
        os.makedirs(klasor, exist_ok=True)

        ayarlar = {
            'format': 'bestaudio',
            'outtmpl': os.path.join(klasor, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': self.get_ffmpeg_path(),
            'noplaylist': True,
            'quiet': True,
            'concurrent_fragment_downloads': 3
        }

        try:
            self.label.text = "MP3 indiriliyor..."
            with yt_dlp.YoutubeDL(ayarlar) as ydl:
                ydl.download([link])
            self.label.text = "MP3 indirme tamamlandı."
        except Exception as e:
            self.label.text = f"Hata: {str(e)}"

    def mp4fonk(self, widget):
        link = self.linkInput.value.strip()
        if not link:
            self.label.text = "Lütfen bir link girin!"
            return

        klasor = os.path.expanduser("~/Desktop/İndirilen videolar ve müzikler")
        os.makedirs(klasor, exist_ok=True)

        ayarlar = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(klasor, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'ffmpeg_location': self.get_ffmpeg_path(),
            'noplaylist': True,
            'quiet': True,
        }

        try:
            self.label.text = "MP4 indiriliyor..."
            with yt_dlp.YoutubeDL(ayarlar) as ydl:
                ydl.download([link])
            self.label.text = "MP4 indirme tamamlandı."
        except Exception as e:
            self.label.text = f"Hata: {str(e)}"

def main():
    return MuzikIndirici()
