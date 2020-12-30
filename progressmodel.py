from PySide2 import QtCore
from PySide2.QtGui import QStandardItemModel, QStandardItem
from ydlprogress import YDLProgress


class ProgressModel(QStandardItemModel):
    def __init__(self):
        super().__init__(0, 8)
        self.setHorizontalHeaderLabels(['URL', 'Filename', 'Total Bytes', 'Downloaded Bytes',
                                        'Elapsed', 'Speed', 'ETA', 'Progress'])

    def add_row(self, url):
        root_index = QtCore.QModelIndex()
        num_rows = self.rowCount(root_index)
        self.beginInsertRows(root_index, num_rows, num_rows)
        self.appendRow([QStandardItem(url),
                                QStandardItem(''),
                                QStandardItem('0'),
                                QStandardItem('0'),
                                QStandardItem('0'),
                                QStandardItem('0'),
                                QStandardItem('0'),
                                QStandardItem('0.0%')
                                ])
        self.endInsertRows()

    def remove_row(self, url):
        root_index = QtCore.QModelIndex()
        items = self.findItems(url)

        for i in items:
            row = i.index().row()
            self.beginRemoveRows(root_index, row, row)
            self.removeRow(row, root_index)
            self.endRemoveRows()

    @QtCore.Slot(str, dict)
    def update_row(self, url, obj):
        items = self.findItems(url)
        if not items:
            return
        for i in items:
            if 'youmacro_done' in obj:
                self.remove_row(url)
                continue

            row = i.index().row()
            p = YDLProgress(obj)
            self.item(row, 7).setData(p.get_percent_string(), QtCore.Qt.DisplayRole)
            self.item(row, 6).setData(p.get_eta_string(), QtCore.Qt.DisplayRole)
            self.item(row, 5).setData(p.get_speed_string(), QtCore.Qt.DisplayRole)
            self.item(row, 4).setData(p.get_elapsed(), QtCore.Qt.DisplayRole)
            self.item(row, 3).setData(p.get_downloaded_bytes(), QtCore.Qt.DisplayRole)
            self.item(row, 2).setData(p.get_total_bytes_string(), QtCore.Qt.DisplayRole)
            self.item(row, 1).setData(p.get_filename(), QtCore.Qt.DisplayRole)
