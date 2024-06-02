import time as t
from playsound import playsound
import tkinter as tk

window = tk.Tk()	
window.title("Timer")
window.geometry("300x200")
window.configure(bg="black")

def start_timer():
    time = int(entry.get())
    for i in range(time + 1):
        label.config(text=time - i)
        window.update()
        t.sleep(1)

        if i == time:
            label.config(text="Time's up!")
            playsound("alarm.wav")


label = tk.Label(window, text="Enter the time in seconds:", bg="black", fg="white")
label.pack()


entry = tk.Entry(window, bg="black", fg="white", text="Wanna use or not? Write Yes or not:")
entry.pack()

button = tk.Button(window, text="Start", command=start_timer, bg="black", fg="white")
button.pack()


startofStart = tk.Label(window, text="Press Start to begin the countdown", bg="black", fg="white")
startofStart.pack()

window.mainloop()