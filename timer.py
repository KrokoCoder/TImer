import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTabWidget, QGridLayout, QListWidget
from PySide2.QtCore import Qt, QTimer, QTime, QDateTime
from PySide2.QtGui import QFont, QColor, QPalette
from playsound import playsound

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle('Timer Application')
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #2b2b2b;")

        # Main Layout
        main_layout = QVBoxLayout()

        # Tab Widget
        self.tabs = QTabWidget()
        self.tabs.addTab(self.create_timer_tab(), "Timer")
        self.tabs.addTab(self.create_stopwatch_tab(), "Stopwatch")
        self.tabs.addTab(self.create_alarms_tab(), "Alarms")
        self.tabs.addTab(self.create_clock_tab(), "Clock")

        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def create_timer_tab(self):
        timer_widget = QWidget()
        timer_layout = QVBoxLayout()
        entry_layout = QHBoxLayout()

        label_font = QFont('Arial', 12)
        button_font = QFont('Arial', 11, QFont.Bold)

        # Timer Label
        self.timer_label = QLabel("Enter the time in seconds:")
        self.timer_label.setFont(label_font)
        self.timer_label.setStyleSheet("color: #ffffff;")
        entry_layout.addWidget(self.timer_label)

        # Timer Input
        self.timer_entry = QLineEdit()
        self.timer_entry.setMaxLength(5)
        self.timer_entry.setStyleSheet(
            '''QLineEdit {
                background-color: #434343;
                color: #ffffff;
                border-radius: 5px;
                padding: 5px;
            }''')
        entry_layout.addWidget(self.timer_entry)

        # Start Button
        self.start_button = QPushButton("Start")
        self.start_button.setFont(button_font)
        self.start_button.setStyleSheet(
            '''QPushButton {
                background-color: #3a82e9;
                color: #ffffff;
                border-radius: 10px;
                padding: 10px 15px;
            }
               QPushButton:pressed {
                background-color: #285bb5;
            }''')
        self.start_button.clicked.connect(self.start_timer)

        # Timer Display
        self.timer_display = QLabel("Press Start to begin the countdown")
        self.timer_display.setFont(label_font)
        self.timer_display.setAlignment(Qt.AlignCenter)
        self.timer_display.setStyleSheet("color: #ffffff;")

        # Layout assembly
        timer_layout.addLayout(entry_layout)
        timer_layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        timer_layout.addWidget(self.timer_display)

        # Timer functionality
        self.timer_seconds_left = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        timer_widget.setLayout(timer_layout)
        return timer_widget

    def start_timer(self):
        time_text = self.timer_entry.text()
        if time_text.isdigit():
            self.timer_seconds_left = int(time_text)
            self.timer_display.setText(str(self.timer_seconds_left))
            self.timer.start(1000)

    def update_timer(self):
        if self.timer_seconds_left > 0:
            self.timer_seconds_left -= 1
            self.timer_display.setText(str(self.timer_seconds_left))
        else:
            self.timer.stop()
            self.timer_display.setText("Time's up!")
            playsound("alarm.wav")

    def create_stopwatch_tab(self):
        stopwatch_widget = QWidget()
        stopwatch_layout = QVBoxLayout()

        label_font = QFont('Arial', 12)
        button_font = QFont('Arial', 11, QFont.Bold)

        # Stopwatch Display
        self.stopwatch_display = QLabel("00:00:00")
        self.stopwatch_display.setFont(label_font)
        self.stopwatch_display.setAlignment(Qt.AlignCenter)
        self.stopwatch_display.setStyleSheet("color: #ffffff;")

        # Stopwatch Buttons
        button_layout = QHBoxLayout()
        self.stopwatch_start_button = QPushButton("Start")
        self.stopwatch_start_button.setFont(button_font)
        self.stopwatch_start_button.setStyleSheet(
            '''QPushButton {
                background-color: #3a82e9;
                color: #ffffff;
                border-radius: 10px;
                padding: 10px 15px;
            }
               QPushButton:pressed {
                background-color: #285bb5;
            }''')
        self.stopwatch_start_button.clicked.connect(self.start_stopwatch)
        
        self.stopwatch_pause_button = QPushButton("Pause")
        self.stopwatch_pause_button.setFont(button_font)
        self.stopwatch_pause_button.setStyleSheet(
            '''QPushButton {
                background-color: #3a82e9;
                color: #ffffff;
                border-radius: 10px;
                padding: 10px 15px;
            }
               QPushButton:pressed {
                background-color: #285bb5;
            }''')
        self.stopwatch_pause_button.clicked.connect(self.pause_stopwatch)

        self.stopwatch_reset_button = QPushButton("Reset")
        self.stopwatch_reset_button.setFont(button_font)
        self.stopwatch_reset_button.setStyleSheet(
            '''QPushButton {
                background-color: #3a82e9;
                color: #ffffff;
                border-radius: 10px;
                padding: 10px 15px;
            }
               QPushButton:pressed {
                background-color: #285bb5;
            }''')
        self.stopwatch_reset_button.clicked.connect(self.reset_stopwatch)

        button_layout.addWidget(self.stopwatch_start_button)
        button_layout.addWidget(self.stopwatch_pause_button)
        button_layout.addWidget(self.stopwatch_reset_button)

        # Stopwatch functionality
        self.stopwatch_timer = QTimer()
        self.stopwatch_time = QTime(0, 0, 0)
        self.stopwatch_timer.timeout.connect(self.update_stopwatch)

        stopwatch_layout.addWidget(self.stopwatch_display)
        stopwatch_layout.addLayout(button_layout)

        stopwatch_widget.setLayout(stopwatch_layout)
        return stopwatch_widget

    def start_stopwatch(self):
        self.stopwatch_timer.start(1000)
        self.stopwatch_start_button.setText("Continue")

    def pause_stopwatch(self):
        self.stopwatch_timer.stop()

    def reset_stopwatch(self):
        self.stopwatch_timer.stop()
        self.stopwatch_time = QTime(0, 0, 0)
        self.stopwatch_display.setText(self.stopwatch_time.toString("hh:mm:ss"))
        self.stopwatch_start_button.setText("Start")

    def update_stopwatch(self):
        self.stopwatch_time = self.stopwatch_time.addSecs(1)
        self.stopwatch_display.setText(self.stopwatch_time.toString("hh:mm:ss"))

    def create_alarms_tab(self):
        alarms_widget = QWidget()
        alarms_layout = QVBoxLayout()
        button_font = QFont('Arial', 11, QFont.Bold)

        # Alarms List
        self.alarms_list = QListWidget()
        self.alarms_list.setStyleSheet(
            '''QListWidget {
                background-color: #434343;
                color: #ffffff;
                border-radius: 5px;
                padding: 5px;
            }''')
        alarms_layout.addWidget(self.alarms_list)

        # Alarm Entry
        entry_layout = QHBoxLayout()
        self.alarm_entry = QLineEdit()
        self.alarm_entry.setPlaceholderText("HH:MM")
        self.alarm_entry.setStyleSheet(
            '''QLineEdit {
                background-color: #434343;
                color: #ffffff;
                border-radius: 5px;
                padding: 5px;
            }''')
        entry_layout.addWidget(self.alarm_entry)

        # Add Alarm Button
        self.add_alarm_button = QPushButton("Add Alarm")
        self.add_alarm_button.setFont(button_font)
        self.add_alarm_button.setStyleSheet(
            '''QPushButton {
                background-color: #3a82e9;
                color: #ffffff;
                border-radius: 10px;
                padding: 10px 15px;
            }
               QPushButton:pressed {
                background-color: #285bb5;
            }''')
        self.add_alarm_button.clicked.connect(self.add_alarm)
        entry_layout.addWidget(self.add_alarm_button)

        # Alarm functionality
        self.alarms = []
        self.alarm_timer = QTimer()
        self.alarm_timer.timeout.connect(self.check_alarms)
        self.alarm_timer.start(1000)

        alarms_layout.addLayout(entry_layout)

        alarms_widget.setLayout(alarms_layout)
        return alarms_widget

    def add_alarm(self):
        alarm_time = self.alarm_entry.text()
        if QTime.fromString(alarm_time, "HH:mm").isValid():
            self.alarms.append(alarm_time)
            self.alarms_list.addItem(alarm_time)
            self.alarm_entry.clear()

    def check_alarms(self):
        current_time = QTime.currentTime().toString("HH:mm")
        if current_time in self.alarms:
            self.alarms.remove(current_time)
            for i in range(self.alarms_list.count()):
                if self.alarms_list.item(i).text() == current_time:
                    self.alarms_list.takeItem(i)
                    break
            playsound("alarm.wav")

    def create_clock_tab(self):
        clock_widget = QWidget()
        clock_layout = QVBoxLayout()

        label_font = QFont('Arial', 12)

        # Clock Display
        self.clock_display = QLabel()
        self.clock_display.setFont(label_font)
        self.clock_display.setAlignment(Qt.AlignCenter)
        self.clock_display.setStyleSheet("color: #ffffff;")
        
        # Timezone Display
        self.timezone_display = QLabel()
        self.timezone_display.setFont(label_font)
        self.timezone_display.setAlignment(Qt.AlignCenter)
        self.timezone_display.setStyleSheet("color: #ffffff;")
        
        self.update_clock()
        
        # Timer to update clock every second
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)

        clock_layout.addWidget(self.clock_display)
        clock_layout.addWidget(self.timezone_display)

        clock_widget.setLayout(clock_layout)
        return clock_widget

    def update_clock(self):
        current_time = QDateTime.currentDateTime().toString("dddd, MMMM d, yyyy h:mm:ss AP")
        self.clock_display.setText(current_time)
        
        # Update the timezone
        timezone_time = QDateTime.currentDateTime().toString("h:mm:ss AP")
        self.timezone_display.setText(f"Tokyo Time: {timezone_time}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())
