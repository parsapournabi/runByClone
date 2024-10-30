import sys
from PyQt5.QtWidgets import QApplication
from src.gui.mainGUI import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    sys.exit(app.exec_())
