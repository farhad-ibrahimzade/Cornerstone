from PIL import ImageTk, Image

class Images():
    start = Image.open("Images\city.png").resize((500,500))
    car = Image.open("Images\car.png").resize((300,300))