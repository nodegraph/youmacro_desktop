import os
import sys
root_dir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
sys.path.append(root_dir + '/deps/youtube-dl')

from mainwindow import MainWindow
from PySide2 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
