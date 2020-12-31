from ydllogger import YDLLogger
from ydlprogress import YDLProgress

from youtube_dl.YoutubeDL import YoutubeDL
from multiprocessing import Process, Pipe, Queue

from PySide2.QtCore import QThread, Signal

import os


class DownloadThread(QThread):
    signal = Signal(str, dict)

    def __init__(self, url, download_dir, video_res, audio_only):
        super().__init__()
        self.url = url
        self.download_dir = download_dir
        self.video_res = video_res
        self.audio_only = audio_only
        self.root_dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
        self.progress = YDLProgress()

    def run(self):
        if self.audio_only:
            options = self.create_audio_option()
        else:
            options = self.create_video_option(self.video_res)

        ydl = YoutubeDL(options)
        print('Download url: %s' % self.url)
        ydl.download([self.url])
        self.signal.emit(self.url, {'youmacro_done': True})

    def on_progress(self, info):
        self.progress.update_obj(info)
        self.signal.emit(self.url, self.progress.obj)

    def create_video_option(self, max_height=0):
        opt = {
                'outtmpl': self.download_dir + '/%(title)s-%(id)s.%(ext)s',
                'format': 'bestvideo[height<=?1080]+bestaudio/best',
                'logger': YDLLogger(),
                'progress_hooks': [self.on_progress],
                'merge_output_format': 'mp4',
                'write_thumbnail': True,
                'embed_thumbnail': True,
                'add_metadata': [self.url],
                'ffmpeg_location': self.root_dir + '/deps/ffmpeg-4.3-win64-static/bin'
            }
        if max_height:
            opt['format'] = 'bestvideo[height<=?' + str(max_height) + ']+bestaudio/best'
        return opt

    def create_audio_option(self):
        opt = {
            'postprocessors': [{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': '192',
            }],
            'outtmpl': self.download_dir + '/%(title)s-%(id)s.%(ext)s',
            'format': 'm4a',
            'audioformat': 'mp3',
            'extractaudio': True,
            'logger': YDLLogger(),
            'progress_hooks': [self.on_progress],
            'add_metadata': [self.url],
            'ffmpeg_location': self.root_dir + '/deps/ffmpeg-4.3-win64-static/bin'
        }
        return opt






