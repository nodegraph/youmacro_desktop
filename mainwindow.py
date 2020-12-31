import os

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from progressview import ProgressView
from aboutdialog import AboutDialog
from helpdialog import HelpDialog
from settings import Settings


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("YouMacro")
        self.about_dialog = AboutDialog()
        self.help_dialog = HelpDialog()
        self.settings = Settings()
        self.list_view = ProgressView(self.settings)

        root_dir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(root_dir + '/images/logo_bare.png'))

        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)
        central_layout.addWidget(self.settings)
        central_layout.addWidget(self.list_view)

        self.setCentralWidget(central_widget)
        self.resize(1024, 800)

    def closeEvent(self, event):
        # Save current settings
        self.settings.save_settings()
        event.accept()
