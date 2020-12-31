from PySide2.QtWidgets import QLineEdit, QFileDialog, QDialog, QWidget, QHBoxLayout, QPushButton
from PySide2.QtGui import QMouseEvent
from PySide2.QtCore import Qt, SIGNAL, QStandardPaths


class DirChooser(QWidget):
    def __init__(self, dir=''):
        super().__init__()
        if not dir:
            dir = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation) + '/youmacro'

        self.setFixedWidth(440)
        layout = QHBoxLayout()
        layout.setMargin(0)
        self.setLayout(layout)

        self.edit = QLineEdit(dir)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setFixedWidth(400)
        self.edit.setReadOnly(True)
        layout.addWidget(self.edit)

        self.button = QPushButton('...')
        self.button.setFixedWidth(30)
        self.button.setFixedHeight(35)
        self.button.connect(self.button, SIGNAL('clicked()'), self.choose_dir)
        layout.addWidget(self.button)

    def choose_dir(self):
        dialog = QFileDialog(self, 'Download Directory', self.edit.text(), '')
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            self.edit.setText(dialog.selectedFiles()[0])

    def get_dir(self):
        return self.edit.text()

    def set_dir(self, dir):
        self.edit.setText(dir)
