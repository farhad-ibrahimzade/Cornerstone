"""This program will run the "Fix the road game" using a GUI powered by Tkinter.
    The program will take input from an Arduino using serial.
    Please check and define the serial port prior to running the code."""
import serial
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from Data.cities import Cities
# Import the Data
from Data.data import CityCost, CityEmissions, RoadCapacity

cost_unit = "USD per 100 people"
emissions_unit = "g CO2/mi per 100 people"
capacity_unit = "people per hour"

cost = [CityCost.boston, CityCost.london, CityCost.tokyo, CityCost.lagos, CityCost.lima]
emissions = [CityEmissions.boston, CityEmissions.london, CityEmissions.tokyo, CityEmissions.lagos, CityEmissions.lima]

capacity_range = np.linspace(1000, 15000, 100)
cost_range = np.linspace(0, 60000000, 100)
emissions_range = np.linspace(0, 18149, 100) #18149

# Make sure the 'COM#' is set according the Windows Device Manager
serial_port = "COM3"
ser = serial.Serial()

# Create a new window
window = tk.Tk()

#window.attributes('-fullscreen',True)

# Make the window cover the whole screen
window.geometry("%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))

style = ttk.Style()
style.theme_use('clam') 
# Self test for each subject,'winnative','clam','alt','default','classic' Test successful. 
# windows theme:('winnative','clam','alt','default','classic','vista','xpnative')

style.configure("1.Horizontal.TProgressbar", troughcolor ='gray', background='red') 
style.configure("2.Horizontal.TProgressbar", troughcolor ='gray', background='yellow')
style.configure("3.Horizontal.TProgressbar", troughcolor ='gray', background='green')

# Initialize all the images
_start = Image.open("Images\city.png")
_car = Image.open("Images\car.png")
_tram = Image.open("Images\\tram.png")
_ped = Image.open("Images\ped.png")
_bike = Image.open("Images\\bike.png")
_bus = Image.open("Images\\bus.png")
_data = [Image.open(f"Images\\data{i}.png") for i in range(1,15)]
_road = Image.open("Images\\road.png")

# Prepare the images for use by Tkinter
start = ImageTk.PhotoImage(_start.resize((500,500)))
car = ImageTk.PhotoImage(_car.resize((240,240)))
tram = ImageTk.PhotoImage(_tram.resize((240,240)))
ped = ImageTk.PhotoImage(_ped.resize((240,240)))
bike = ImageTk.PhotoImage(_bike.resize((240,240)))
bus = ImageTk.PhotoImage(_bus.resize((240,240)))
data = [ImageTk.PhotoImage(dat.resize((window.winfo_screenwidth(), window.winfo_screenheight()))) for dat in _data]
road = ImageTk.PhotoImage(_road.resize((window.winfo_screenwidth(), window.winfo_screenheight())))

# Initialize the road lanes and the layout
lanes = []
layout = []

def reset_window():
    """This function resets the window grid
    """
    window.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), weight=0)
    window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), weight=0)

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
    ser.close() #TODO: remove once done testing
    ser = serial.Serial(serial_port, 9800, timeout=1)

    clear(layout)

    background = tk.Label(image=data[5])
    background.place(x=0, y=0, relwidth=1, relheight=1)

    text = [tk.Label(text = "Welcome to the fix the Road Game", font=("Arial", 22)),
                tk.Label(text = "Scan and place your lanes on the road", font=("Arial", 22)),
                tk.Label(text = "Please click the button below when done scanning", font=("Arial", 22))]

    button = tk.Button(text="Done Scanning", command = lambda: display_road(layout, ser, lanes), font=("Arial", 22))

    text[0].config(bg= "white", fg= "black")
    text[1].config(bg= "white", fg= "black")
    text[2].config(bg= "white", fg= "black")

    text[0].grid(row=1, column=1)
    text[1].grid(row=2, column=1)
    text[2].grid(row=3, column=1)
    button.grid(row=7, column=1)

    layout.append(background)
    layout.extend(text)
    layout.append(button)

    window.grid_columnconfigure((0, 2), weight=1)
    window.grid_rowconfigure((4, 5, 6), weight=1)
    window.grid_rowconfigure((0, 8), weight=2) 

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

    road_background = tk.Label(image=road)
    road_background.place(x=0, y=0, relwidth=1, relheight=1)

    #lanes = ["Pedestrian", "Bike", "Car", "Tram", "Bike", "Pedestrian"]
    if len(lanes) == 0:
        lanes = get_lanes(ser, lanes) #TODO: fix if lanes not empty

    top_text = tk.Label(text = "Thank you for scanning, here is your road: ", font=("Arial", 25))

    top_text.config(bg= "#747473", fg= "white")

    top_text.grid(row = 1, column = 2, columnspan = 4)

    window.grid_rowconfigure((2), weight=1)

    # text = [tk.Label(text=lanes[0], font = ("Arial", 15)), tk.Label(text=lanes[1], font = ("Arial", 15)), tk.Label(text=lanes[2], font = ("Arial", 15)), 
    #         tk.Label(text=lanes[3], font = ("Arial", 15)), tk.Label(text=lanes[4], font = ("Arial", 15)), tk.Label(text=lanes[5], font = ("Arial", 15))]

    # for i,txt in enumerate(text):
    #     txt.config(bg= "#747473", fg= "white")
    #     txt.grid(row=3, column=i+1)

    window.grid_rowconfigure((4), weight=1)

    images = [tk.Label(image=get_image(lanes[0])), tk.Label(image=get_image(lanes[1])), tk.Label(image=get_image(lanes[2])),
                tk.Label(image=get_image(lanes[3])), tk.Label(image=get_image(lanes[4])), tk.Label(image=get_image(lanes[5]))]
    for i,img in enumerate(images):
        img.config(bg= "#747473", fg= "white")
        img.grid(row=5, column=i+1)

    window.grid_rowconfigure((6), weight=1)

    display_data = [tk.Label(text = f"Average emissions: {road_emissions(lanes):,} {emissions_unit}", font=("Arial", 15)),
                    tk.Label(text = f"Average capacity: {road_capacity(lanes):,} {capacity_unit}", font=("Arial", 15)),
                    tk.Label(text = f"Average cost: {road_cost(lanes):,} {cost_unit}", font=("Arial", 15))]

    for dat in display_data:
        dat.config(bg= "#747473", fg= "white")

    display_data[0].grid(row = 7, column= 1, columnspan= 2)
    display_data[1].grid(row = 7, column= 3, columnspan= 2)
    display_data[2].grid(row = 7, column= 5, columnspan= 2)

    window.grid_rowconfigure((8), weight=1)

    scores = [tk.Label(text=f"You scored {get_emissions_score(lanes)}% in emissions", font = ("Arial", 15)), 
              tk.Label(text=f"You scored {get_capacity_score(lanes)}% in capacity", font = ("Arial", 15)), 
              tk.Label(text=f"You scored {get_cost_score(lanes)}% in cost", font = ("Arial", 15))]

    for i,score in enumerate(scores):
        score.config(bg= "#747473", fg= "white")

    scores[0].grid(row = 9, column= 1, columnspan= 2)
    scores[1].grid(row = 9, column= 3, columnspan= 2)
    scores[2].grid(row = 9, column= 5, columnspan= 2)
    
    score_bars = [ttk.Progressbar(window, style= get_progress_score(get_emissions_score(lanes)), orient = "horizontal", length = 200, mode = "determinate"), 
                ttk.Progressbar(window, style= get_progress_score(get_capacity_score(lanes)), orient = "horizontal", length = 200, mode = "determinate"),
                ttk.Progressbar(window, style= get_progress_score(get_cost_score(lanes)), orient = "horizontal", length = 200, mode = "determinate")]

    score_bars[0]["value"] = get_emissions_score(lanes)
    score_bars[1]["value"] = get_capacity_score(lanes)
    score_bars[2]["value"] = get_cost_score(lanes)

    score_bars[0].grid(row = 10, column= 1, columnspan= 2)
    score_bars[1].grid(row = 10, column= 3, columnspan= 2)
    score_bars[2].grid(row = 10, column= 5, columnspan= 2)

    window.grid_rowconfigure((11), weight=1)

    globe_text = tk.Label(text = "See how your road performs across the globe:", font=("Arial", 17))

    globe_text.config(bg= "#747473", fg= "white")

    globe_text.grid(row = 12, column=3, columnspan=2)

    window.grid_rowconfigure((13), weight=1)

    city_buttons = [tk.Button(text ="Restart game", font=("Arial", 20), command  = lambda: start_game(layout, ser, lanes)),
                    tk.Button(text="Boston", font=("Arial", 20), command = lambda: get_boston(layout, ser, lanes)),
                    tk.Button(text="London", font=("Arial", 20), command = lambda: get_london(layout, ser, lanes)),
                    tk.Button(text="Tokyo", font=("Arial", 20),  command = lambda: get_tokyo(layout, ser, lanes)), 
                    tk.Button(text="Lagos", font=("Arial", 20), command = lambda: get_lagos(layout, ser, lanes)),
                    tk.Button(text="Lima", font=("Arial", 20), command = lambda: get_lima(layout, ser, lanes))]

    for i,btn in enumerate(city_buttons):
        btn.config(bg= "#747473", fg= "white")
        btn.grid(row=14, column=i+1)

    window.grid_columnconfigure((0, 7), weight=3)
    window.grid_rowconfigure((0, 15), weight=3)

    layout.append(road_background)
    layout.append(top_text)
    layout.extend(images)
    layout.extend(display_data)
    layout.extend(scores)
    layout.extend(score_bars)
    layout.append(globe_text)
    layout.extend(city_buttons)

def get_boston(layout: list, ser: serial.Serial, lanes: list):
    reset_window()
    clear(layout)

    background = tk.Label(image=data[4])
    background.place(x=0, y=0, relwidth=1, relheight=1)
    text = [tk.Label(text = f"The emissions of your road in Boston would be {city_emissions(lanes, Cities.boston):,} {emissions_unit}", font=("Arial", 18)),
            tk.Label(text = f"The cost of your road in Boston would be {city_cost(lanes, Cities.boston):,} {cost_unit}", font=("Arial", 18))]
    text[0].config(bg= "white", fg= "black")
    text[1].config(bg= "white", fg= "black")
    text[0].grid(row = 5, column = 1)
    text[1].grid(row = 6, column = 1)

    button = tk.Button(text = "Return", command= lambda: display_road(layout, ser, lanes), font=("Arial", 25))

    button.grid(row = 1, column = 1)

    layout.append(background)
    layout.extend(text)
    layout.append(button)
    
    window.grid_columnconfigure((0, 2), weight=1)
    window.grid_rowconfigure((2, 3, 4), weight=2)
    window.grid_rowconfigure((0, 7), weight=3)

def get_london(layout: list, ser: serial.Serial, lanes: list):
    reset_window()
    clear(layout)

    background = tk.Label(image=data[3])
    background.place(x=0, y=0, relwidth=1, relheight=1)
    text = [tk.Label(text = f"The emissions of your road in London would be {city_emissions(lanes, Cities.london):,} {emissions_unit}", font=("Arial", 25)),
            tk.Label(text = f"The cost of your road in London would be {city_cost(lanes, Cities.london):,} {cost_unit}", font=("Arial", 25))]
    text[0].config(bg= "white", fg= "black")
    text[1].config(bg= "white", fg= "black")
    text[0].grid(row = 1, column = 1)
    text[1].grid(row = 2, column = 1)

    button = tk.Button(text = "Return", command= lambda: display_road(layout, ser, lanes), font=("Arial", 25))

    button.grid(row = 10, column = 1)

    layout.append(background)
    layout.extend(text)
    layout.append(button)
    
    window.grid_columnconfigure((0, 2), weight=1)
    window.grid_rowconfigure((3, 4, 5, 6, 7, 9), weight=1)
    window.grid_rowconfigure((0, 11), weight=3)

def get_tokyo(layout: list, ser: serial.Serial, lanes: list):
    reset_window()
    clear(layout)

    background = tk.Label(image=data[13])
    background.place(x=0, y=0, relwidth=1, relheight=1)
    text = [tk.Label(text = f"The emissions of your road in Tokyo would be {city_emissions(lanes, Cities.tokyo):,} {emissions_unit}", font=("Arial", 25)),
            tk.Label(text = f"The cost of your road in Tokyo would be {city_cost(lanes, Cities.tokyo):,} {cost_unit}", font=("Arial", 25))]
    text[0].config(bg= "white", fg= "black")
    text[1].config(bg= "white", fg= "black")
    text[0].grid(row = 1, column = 1)
    text[1].grid(row = 2, column = 1)

    button = tk.Button(text = "Return", command= lambda: display_road(layout, ser, lanes), font=("Arial", 25))

    button.grid(row = 9, column = 1)

    layout.append(background)
    layout.extend(text)
    layout.append(button)
    
    window.grid_columnconfigure((0, 2), weight=1)
    window.grid_rowconfigure((3, 4, 5, 6, 7, 8), weight=2)
    window.grid_rowconfigure((0, 10), weight=3)

def get_lagos(layout: list, ser: serial.Serial, lanes: list):
    reset_window()
    clear(layout)

    background = tk.Label(image=data[11])
    background.place(x=0, y=0, relwidth=1, relheight=1)
    text = [tk.Label(text = f"The emissions of your road in Lagos would be {city_emissions(lanes, Cities.lagos):,} {emissions_unit}", font=("Arial", 21)),
            tk.Label(text = f"The cost of your road in Lagos would be {city_cost(lanes, Cities.lagos):,} {cost_unit}", font=("Arial", 21))]
    text[0].config(bg= "white", fg= "black")
    text[1].config(bg= "white", fg= "black")
    text[0].grid(row = 6, column = 1)
    text[1].grid(row = 7, column = 1)

    button = tk.Button(text = "Return", command= lambda: display_road(layout, ser, lanes), font=("Arial", 25))

    button.grid(row = 1, column = 1)

    layout.append(background)
    layout.extend(text)
    layout.append(button)
    
    window.grid_columnconfigure((0, 2), weight=1)
    window.grid_rowconfigure((3, 4, 5), weight=1)
    window.grid_rowconfigure((0, 8, 9, 10), weight=3)

def get_lima(layout: list, ser: serial.Serial, lanes: list):
    reset_window()
    clear(layout)

    background = tk.Label(image=data[8])
    background.place(x=0, y=0, relwidth=1, relheight=1)
    text = [tk.Label(text = f"The emissions of your road in Lima would be {city_emissions(lanes, Cities.lima):,} {emissions_unit}", font=("Arial", 22)),
            tk.Label(text = f"The cost of your road in Lima would be {city_cost(lanes, Cities.lima):,} {cost_unit}", font=("Arial", 22))]
    text[0].config(bg= "white", fg= "black")
    text[1].config(bg= "white", fg= "black")
    text[0].grid(row = 9, column = 1)
    text[1].grid(row = 10, column = 1)

    button = tk.Button(text = "Return", command= lambda: display_road(layout, ser, lanes), font=("Arial", 25))

    button.grid(row = 1, column = 1)

    layout.append(background)
    layout.extend(text)
    layout.append(button)
    
    window.grid_columnconfigure((0, 2), weight=1)
    window.grid_rowconfigure((3, 4, 5, 6), weight=2)
    window.grid_rowconfigure((0, 11), weight=3)

def road_cost(lanes: str) -> int:
    result = 0
    for lane in lanes:
        result += average_cost(lane)

    return int(result / len(lanes))
    
def road_capacity(lanes: str):
    result = 0
    for lane in lanes:
        result += RoadCapacity.capacity[lane]

    return int(result)

def road_emissions(lanes: str) -> int:
    result = 0
    for lane in lanes:
        result += average_emissions(lane)

    return int(result / len(lanes))

def average_cost(lane: str) -> int:
    """This function returns the average cost per 100 people for a vehicle type

    Args:
        lane (str): type of vehicle

    Returns:
        int: average cost
    """
    total_cost = 0
    for cos in cost:
        total_cost += cos[lane]
    
    return int(total_cost / len(cost))

def average_emissions(lane: str) -> int:
    """This function returns the average emissions per 100 people for a vehicle type

    Args:
        lane (str): type of vehicle

    Returns:
        int: average emissions
    """
    total_emissions = 0
    for em in emissions:
        total_emissions += em[lane]
    
    return int(total_emissions / len(emissions))

def city_emissions(lanes: list, city: int) -> int:
    result = 0
    for lane in lanes:
        result += emissions[city][lane]

    return int(result / len(lanes))

def city_cost(lanes: list, city: int) -> int:
    result = 0
    for lane in lanes:
        result += cost[city][lane]

    return int(result / len(lanes))

def get_progress_score(score: int):
    if score < 40:
        return "1.Horizontal.TProgressbar"

    elif score >= 40 and score <=60:
        return "2.Horizontal.TProgressbar"

    else:
        return "3.Horizontal.TProgressbar"

def get_capacity_score(lanes: list) -> int:
    capacity = road_capacity(lanes) / 6

    for i, cap in enumerate(capacity_range):
        if capacity <= cap:
            return i

def get_cost_score(lanes: list):
    cost = road_cost(lanes)

    for i, cos in enumerate(cost_range):
        if cost < cos:
            return 100-i
        
def get_emissions_score(lanes: list):
    emissions = road_emissions(lanes) 

    for i, em in enumerate(emissions_range):
        if emissions < em:
            return 100 - i

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