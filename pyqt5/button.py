import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)      # 클릭될 때만 실행되어야 하므로 () 안 붙임
                                                        # on_click은 클래스(객체)의 메서드이므로 self.를 붙임.
        self.label.setGeometry(150, 300, 200, 100)      # 안 붙이면 on_click을 지역 범위나 전역 범위에서 찾는데 찾지 못해서 오류 발생.
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        print("Button Clicked!")
        self.button.setText("Ouch!!")           # button에 self를 붙이지 않으면 button은 local 객체가 되어 다른 함수에서 button을 사용 못함
        self.button.setDisabled(True)
        self.label.setText("Good Bye!!")

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()