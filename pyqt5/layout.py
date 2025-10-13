import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()                  # window 중앙에 올릴 빈 위젯 생성
        self.setCentralWidget(central_widget)       # window 객체 중앙에 central_widget 설정

        label1 = QLabel("#1")                       # label1 객체 생성
        label2 = QLabel("#2")                       # window 객체에 직접 올리는 것이 아니므로 self 없어도 됨
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        label1.setStyleSheet("background-color: red;")          # 객체 디자인
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        # vbox = QVBoxLayout()              # QHBoxLayout() 사용 가능
        #
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        #
        # central_widget.setLayout(vbox)

        grid = QGridLayout()                # grid 레이아웃 생성

        grid.addWidget(label1, 0, 0)        # grid 레이아웃에 label 추가
        grid.addWidget(label2, 0, 1)        # row = 0, col = 1
        grid.addWidget(label3, 1, 0)        # row = 1, col = 0
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 2)

        central_widget.setLayout(grid)      # 위젯에 레이아웃 적용

        # label을 grid 레이아웃에 추가하고 그 레이아웃을 central_widget에 추가함
        # 그리고 central_widget을 window 객체의 중심 위젯으로 설정

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())       # app.exec_()는 app 객체의 이벤트 루프를 실행시킴

if __name__ == '__main__':
    main()