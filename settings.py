from PySide2.QtCore import Qt, QSettings, QStandardPaths
from PySide2.QtWidgets import QWidget, QHBoxLayout, QComboBox, QLabel, QCheckBox
from dirchooser import DirChooser


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings('YouMacro', 'download')
        self.video_res_combo = None
        self.audio_only_checkbox = None
        self.download_dir_chooser = None
        self.build()
        self.load_settings()

    def build(self):
        # Add a label with info.
        settings_layout = QHBoxLayout()
        settings_layout.setMargin(0)
        self.setLayout(settings_layout)

        self.video_res_combo = QComboBox()
        self.video_res_combo.addItems(['4320', '2160', '1440', '1080', '720', '480', '360', '240'])
        label = QLabel('video_res')
        label.setAlignment(Qt.AlignVCenter)
        settings_layout.addWidget(label)
        settings_layout.addWidget(self.video_res_combo)

        self.audio_only_checkbox = QCheckBox()
        label = QLabel('audio_only')
        label.setAlignment(Qt.AlignVCenter)
        settings_layout.addWidget(label)
        settings_layout.addWidget(self.audio_only_checkbox)

        self.download_dir_chooser = DirChooser(self.settings.value('download_dir', ''))
        label = QLabel('download_dir')
        label.setAlignment(Qt.AlignVCenter)
        settings_layout.addWidget(label)
        settings_layout.addWidget(self.download_dir_chooser)
        settings_layout.addStretch()

    def load_settings(self):
        default_download_dir = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation) + '/youmacro'
        self.video_res_combo.setCurrentText(str(self.settings.value('video_res', 4320, type=int)))
        self.audio_only_checkbox.setChecked(self.settings.value('audio_only', False, type=bool))
        self.download_dir_chooser.set_dir(self.settings.value('download_dir', default_download_dir, type=str))

    def save_settings(self):
        self.settings.setValue('video_res', int(self.video_res_combo.currentText()))
        self.settings.setValue('audio_only', self.audio_only_checkbox.isChecked())
        self.settings.setValue('download_dir', self.download_dir_chooser.get_dir())

    def get_download_dir(self):
        return self.download_dir_chooser.get_dir()

    def get_audio_only(self):
        return self.audio_only_checkbox.isChecked()

    def get_video_res(self):
        return int(self.video_res_combo.currentText())
