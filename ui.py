import PyQt5
import main_ as m
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500,250,500,400)
        self.setWindowTitle("Live Weather")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.layout = QtWidgets.QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.input = QtWidgets.QLineEdit(self)
        self.input.setPlaceholderText("Enter City")
        self.input.move(150,40)
        self.input.resize(200,30)
        self.input.setStyleSheet("border: 2px; background-color: white")
        

        self.search = QtWidgets.QPushButton(self)
        self.search.setText("Search")
        self.search.resize(65,25)
        self.search.move(287, 75)
        self.search.setDefault(True)
        self.search.clicked.connect(self.clicked)
        self.search.setStyleSheet("background-color: white")

        self.printbox = QtWidgets.QGroupBox(self)
        self.printbox.resize(400,200)
        self.printbox.move(50, 115)
        self.printbox.setStyleSheet("border-radius: 10px; background-color: white")

        self.weather_print = QtWidgets.QLabel(self)
        self.weather_print.move(55,150)
        self.weather_print.setStyleSheet("background-color: white")
  
        self.enter = QtWidgets.QShortcut(QtGui.QKeySequence('Return'), self)
        self.enter.activated.connect(self.clicked)

    def print(self):
        if self.timing == 0:
            self.setStyleSheet("background-color: grey")
        else:
            self.setStyleSheet("background-color: skyblue")


        print(f"{self.city}, {self.region}, {self.country}\n{self.time}")
        print(f"-> Temperature: {self.temp}C\n-> Feels like: {self.feels_like}C\n-> Humidity: {self.humidity}")
        print(f"-> Skies: {self.condition}\n-> Visibility: {self.visibility}km")
        print(f"-> Wind Speed: {self.wind_speed}\n-> Wind direction: {self.wind_angle} in {self.wind_dir}")

        self.printbox.setTitle(f"{self.city}, {self.region}, {self.country}  {self.time}")
        self.weather_print.setText(f"-> Temperature: {self.temp}C\n-> Feels like: {self.feels_like}C\n-> Humidity: {self.humidity}\n-> Skies: {self.condition}\n-> Visibility: {self.visibility}km\n-> Wind Speed: {self.wind_speed}\n-> Wind direction: {self.wind_angle} in {self.wind_dir}")
        self.weather_print.adjustSize()    

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
            self.timing = self.data["current"]["is_day"]
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