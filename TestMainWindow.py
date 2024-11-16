from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowExt import MainWindowExt

app=QApplication([])
mainWindow=QMainWindow()
myui=MainWindowExt()
myui.setupUi(mainWindow)
myui.showWindow()
app.exec()