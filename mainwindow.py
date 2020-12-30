import os

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from progressview import ProgressView


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("YouMacro")
        root_dir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(root_dir + '/images/logo_bare.png'))

        central_widget = QtWidgets.QWidget()
        central_layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(central_layout)

        # Add a label with info.
        label = QtWidgets.QLabel("Drag and drop links from your browser here. Links can appear as text, images or favicons.")
        central_layout.addWidget(label)

        list_view = ProgressView()
        central_layout.addWidget(list_view)

        self.setCentralWidget(central_widget)
        self.resize(800, 500)
        self.show()
