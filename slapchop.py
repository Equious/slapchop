from email.message import EmailMessage
import videoCut as vc
import os
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFileDialog,
    QLineEdit,
)
from PySide6.QtCore import Qt, QCoreApplication


audio_file_name = "testoutputaudio.mp3"
current_dir = os.getcwd()
audio_file = os.path.join(current_dir, audio_file_name)

os.environ["PATH"] += os.pathsep + "C:\PATH_Programs"


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.em = EmailMessage()
        self.image = None
        self.uploaded = False
        self.file_number = 0
        self.response = ""

        self.upload_label = QLabel("No File Selected.")
        self.upload_label.setAlignment(Qt.AlignHCenter)
        self.upload_button = QPushButton("Select File to Upload")
        self.upload_button.clicked.connect(self.select_file)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignHCenter)

        self.response_label = QLabel(self.response)
        self.response_label.setAlignment(Qt.AlignHCenter)
        self.response_label.setWordWrap(True)

        self.upload_layout = QHBoxLayout()
        self.upload_layout.addWidget(self.upload_button)
        self.upload_layout.addWidget(self.upload_label)

        self.distribution_layout = QHBoxLayout()
        self.distribution_button = QPushButton("Chop Recording!")
        self.distribution_button.clicked.connect(self.submit_data)
        self.distribution_input = QLineEdit()
        self.distribution_input.setPlaceholderText("##:##, ##:##...")

        self.distribution_layout.addWidget(self.distribution_input)
        self.distribution_layout.addWidget(self.distribution_button)

        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.upload_layout)
        self.v_layout.addLayout(self.distribution_layout)

        self.setLayout(self.v_layout)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open MP3 File", ".", "MP3 Files (*.mp3)"
        )
        if file_name:
            self.mp3_file = file_name
            self.upload_label.setText(file_name)
            QCoreApplication.processEvents()

    def submit_data(self):
        print("Chopping Recording!")
        self.cutList = self.distribution_input.text().split(",")
        vc.cut(self.cutList, self.mp3_file)
        QCoreApplication.processEvents()

    def distribute(self):
        pass

    def load(self):
        pass

    def reset(self):
        pass
