from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class ErrorDialog(QDialog):
    def __init__(self ,title:str ,message:str, parent=None):
        super(ErrorDialog, self).__init__(parent)
        self.setWindowTitle(title)
        layout = QVBoxLayout(self)
        label = QLabel(message)
        layout.addWidget(label)
        button = QPushButton("OK")
        button.clicked.connect(self.accept)
        layout.addWidget(button)