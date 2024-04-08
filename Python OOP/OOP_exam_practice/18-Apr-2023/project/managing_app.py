from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.user import User
from project.route import Route


class ManagingApp:
    VALID_VEHICLE_TYPES = {
        "CargoVan": CargoVan,
        "PassengerCar": PassengerCar
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for u in self.users:
            if u.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        try:
            vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        except KeyError:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for v in self.vehicles:
            if v.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for r in self.routes:
            if r.start_point == start_point and r.end_point == end_point and r.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if r.start_point == start_point and r.end_point == end_point and r.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if r.start_point == start_point and r.end_point == end_point and r.length > length:
                r.is_locked = True

        route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles_list = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles_list = sorted(
            vehicles_list,
            key=lambda v: (v.brand, v.model)
        )

        repaired_vehicles = 0

        for v in sorted_vehicles_list:
            if repaired_vehicles == count:
                break
            v.change_status()
            v.recharge()
            repaired_vehicles += 1

        return f"{repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        result = f"*** E-Drive-Rent ***\n"

        users_list = sorted(self.users, key=lambda u: -u.rating)

        for user in users_list:
            result += f"{str(user)}\n"

        return result[:-1]

