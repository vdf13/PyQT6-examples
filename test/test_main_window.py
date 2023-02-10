import sys

from main_window import Window


def test_basic(qtbot):
    windowT = Window()
    windowT.show()
    qtbot.addWidget(windowT)
    windowT.setWindowTitle("Qmain")
