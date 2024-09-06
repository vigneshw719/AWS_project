# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtCore import QThread
from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtCore import Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterSingletonType

OBJ = None
class SenderTest1(QObject):
    # valueChanged = Signal(int)
    def __init__(self, val):
        super().__init__()
        self.value = val
        OBJ.valueChanged.connect(self.setValue)

    @Slot(int)
    def setValue(self, val):
        print("Slot setValue SENDER ->", self.sender())
        self.value = val

class SenderTest2(QObject):
    valueChanged = Signal(int)
    def __init__(self):
        super().__init__()


    def createObj1(self):
        self.obj = SenderTest1(1)
    def emitSignal(self, val):
        print("Emitting signal from thread ->", self.thread())
        self.valueChanged.emit(1)

    def finished(self):
        print("Thread Finished")

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    thread1 = QThread()

    obj = SenderTest2()
    OBJ = obj
    obj.createObj1()
    obj.moveToThread(thread1)
    thread1.finished.connect(obj.finished())
    thread1.start()
    obj.emitSignal(2)

    # print("Current Value", obj.value)
    engine = QQmlApplicationEngine()
    qmlRegisterSingletonType(QUrl("Settings.qml"), "MyApp", 1, 0, "Settings")

    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
