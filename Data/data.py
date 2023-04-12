from Data.bikes import BikeCost, BikeEmissions
from Data.buses import BusCost, BusEmissions
from Data.cars import CarCost, CarEmissions
from Data.trams import TramCost, TramEmissions
from Data.pedestrians import PedestrianCost, PedestrianEmissions


class CityCost:
    # Cost to transport 100 people by all types of transport in various cities in USD
    boston = {"bike": BikeCost.boston, "bus": BusCost.boston, "car": CarCost.boston,
                "tram": TramCost.boston, "pedestrian": PedestrianCost.boston}
    london = {"bike": BikeCost.london, "bus": BusCost.london, "car": CarCost.london,
                "tram": TramCost.london, "pedestrian": PedestrianCost.london}
    tokyo = {"bike": BikeCost.tokyo, "bus": BusCost.tokyo, "car": CarCost.tokyo,
                "tram": TramCost.tokyo, "pedestrian": PedestrianCost.tokyo}
    lagos = {"bike": BikeCost.lagos, "bus": BusCost.lagos, "car": CarCost.lagos,
                "tram": TramCost.lagos, "pedestrian": PedestrianCost.lagos}
    lima = {"bike": BikeCost.lima, "bus": BusCost.lima, "car": CarCost.lima,
                "tram": TramCost.lima, "pedestrian": PedestrianCost.lima}

class CityEmissions:
    # Emissions from transporting 100 people by all types of transport in various cities in USD
    boston = {"bike": BikeEmissions.boston, "bus": BusEmissions.boston, "car": CarEmissions.boston,
                "tram": TramEmissions.boston, "pedestrian": PedestrianEmissions.boston}
    london = {"bike": BikeEmissions.london, "bus": BusEmissions.london, "car": CarEmissions.london,
                "tram": TramEmissions.london, "pedestrian": PedestrianEmissions.london}
    tokyo = {"bike": BikeEmissions.tokyo, "bus": BusEmissions.tokyo, "car": CarEmissions.tokyo,
                "tram": TramEmissions.tokyo, "pedestrian": PedestrianEmissions.tokyo}
    lagos = {"bike": BikeEmissions.lagos, "bus": BusEmissions.lagos, "car": CarEmissions.lagos,
                "tram": TramEmissions.lagos, "pedestrian": PedestrianEmissions.lagos}
    lima = {"bike": BikeEmissions.lima, "bus": BusEmissions.lima, "car": CarEmissions.lima,
                "tram": TramEmissions.lima, "pedestrian": PedestrianEmissions.lima}
