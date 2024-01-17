import sys
from alarm_design import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from pydub import AudioSegment
from pydub.playback import play
from PyQt5.QtGui import QValidator, QIcon
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu


class CloneThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)

class Field1CustomerValidator(QValidator):
    def validate(self, input_text, pos):
        if not input_text:
            return QValidator.Acceptable, input_text, pos

        try:
            value = int(input_text)
            if 0 <= value <= 24:
                return QValidator.Acceptable, input_text, pos
        except ValueError:
            pass

        return QValidator.Invalid, input_text, pos
    
class Field2CustomerValidator(QValidator):
    def validate(self, input_text, pos):
        if not input_text:
            return QValidator.Acceptable, input_text, pos

        try:
            value = int(input_text)
            if 0 <= value <= 60:
                return QValidator.Acceptable, input_text, pos
        except ValueError:
            pass

        return QValidator.Invalid, input_text, pos
    
class Mytimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.thread1 = CloneThread()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.curr_time = QtCore.QTime(0, 0, 0)
        self.Reach_timer = self.curr_time
        self.thread1.signal.connect(self.thread1.terminate)
        self.time = QtCore.QTime(self.curr_time)
        self.ui.pushButton.clicked.connect(self.saveData)
        self.setWindowIcon(QIcon('images/alarm.png'))

        # Connect each checkbox's clicked signal to the slot function
        checkboxes = [
            self.ui.checkBox_5, self.ui.checkBox, self.ui.checkBox_6,
            self.ui.checkBox_7, self.ui.checkBox_2, self.ui.checkBox_3, self.ui.checkBox_4
        ]
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # Set an additional property for each checkbox
        for i, checkbox in enumerate(checkboxes):
            checkbox.setProperty("day", days[i])

        self.ui.lineEdit.setValidator(Field1CustomerValidator())
        self.ui.lineEdit_2.setValidator(Field2CustomerValidator())

    def saveData(self):
        # Retrieve data from input fields
        input_field1_data = self.ui.lineEdit.text()
        input_field2_data = self.ui.lineEdit_2.text()

        # Retrieve selected checkbox additional values
        checkboxes = [
            self.ui.checkBox_5, self.ui.checkBox, self.ui.checkBox_6,
            self.ui.checkBox_7, self.ui.checkBox_2, self.ui.checkBox_3, self.ui.checkBox_4
        ]

        selected_checkbox_values = [
            checkbox.property("day") for checkbox in checkboxes if checkbox.isChecked()
        ]

        current_date = datetime.now().date()
        time_str = f"{input_field1_data}:{input_field2_data}"
        alarms = []
        for x in selected_checkbox_values:

            # Map day string to corresponding weekday integer (0 for Monday, 1 for Tuesday, and so on)
            weekday_mapping = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
            weekday = weekday_mapping.get(x)

            # Create a datetime object with the current date, given time, and day
            timestamp = datetime.combine(current_date, datetime.strptime(time_str, "%H:%M").time()) + timedelta(days=(weekday - datetime.today().weekday()))

            # Convert the datetime object to a timestamp
            minutes_left= (timestamp - datetime.now()).total_seconds() / 60
            if minutes_left < 0:
                minutes_left += 7 * 24 * 60
            alarms.append((minutes_left))
        alarms.sort()
        for i in range(len(alarms)):
            current_minutes = alarms[i]
            next_minutes = alarms[i + 1] if i + 1 < len(alarms) else None
            if next_minutes is None:
                break
            alarms[i + 1] = next_minutes - current_minutes

        # Change the alarm label
        self.ui.label_5.setText("Alarm set for " + ", ".join(selected_checkbox_values) + " at " + time_str + ".")

        for minutes in alarms:
            self.startAlarmTimer(minutes)

    def startAlarmTimer(self, minutes):
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(lambda: self.handleAlarmTimer(minutes))
        
        # Convert minutes to milliseconds
        milliseconds = int(minutes * 60 * 1000)
        # Start the timer
        timer.start(milliseconds)
    
    def handleAlarmTimer(self, minutes):
        self.ui.label_5.setText("Alarm!")
        self.playAlarmSound()
        self.showNotification()
    
    def showNotification(self):
        notification_title = "Alarm!"
        notification_message = "It's time for your alarm."

        # Create a system tray icon
        tray_icon = QSystemTrayIcon(self)
        tray_icon.setIcon(self.windowIcon())
        tray_icon.setToolTip("MyTimerApp")

        # Create a context menu for the system tray icon
        menu = QMenu(self)
        menu.addAction("You Have a new Alarm!", self.handleNotificationClick)
        tray_icon.setContextMenu(menu)
        tray_icon.setVisible(True)

        # Show the notification
        tray_icon.show()
        tray_icon.showMessage(notification_title, notification_message, QSystemTrayIcon.Information, 5000)

    def handleNotificationClick(self):
        # Handle the click action (e.g., bring the main window to the front)
        self.showNormal()
    
    def playAlarmSound(self):
        alarm_sound = AudioSegment.from_file("audio/sound.wav", format="mp3")
        play(alarm_sound[:5000])
        self.ui.label_5.setText("Please set next alarm")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mytimer()
    w.show()
    sys.exit(app.exec_())