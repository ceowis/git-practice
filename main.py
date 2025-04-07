import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1=QPushButton('Message', self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage) #버튼 클릭시 activateMessage 메소드 호출
        
        vbox = QVBoxLayout() # 수직 레이아웃 추가
        vbox.addStretch(1) #빈 공간 추가
        vbox.addWidget(self.btn1) #버튼 추가
        vbox.addStretch(1) #빈 공간 추가
        
        self.setLayout(vbox) # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정
        
        self.setWindowTitle('Simple Calculator')
        self.setWindowIcon(QIcon('calculator.png')) #아이콘 설정
        self.resize(256, 256)
        self.show()
    def activateMessage(self): # 버튼 클릭시 호출되는 메소드: 메시지 박스 출력
        QMessageBox.information(self, 'information', 'Button Clicked!') #메시지 박스 출력
        
if __name__ == '__main__':
  app = QApplication(sys.argv)
  view = Calculator()
  sys.exit(app.exec_()) 