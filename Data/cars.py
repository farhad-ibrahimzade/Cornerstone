from enum import IntEnum

class CarCost (IntEnum):
    # Cost to transport 100 people by car in various cities in USD
    boston = 3718968
    london = 2392402
    tokyo = 1928313
    lagos = 2386852
    lima = 1779712

class CarEmissions(IntEnum):
    # Emissions from transporting 100 people by car in various cities in USD
    boston = 18149
    london = 13648
    tokyo = 15712
    lagos = 14607
    lima = 16151