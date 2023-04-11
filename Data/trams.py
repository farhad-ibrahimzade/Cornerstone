from enum import IntEnum

class TramCost (IntEnum):
    # Cost to transport 100 people by tram in various cities in USD
    boston = 214000000
    london = 41477938
    tokyo = 25550578
    lagos = 9685879
    lima = 5985974

class TramEmissions(IntEnum):
    # Emissions from transporting 100 people by tram in various cities in USD
    boston = 491
    london = 682
    tokyo = 2952
    lagos = 0
    lima = 2124