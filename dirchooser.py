from PySide2.QtWidgets import QLineEdit, QFileDialog, QDialog, QWidget, QHBoxLayout, QPushButton
from PySide2.QtCore import Qt, SIGNAL, QStandardPaths
import os


class DirChooser(QWidget):
    def __init__(self, dir=''):
        super().__init__()
        if not dir:
            dir = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation) + '/youmacro'

        self.setFixedWidth(400)
        layout = QHBoxLayout()
        layout.setMargin(0)
        self.setLayout(layout)

        self.edit = QLineEdit(dir)
        self.edit.setAlignment(Qt.AlignRight)
        self.edit.setFixedWidth(250)
        self.edit.setReadOnly(True)
        layout.addWidget(self.edit)

        self.edit_button = QPushButton('edit')
        self.edit_button.setFixedWidth(50)
        self.edit_button.setFixedHeight(35)
        self.edit_button.connect(self.edit_button, SIGNAL('clicked()'), self.choose_dir)
        layout.addWidget(self.edit_button)

        self.view_button = QPushButton('view')
        self.view_button.setFixedWidth(50)
        self.view_button.setFixedHeight(35)
        self.view_button.connect(self.view_button, SIGNAL('clicked()'), self.open_dir)
        layout.addWidget(self.view_button)

    def choose_dir(self):
        dialog = QFileDialog(self, 'Download Directory', self.edit.text(), '*.*')
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            self.edit.setText(dialog.selectedFiles()[0])

    def open_dir(self):
        os.startfile(self.get_dir())

    def get_dir(self):
        return self.edit.text()

    def set_dir(self, dir):
        self.edit.setText(dir)
