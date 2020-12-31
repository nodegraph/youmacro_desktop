from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QSplashScreen

import os
import sys
import urllib.request
import zipfile
import shutil

root_dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')


def download_deps():
    url = 'https://github.com/ytdl-org/youtube-dl/archive/master.zip'
    zip_path = root_dir + '/master.zip'
    urllib.request.urlretrieve(url, zip_path)

    # Unpack the zip file.
    with zipfile.ZipFile(zip_path, 'r') as f:
        f.extractall(root_dir)

    # Delete the zip file.
    os.remove(zip_path)

    # Rename from youtube-dl-master to youtube-dl.
    src_dir = root_dir + '/youtube-dl-master'
    dest_dir = root_dir + '/youtube-dl'
    if os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    os.rename(src_dir, dest_dir)


def main():
    app = QtWidgets.QApplication(sys.argv)
    pixmap = QPixmap(root_dir + '/images/logo_bare.png')
    splash = QSplashScreen(pixmap)
    splash.show()
    app.processEvents()

    # Perform initialization steps.
    download_deps()

    # Update the python path with youtube-dl.
    sys.path.append(root_dir + '/youtube-dl')

    # Import and create our main windows.
    from mainwindow import MainWindow
    main_window = MainWindow()
    splash.hide()
    main_window.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()
