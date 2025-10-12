import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

# QtWidgets: PyQt5 라이브러리 안 widget관련 모듈
# QApplication: PyQt 프로그램 전체를 관리하는 클래스
#               PyQt 프로그램은 반드시 하나의 QApplication 객체를 가짐
#               event loop를 돌면서 버튼 클릭, 마우스 이동, 창 닫기 같은 사용자 입력 처리
# QMainWindow: 프로그램 기본 창(window) 역할을 하는 클래스
#              메뉴바, 상태바, 중앙 위젯 등을 포함하는 윈도우 구조 제공
# QtGui: 그래픽 관련 기능(아이콘, 폰트, 색상, 이미지 등)을 다루는 모듈
# QIcon: 아이콘 이미지를 다루는 객체를 만들 때 사용하는 클래스

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool First GUI")
        self.setGeometry(200, 100, 500, 300)        # x, y, width, height
        self.setWindowIcon(QIcon("chicken.jpg"))

def main():
    app = QApplication(sys.argv)        # sys.argv: 명령줄에서 프로그램 실행할 때 전달되는 인자를 저장하는 리스트
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())               # app.exec_(): app 객체 실행과 이벤트 루프 시작. 프로그램이 끝나면 자동으로 종료 코드 반환

if __name__ == "__main__":
    main()