"""This program will run the "Fix the road game" using a GUI powered by Tkinter.
    The program will take input from an Arduino using serial.
    Please check and define the serial port prior to running the code."""
import serial
import tkinter as tk
from PIL import ImageTk, Image

# Import the Data
from Data.data import CityCost, CityEmissions

cost_unit = "USD per 100 people"
emissions_unit = "grams of CO2 per mile per 100 people"

cost = [CityCost.boston, CityCost.london, CityCost.tokyo, CityCost.lagos, CityCost.lima]
emissions = [CityEmissions.boston, CityEmissions.london, CityEmissions.tokyo, CityEmissions.lagos, CityEmissions.lima]

# Make sure the 'COM#' is set according the Windows Device Manager
serial_port = "COM6"
ser = serial.Serial()

# Create a new window
window = tk.Tk()

#window.attributes('-fullscreen',True)

# Make the window cover the whole screen
window.geometry("%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))

# Initialize all the images
_start = Image.open("Images\city.png")
_car = Image.open("Images\car.png")
_tram = Image.open("Images\\tram.png")
_ped = Image.open("Images\ped.png")
_bike = Image.open("Images\\bike.png")
_bus = Image.open("Images\\bus.png")
_data = [Image.open(f"Images\\data{i}.png") for i in range(1,15)]

# Prepare the images for use by Tkinter
start = ImageTk.PhotoImage(_start.resize((500,500)))
car = ImageTk.PhotoImage(_car.resize((200,200)))
tram = ImageTk.PhotoImage(_tram.resize((200,200)))
ped = ImageTk.PhotoImage(_ped.resize((200,200)))
bike = ImageTk.PhotoImage(_bike.resize((200,200)))
bus = ImageTk.PhotoImage(_bus.resize((200,200)))
data = [ImageTk.PhotoImage(dat.resize((window.winfo_screenwidth(), window.winfo_screenheight()))) for dat in _data]

# Initialize the road lanes and the layout
lanes = ["Car", "Car", "Car", "Car", "Car", "Car"]
layout = []

def reset_window():
    """This function resets the window grid
    """
    window.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=0)
    window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=0)

def start_game(layout: list, ser: serial.Serial, lanes: list):
    """This function begins the game and welcomes the user.
    It asks the user to press a button when they are done scanning
    to call the display_road function

    Args:
        layout (list): layout of the window
        ser (serial.Serial): serial object
        lanes (list): list of lanes
    """
    reset_window()
    
    lanes = []
    #ser.close()
    #ser = serial.Serial(serial_port, 9800, timeout=1)

    if layout:
        clear(layout)

    label1 = tk.Label(image=start)

    label = tk.Label(text = "Welcome to the fix the Road Game")

    button = tk.Button(text="Done Scanning", command = lambda: display_road(layout, ser, lanes))

    layout = [label1, label, button]

    layout[0].grid(row=1, column=1)
    layout[1].grid(row=2, column=1)
    layout[2].grid(row=3, column=1)

    window.grid_columnconfigure((0, 2), weight=1)
    window.grid_rowconfigure((0, 4), weight=1)

def get_image(string: str) -> ImageTk.PhotoImage:
    """This function returns an image for the appropriate lane.

    Args:
        string (str): lane type

    Returns:
        ImageTk.PhotoImage: lane image
    """

    if string == "Bus":
        return bus
    
    if string == "Bike":
        return bike
    
    if string == "Car":
        return car
    
    if string == "Tram":
        return tram

    if string == "Pedestrian":
        return ped

def get_lanes(ser: serial.Serial, lanes: list) -> list:
    """This function retrieves the lanes from the Arduino via the
    serial port and returns them as a list of strings.

    Args:
        ser (serial.Serial): serial orbject
        lanes (list): list of lanes

    Returns:
        list: list of lanes
    """

    line = ser.readline()   # read a byte
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        string = string[:-2]
        data = string.split(",")
        lanes.append(data[0])
        output = "Lane" + str(data[1]) + ": " + data[0]
        print(string)
        if int(data[1]) != 5:
            get_lanes(ser, lanes)

        return lanes

def display_road(layout: list, ser: serial.Serial, lanes: list):
    """This function displays the road. It creates a row of lane names,
    a row of images and buttons for city choices as well as a button to 
    restat the game.

    Args:
        layout (list): layout of the window
        ser (serial.Serial): serial object
        lanes (list): list of lanes
    """

    reset_window()
    clear(layout)
    lanes = ["Car", "Car", "Car", "Car", "Car", "Car"]
    #lanes = get_lanes(ser, lanes)
    images = [tk.Label(image=get_image("lanes[0]")), tk.Label(image=get_image(lanes[1])), tk.Label(image=get_image(lanes[2])),
                tk.Label(image=get_image(lanes[3])), tk.Label(image=get_image(lanes[4])), tk.Label(image=get_image(lanes[5]))]
    for i,img in enumerate(images):
        img.grid(row=2, column=i+1)


    text = [tk.Label(text=lanes[0]), tk.Label(text=lanes[1]), tk.Label(text=lanes[2]), 
            tk.Label(text=lanes[3]), tk.Label(text=lanes[4]), tk.Label(text=lanes[5])]

    for i,txt in enumerate(text):
        txt.grid(row=1, column=i+1)

    buttons = [tk.Button(text="London", command = lambda: get_london(layout, lanes)), tk.Button(text="Tokyo"), tk.Button(text="Lima"), tk.Button(text="Cairo")]

    for i,btn in enumerate(buttons):
        btn.grid(row=3, column=i+1)

    restart = [tk.Button(text ="Restart", command  = lambda: start_game(layout, ser, lanes))]

    restart[0].grid(row=4)

    window.grid_columnconfigure((0, 7), weight=1)
    window.grid_rowconfigure((0, 5), weight=1)

    layout.extend(images)
    layout.extend(text)
    layout.extend(buttons)
    layout.extend(restart)

def get_london(layout: list, lanes: list):
    reset_window()
    clear(layout)

    background = tk.Label(image=data[3])
    background.place(x=0, y=0, relwidth=1, relheight=1)
    em = emissions[1]["car"]
    text = tk.Label(text = f"London car emissions are {em} {emissions_unit}")
    text.grid(row = 1, column = 1)

    window.grid_columnconfigure((0, 2), weight=1)
    window.grid_rowconfigure((0), weight=1)
    window.grid_rowconfigure((2), weight=2)


def calculate_cost(lanes: list) -> list:
    return CityEmissions

def calculate_emissions(lanes: list):
    pass

def pack(layout: list):
    """This function packs all the labels in the layout.
    This function is not needed if .grid() is used

    Args:
        layout (list): layout of the window
    """

    for label in layout:
        label.pack()

def clear(layout: list):
    """This function clears the window by destroying all labels.

    Args:
        layout (list): layout of the window
    """

    for label in layout:
        label.destroy()

# Begin the game
start_game(layout, ser, lanes)

# Main loop of the window, this function is integral to the functionality of the UI
window.mainloop()

# Close the serial port when finished
ser.close()