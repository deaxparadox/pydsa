import sys 

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, 
    QLineEdit, QHBoxLayout, QWidget
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QPalette

from Stack import Stack


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stack = Stack()

        self.setWindowTitle("Stack")
        # self.setFixedSize(200, 100)
        
        self.data = None


        # Enter data to stack
        self.input = QLineEdit()
        self.input.setPlaceholderText("text...")
        self.input.textChanged.connect(self.you_entered)
        

        # Button: Push enter data to stack 
        self.append = QPushButton("Append")
        self.append.clicked.connect(self.push)

        # Button: Remove last element from stack
        self.pop = QPushButton(self.getPopText())
        self.pop.clicked.connect(self.remove)

        # horizontal layout for append and pop button 
        self.buttonAppendPop = QHBoxLayout()
        self.buttonAppendPop.setSpacing(0)
        self.buttonAppendPop.addWidget(self.append)
        self.buttonAppendPop.addWidget(self.pop)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addLayout(self.buttonAppendPop)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)



    def you_entered(self, a0: str) -> str:
        self.data = a0

    def push(self) -> None:
        if self.data is None or self.data == "":
            pass 
        else:
            self.stack.push(self.data)
            self.setPopText()
            print(f"Adding: {self.data}")
            self.data = None 
            self.input.setText(self.data)

    def remove(self) -> None:
        self.stack.pop()
        print("removing the last item.")

    def getPopText(self) -> None:
        return f"Pop ({len(self.stack)})"
    def setPopText(self) -> None:
        self.pop.setText(self.getPopText())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()