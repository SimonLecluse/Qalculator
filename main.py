from PySide2.QtWidgets import QApplication
import sys
from src.controller import Controller
from configparser import ConfigParser

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ctrl = Controller()
    sys.exit(app.exec_())