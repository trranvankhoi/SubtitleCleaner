from PySide6.QtCore import QObject, Signal


class WorkerSignals(QObject):
    progress = Signal(int)
    message = Signal(str)
    finished = Signal()
    error = Signal(str)


class Worker(QObject):
    def __init__(self) -> None:
        super().__init__()
