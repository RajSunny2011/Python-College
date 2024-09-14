import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg

class Mainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Hi!")

        # Set Layout
        self.setLayout(qtw.QVBoxLayout())

        # Label
        myLabel = qtw.QLabel("Enter your name: ")
        # Change font and size
        myLabel.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(myLabel)

        # Entry field
        myEntry = qtw.QLineEdit()
        myEntry.setObjectName("nameField")
        myEntry.setPlaceholderText("Name")
        self.layout().addWidget(myEntry)

        # Button
        myButton = qtw.QPushButton("Press to enter name",
                                   clicked = lambda: sayHello())
        self.layout().addWidget(myButton)

        self.show()
    
        def sayHello():
            myLabel.setText(f"Hi, {myEntry.text()}")
            # Clearing the entry field
            myEntry.setText("")

app = qtw.QApplication([])
mw = Mainwindow()

#Run The applicaiton
app.exec()
