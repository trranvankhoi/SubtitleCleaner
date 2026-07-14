from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("SubtitleCleaner")
        self._setup_ui()

    def _setup_ui(self) -> None:
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(QLabel("SubtitleCleaner UI placeholder"))
        self.setCentralWidget(central_widget)
