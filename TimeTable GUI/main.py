# from graphicalUserInterface import TimeTableApp
# from graphicalUserInterface import Ui
# from PySide6 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

""" if __name__ == "__main__":
    TimeTableApp().run() """