from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QFont, QPalette, QColor

from playsound import playsound

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle('Timer')
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: #2b2b2b;")

        # Layouts
        main_layout = QVBoxLayout()
        entry_layout = QHBoxLayout()

        label_font = QFont('Arial', 12)
        button_font = QFont('Arial', 11, QFont.Bold)

        # Timer Label
        self.label = QLabel("Enter the time in seconds:")
        self.label.setFont(label_font)
        self.label.setStyleSheet("color: #ffffff;")
        entry_layout.addWidget(self.label)

        # Timer Input
        self.entry = QLineEdit()
        self.entry.setMaxLength(5)
        self.entry.setStyleSheet(
            '''QLineEdit {
                background-color: #434343;
                color: #ffffff;
                border-radius: 5px;
                padding: 5px;
            }''')
        entry_layout.addWidget(self.entry)

        # Start Button
        self.button = QPushButton("Start")
        self.button.setFont(button_font)
        self.button.setStyleSheet(
            '''QPushButton {
                background-color: #3a82e9;
                color: #ffffff;
                border-radius: 10px;
                padding: 10px 15px;
            }
               QPushButton:pressed {
                background-color: #285bb5;
            }''')
        self.button.clicked.connect(self.start_timer)

        # Countdown Display
        self.timer_label = QLabel("Press Start to begin the countdown")
        self.timer_label.setFont(label_font)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("color: #ffffff;")

        # Layout assembly
        main_layout.addLayout(entry_layout)
        main_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.timer_label)

        self.setLayout(main_layout)

        # Timer functionality
        self.seconds_left = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def start_timer(self):
        time_text = self.entry.text()
        if time_text.isdigit():
            self.seconds_left = int(time_text)
            self.timer_label.setText(str(self.seconds_left))
            self.timer.start(1000)

    def update_timer(self):
        if self.seconds_left > 0:
            self.seconds_left -= 1
            self.timer_label.setText(str(self.seconds_left))
        else:
            self.timer.stop()
            self.timer_label.setText("Time's up!")
            playsound("alarm.wav")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    timer = TimerApp()
    timer.show()
    sys.exit(app.exec_())