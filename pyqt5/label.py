import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):                         # self는 window 객체
        super().__init__()
        self.setGeometry(100, 200, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #f92917;"
                            "background-color: green;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline")
        # label.setAlignment(Qt.AlignTop)           # vertically top
        # label.setAlignment(Qt.AlignBottom)        # vertically bottom
        # label.setAlignment(Qt.AlignVCenter)       # vertically center
        # label.setAlignment(Qt.AlignLeft)          # horizontally left
        # label.setAlignment(Qt.AlignRight)         # horizontally right
        # label.setAlignment(Qt.AlignHCenter)       # horizontally center

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)       # 두 값 동시에 바꾸기
        label.setAlignment(Qt.AlignCenter)          # label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()