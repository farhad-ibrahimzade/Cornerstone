import time
import serial
import PySimpleGUI as gui
import tkinter as tk
from PIL import ImageTk, Image

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 9800, timeout=1)
time.sleep(2)

root = tk.Tk("Road Game Test")

mainContainer = tk.Frame(root)

lanes = []

image1 = Image.open("Images\city.png")
test = ImageTk.PhotoImage(image1.resize((300,300)))

label1 = tk.Label(image=test)

label1.place(x=10, y=10)

label = tk.Label(mainContainer, text = "Lane")
label.pack()

mainContainer.pack()

def getLanes():
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        data = string.split(",")
        lanes.append(data[0])
        output = "Lane" + str(data[1]) + ": " + data[0]
        label.configure(text = output)
        print(string)
        if int(data[1]) != 5:
            getLanes()

label.after(1, getLanes())

root.mainloop()

ser.close()
print(lanes)


#layout = [[gui.Text("Welcome to the Road Lane Game, please scan your road lanes.")], [gui.Text(str(lanes))]] #, [gui.Button("OK")]

# Create the window
#window = gui.Window("Road Lane Game", layout)

# while True:
#     event, values = window.read()
#     if event == gui.WIN_CLOSED:
#         break

# window.close()