import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        self.button1.setObjectName("btn1")
        self.button2.setObjectName("btn2")
        self.button3.setObjectName("btn3")

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid black;
                border-radius: 15px;
            }
            QPushButton#btn1 {
                background-color: hsl(0, 100%, 64%);
            }
            QPushButton#btn2 {
                background-color: hsl(122, 100%, 64%);
            }
            QPushButton#btn3 {
                background-color: hsl(204, 100%, 64%);
            }
            QPushButton#btn1:hover {
                background-color: hsl(0, 100%, 84%);
            }
            QPushButton#btn2:hover {
                background-color: hsl(122, 100%, 84%);
            }
            QPushButton#btn3:hover {
                background-color: hsl(204, 100%, 84%);
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()