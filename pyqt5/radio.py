import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)    # self(=window 객체)에 radio1 만듦
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("GiftCard", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(10, 0, 300, 50)
        self.radio2.setGeometry(10, 50, 300, 50)
        self.radio3.setGeometry(10, 100, 300, 50)
        self.radio4.setGeometry(10, 150, 300, 50)
        self.radio5.setGeometry(10, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_btn = self.sender()       # sender(): signal을 보낸 widget을 return
        if radio_btn.isChecked():
            print(f"{radio_btn.text()} is selected")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()