from Data.bikes import BikeCost, BikeEmissions
from Data.buses import BusCost, BusEmissions
from Data.cars import CarCost, CarEmissions
from Data.trams import TramCost, TramEmissions
from Data.pedestrians import PedestrianCost, PedestrianEmissions


class CityCost:
    # Cost to transport 100 people by all types of transport in various cities in USD
    boston = {"Bike": BikeCost.boston, "Bus": BusCost.boston, "Car": CarCost.boston,
                "Tram": TramCost.boston, "Pedestrian": PedestrianCost.boston}
    london = {"Bike": BikeCost.london, "Bus": BusCost.london, "Car": CarCost.london,
                "Tram": TramCost.london, "Pedestrian": PedestrianCost.london}
    tokyo = {"Bike": BikeCost.tokyo, "Bus": BusCost.tokyo, "Car": CarCost.tokyo,
                "Tram": TramCost.tokyo, "Pedestrian": PedestrianCost.tokyo}
    lagos = {"Bike": BikeCost.lagos, "Bus": BusCost.lagos, "Car": CarCost.lagos,
                "Tram": TramCost.lagos, "Pedestrian": PedestrianCost.lagos}
    lima = {"Bike": BikeCost.lima, "Bus": BusCost.lima, "Car": CarCost.lima,
                "Tram": TramCost.lima, "Pedestrian": PedestrianCost.lima}

class CityEmissions:
    # Emissions from transporting 100 people by all types of transport in various cities in USD
    boston = {"Bike": BikeEmissions.boston, "Bus": BusEmissions.boston, "Car": CarEmissions.boston,
                "Tram": TramEmissions.boston, "Pedestrian": PedestrianEmissions.boston}
    london = {"Bike": BikeEmissions.london, "Bus": BusEmissions.london, "Car": CarEmissions.london,
                "Tram": TramEmissions.london, "Pedestrian": PedestrianEmissions.london}
    tokyo = {"Bike": BikeEmissions.tokyo, "Bus": BusEmissions.tokyo, "Car": CarEmissions.tokyo,
                "Tram": TramEmissions.tokyo, "Pedestrian": PedestrianEmissions.tokyo}
    lagos = {"Bike": BikeEmissions.lagos, "Bus": BusEmissions.lagos, "Car": CarEmissions.lagos,
                "Tram": TramEmissions.lagos, "Pedestrian": PedestrianEmissions.lagos}
    lima = {"Bike": BikeEmissions.lima, "Bus": BusEmissions.lima, "Car": CarEmissions.lima,
                "Tram": TramEmissions.lima, "Pedestrian": PedestrianEmissions.lima}

class RoadCapacity:
    # Capacity of lane in people per hour
    capacity = {"Bike": 7500, "Bus": 6000, "Car": 1000, "Tram": 15000, "Pedestrian": 9000}

