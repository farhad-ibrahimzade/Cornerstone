from serial import Serial

class MySerial():

    begin = True

    def __init__(self, ser: Serial) -> None:
        self.ser = ser
        pass

    def getLanes(self):
        line = self.ser.readline()   # read a byte
        if line:
            string = line.decode()  # convert the byte string to a unicode string
            data = string.split(",")
            if "Done" in data[0] or string ==  "":
                return "Done"
            
            
            output = "Lane " + str(int(data[1]) + 1) + ": " + data[0]
            
            return output
        
        if MySerial.begin:
            MySerial.begin = False
            return None
        
        return ""