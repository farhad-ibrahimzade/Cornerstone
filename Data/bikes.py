from enum import IntEnum

class BikeCost (IntEnum):
    # Cost to transport 100 people by bike in various cities in USD
    boston = 50000
    london = 49000
    tokyo = 60000
    lagos = 18350
    lima = 17200

class BikeEmissions(IntEnum):
    # Emissions from transporting 100 people by bike in various cities in USD
    boston = 0
    london = 0
    tokyo = 0
    lagos = 0
    lima = 0