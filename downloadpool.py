from downloadthread import DownloadThread

from PySide2 import QtCore
from urllib.parse import urlparse, parse_qs, parse_qsl, urlencode, urlunparse


class DownloadPool(QtCore.QObject):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.processes = {}

    @staticmethod
    def clean_url(url):
        url_parts = urlparse(url)
        query_parts = parse_qsl(url_parts.query)
        new_query_parts = []
        for (k, v) in query_parts:
            if k == 'index':
                continue
            elif k == 'start_radio':
                continue
            elif k == 'list':
                continue
            else:
                new_query_parts.append((k,v))

        new_components = list(url_parts)
        new_components[4] = urlencode(dict(new_query_parts), doseq=True, )
        return urlunparse(new_components)

    def remove_thread(self):
        url = self.sender().url
        self.processes.pop(url)

    def download(self, url, url_model):
        if url in self.processes:
            print('url is already downloaded or currently downloading')
            return

        download_dir = self.settings.get_download_dir()
        audio_only = self.settings.get_audio_only()
        video_res = self.settings.get_video_res()

        # Create the download thread.
        thread = DownloadThread(url, download_dir, video_res, audio_only)
        thread.signal.connect(url_model.update_row, QtCore.Qt.BlockingQueuedConnection)
        thread.finished.connect(self.remove_thread)

        self.processes[url] = thread
        thread.start()
