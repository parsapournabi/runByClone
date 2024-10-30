from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMaximumSize(500, 500)
        main_layout = QtWidgets.QVBoxLayout(self)
        frame = QtWidgets.QFrame()
        main_layout.addWidget(frame)
        frame.setStyleSheet('''background-color: rgb(255, 0, 0);''')
        layout = QtWidgets.QVBoxLayout(frame)
        label = QtWidgets.QLabel()
        label.setText('Hello')
        label.setFont(QtGui.QFont('Arial', 25))
        label.setStyleSheet('''color: white;''')
        layout.addWidget(label)
        self.show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    windows = MainWindow()
    sys.exit(app.exec_())
