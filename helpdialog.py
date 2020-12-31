from PySide2.QtGui import QPixmap, QImage, QFont
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QLabel, QVBoxLayout, QTextEdit
import os


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Help")
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignHCenter)


        # Create the description.
        desc_label_1 = QLabel("Drag and drop links from your browser into the main window. Links can appear as text, images or favicons.")
        desc_label_2 = QLabel("The download progress of each item will appear in the main window. When completed, it will disappear from the list.")
        desc_label_3 = QLabel("If you can't drag links from Firefox, please see: <a href='https://support.mozilla.org/en-US/questions/1295465'>https://support.mozilla.org/en-US/questions/1295465</a>")

        desc_label_1.setAlignment(Qt.AlignLeft)
        desc_label_1.setStyleSheet("font-weight: bold; color: black; font-size: 36px")
        desc_label_1.setWordWrap(True)

        desc_label_2.setAlignment(Qt.AlignLeft)
        desc_label_2.setStyleSheet("font-weight: bold; color: black; font-size: 36px")
        desc_label_2.setWordWrap(True)

        desc_label_3.setAlignment(Qt.AlignLeft)
        desc_label_3.setStyleSheet("font-weight: bold; color: black; font-size: 36px")
        desc_label_3.setWordWrap(True)

        desc_label_3.setOpenExternalLinks(True)



        # Add everything to the main layout.
        main_layout.addWidget(desc_label_1)
        main_layout.addWidget(desc_label_2)
        main_layout.addWidget(desc_label_3)
        self.setLayout(main_layout)
