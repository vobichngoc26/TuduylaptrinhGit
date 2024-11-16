from Func import even, odd, prime_number
from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonOK.clicked.connect(self.process_ok)
    def process_ok(self):
            try:
                n = int(self.lineEditN.text())
                resultchan = even(n)
                self.lineEditEven.setText(f"{resultchan}")
                resultle = odd(n)
                self.lineEditOdd.setText(f"{resultle}")
                resultprimenumber = prime_number(n)
                self.lineEditPrime.setText(f"{resultprimenumber}")
            except:
                self.lineEditEven.setText("Invalid Input Data")