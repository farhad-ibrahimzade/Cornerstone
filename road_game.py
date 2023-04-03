import time
import serial
import PySimpleGUI as gui

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 9800, timeout=1)
time.sleep(2)

lanes = []

while True:
    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        data = string.split(",")
        lanes.append(data[0])
        print(string)
        if int(data[1]) == 5:
            break

ser.close()
print(lanes)

layout = [[gui.Text("Welcome to the Road Lane Game, here are your scanned lanes: ")], [gui.Text(lane) for lane in lanes]] #, [gui.Button("OK")]

# Create the window
window = gui.Window("Road Lane Game", layout)

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break

window.close()