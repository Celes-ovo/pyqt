# 기본 파트
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 버튼 부분을 위해 필요한 파트
from PyQt5.QtWidgets import QPushButton, QToolTip, QMessageBox
from PyQt5.QtGui import QFont

# 메뉴바를 만들기 위해 필요한 파트
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # 폰트 지정
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Push Image convert button to start image convert')

        # 버튼을 만드는 부분
        button = QPushButton('Image convert', self)
        button.setToolTip('Push Image convert button to start image convert')
        button.move(50, 50)
        button.resize(button.sizeHint())

        button.clicked.connect(self.imageconvert)

    def imageconvert(self):
        # print('hello world!')
        QMessageBox.about(self, "message", "clicked")

        self.setWindowTitle('Test')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()

    sys.exit(app.exec_())