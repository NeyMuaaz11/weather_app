import PyQt5
import main_ as m
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500,250,600,600)
        self.setWindowTitle("Live Weather")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.layout = QtWidgets.QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.input = QtWidgets.QLineEdit(self)
        self.input.setPlaceholderText("Enter City")
        self.input.move(200,40)
        self.input.resize(200,30)
        

        self.search = QtWidgets.QPushButton(self)
        self.search.setText("Search")
        self.search.resize(70,32)
        self.search.move(332, 70)
        self.search.setDefault(True)
        self.search.clicked.connect(self.clicked)

        self.printbox = QtWidgets.QGroupBox(self)
        self.printbox.resize(320,200)
        self.printbox.move(150, 120)

        self.temp_print = QtWidgets.QLabel(self)
        self.conditions_print = QtWidgets.QLabel(self)

        self.enter = QtWidgets.QShortcut(QtGui.QKeySequence('Return'), self)
        self.enter.activated.connect(self.clicked)

    def print(self):
        print(f"{self.city}, {self.region}, {self.country}\n{self.time}")
        print(f"-> Temperature: {self.temp}C\n-> Feels like: {self.feels_like}C\n-> Humidity: {self.humidity}")
        print(f"-> Skies: {self.condition}\n-> Visibility: {self.visibility}km")
        print(f"-> Wind Speed: {self.wind_speed}\n-> Wind direction: {self.wind_angle} in {self.wind_dir}")

        self.printbox.setTitle(f"{self.city}, {self.region}, {self.country}         {self.time}")
        self.temp_print.setText(f"-> Temperature: {self.temp}C\n-> Feels like: {self.feels_like}C\n-> Humidity: {self.humidity}\n-> Skies: {self.condition}\n-> Visibility: {self.visibility}km\n-> Wind Speed: {self.wind_speed}\n-> Wind direction: {self.wind_angle} in {self.wind_dir}")
        self.temp_print.move(155,150)
        self.temp_print.adjustSize()    

    def clicked(self):
        self.data = m.get_weather(self.input.text())
        try:
            self.city = self.data['location']['name']
            self.region = self.data['location']['region']
            self.country = self.data['location']['country']
            self.time = self.data['location']['localtime']
            self.temp = self.data['current']['temp_c']
            self.feels_like = self.data['current']['feelslike_c']
            self.humidity = self.data['current']['humidity']
            self.wind_dir = self.data['current']['wind_dir']
            self.wind_speed = self.data['current']['wind_kph']
            self.wind_angle = self.data['current']['wind_degree']
            self.condition = self.data['current']['condition']['text']
            self.visibility = self.data['current']['vis_km']
            self.print()
            self.input.clear()
        except KeyError:
            print("Invalid city! Please enter a valid city")
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle("Invalid City!")
            msg.setText("Please enter a valid city.")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            x = msg.exec_()
            
        



def window():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

window()