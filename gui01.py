from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self), __init__()
        self.initGUI()

    def initGIU(self):
        self.setWindowTitle('A First Window')
        self.resize(250, 150)

if __name__ == "__main__":
    app = QApplication(sys.argv) #create the application
    mywindow = MyWindow() # create an instance oy your Window
    mywindow.move(0, 8)
    mywindow.show() # tell Qt to make your window visible
    sys.exit(app.exe_())
