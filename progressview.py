from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

from downloadpool import DownloadPool
from progressmodel import ProgressModel


class ProgressView(QtWidgets.QTreeView):
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.download_pool = DownloadPool(settings)
        self.setModel(ProgressModel())

    def setModel(self, model):
        super().setModel(model)
        #self.header().setStretchLastSection(False)
        #self.header().resizeSection(1, 70)
        #self.header().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        #self.header().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            url = event.mimeData().text()
            clean_url = DownloadPool.clean_url(url)
            self.add_url(clean_url)
        else:
            event.ignore()

    def add_url(self, url):
        items = self.model().findItems(url, QtCore.Qt.MatchExactly)
        if not items:
            self.model().add_row(url)
            self.update()
            self.download_pool.download(url, self.model())

    def remove_url(self, url):
        items = self.model().findItems(url, QtCore.Qt.MatchExactly)
        for i in items:
            self.model().removeRow(i.row())

