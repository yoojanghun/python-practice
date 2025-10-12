import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 700, 700)

        label = QLabel(self)
        label.setGeometry(0, 0, 500, 250)

        pixmap = QPixmap("chicken.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        # label.setGeometry(self.width() - label.width(),         # bottom right corner
        #                   self.height() - label.height(),
        #                   label.width(),
        #                   label.height())

        label.setGeometry((self.width() - label.width()) // 2,    # Center
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()