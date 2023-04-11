from enum import IntEnum

class BusCost (IntEnum):
    # Cost to transport 100 people by bus in various cities in USD
    boston = 1050000
    london = 884802
    tokyo = 570000
    lagos = 380162
    lima = 400000

class BusEmissions(IntEnum):
    # Emissions from transporting 100 people by bus in various cities in USD
    boston = 66
    london = 20
    tokyo = 39
    lagos = 29
    lima = 7