# hello.py

import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# Create an instance of QApplication
app = QApplication([])


# Create the application GUI
window = QWidget()
window.setWindowTitle("PyQT Application")
window.setGeometry(100,100,280,80)
helloMsg = QLabel("<h1>Hello World!</h1>", parent=window)
helloMsg.move(60, 15)

# Show the application GUI
window.show()

# Run the application's event loop
sys.exit(app.exec())

