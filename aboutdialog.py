from PySide2.QtGui import QPixmap, QImage, QFont
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QLabel, QVBoxLayout
import os


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("About")
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignHCenter)

        # Create the logo image.
        root_dir = os.path.dirname(os.path.realpath(__file__))
        image = QImage((root_dir + '/images/logo_bare.png'))
        pixmap = QPixmap(image.scaledToWidth(500))
        logo_label = QLabel(self)
        logo_label.setPixmap(pixmap)

        # Create the description.
        desc_label_1 = QLabel("YouMacro allows you to")
        desc_label_1.setAlignment(Qt.AlignCenter)
        desc_label_1.setStyleSheet("font-weight: bold; color: black; font-size: 36px")
        desc_label_2 = QLabel("download any online video.")
        desc_label_2.setAlignment(Qt.AlignCenter)
        desc_label_2.setStyleSheet("font-weight: bold; color: black; font-size: 36px")

        # Add everything to the main layout.
        main_layout.addWidget(desc_label_1)
        main_layout.addWidget(desc_label_2)
        main_layout.addWidget(logo_label)
        self.setLayout(main_layout)
