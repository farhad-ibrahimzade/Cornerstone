import time
import serial
from serialtest import MySerial
from tkinter import *

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 9800, timeout=1)
#time.sleep(2)

serry = MySerial(ser)


def update(counter, labels: list):
    output = serry.getLanes()
    if output != "Done" and output != None:
        if output == "":
            update(counter, labels)

        else:
            labels[counter].configure(text = (output)) #"Lane " + str(counter+1) + ": " + 
            update(counter+1, labels)

    else:
        return


root = Tk()
mainContainer = Frame(root)
lane1 = Label(mainContainer, text="Lane 1: ")
lane2 = Label(mainContainer, text="Lane 2: ")
lane3 = Label(mainContainer, text="Lane 3: ")
lane4 = Label(mainContainer, text="Lane 4: ")
lane5 = Label(mainContainer, text="Lane 5: ")
lane6 = Label(mainContainer, text="Lane 6: ")
labels = [lane1, lane2, lane3, lane4, lane5, lane6]
for lane in labels:
    lane.pack()
mainContainer.pack()
mainContainer.after(1, update(0, labels))
root.title("Timed event")
root.mainloop()