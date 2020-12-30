from ydllogger import YDLLogger
from ydlprogress import YDLProgress

from youtube_dl.YoutubeDL import YoutubeDL
from multiprocessing import Process, Pipe, Queue

from PySide2.QtCore import QThread, Signal

import os


class DownloadThread(QThread):
    signal = Signal(str, dict)

    def __init__(self, url, download_dir):
        super().__init__()
        self.url = url
        self.download_dir = download_dir
        self.root_dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
        self.progress = YDLProgress()

    def run(self):
        options = self.create_options(self.url, self.download_dir)
        ydl = YoutubeDL(options)
        print('Download url: %s' % self.url)
        ydl.download([self.url])
        self.signal.emit(self.url, {'youmacro_done': True})

    def on_progress(self, info):
        self.progress.update_obj(info)
        self.signal.emit(self.url, self.progress.obj)

    def create_options(self, url, download_dir):
        ONLY_AUDIO = 1

        if ONLY_AUDIO:
            return {
                # 'format': 'bestaudio/best',
                'postprocessors': [{
                   'key': 'FFmpegExtractAudio',
                   'preferredcodec': 'mp3',
                   'preferredquality': '192',
                }],
                'outtmpl': download_dir + '/%(title)s-%(id)s.%(ext)s',
                'format': 'm4a',
                'audioformat': 'mp3',
                'extractaudio': True,
                'logger': YDLLogger(),
                'progress_hooks': [self.on_progress],
                'ffmpeg_location': self.root_dir + '/deps/ffmpeg-4.3-win64-static/bin'
            }
        else:
            return {
                # 'format': 'bestaudio/best',
                # 'postprocessors': [{
                #    'key': 'FFmpegExtractAudio',
                #    'preferredcodec': 'mp3',
                #    'preferredquality': '192',
                # }],
                'outtmpl': download_dir + '/%(title)s-%(id)s.%(ext)s',
                'format': 'm4a',
                #'audioformat': 'mp3',
                'extractaudio': True,

                #'format': 'bestvideo+bestaudio/best',
                'logger': YDLLogger(),
                'progress_hooks': [self.on_progress],
                #'merge_output_format': 'mp4',
                #'write_thumbnail': True,
                #'embed_thumbnail': True,
                #'add_metadata': [url],
                'ffmpeg_location': self.root_dir + '/deps/ffmpeg-4.3-win64-static/bin'
            }






