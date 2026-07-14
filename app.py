import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from utils.logger import configure_logging


class SubtitleCleanerApp:
    def __init__(self) -> None:
        configure_logging()
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()

    def run(self) -> int:
        self.main_window.show()
        return self.app.exec()
