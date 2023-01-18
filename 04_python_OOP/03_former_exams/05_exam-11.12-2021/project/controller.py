from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def _find_car(self, model):
        for car in self.cars:
            if car.model == model:
                return car

    def _find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def _find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    @staticmethod
    def _check_if_driver_is_in_race_drivers(driver_name, race_drivers):
        for driver in race_drivers:
            if driver.name == driver_name:
                return True
        return False

    def _find_the_fastest_cars(self):
        pass

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self._find_car(model)

        if car:
            raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
            self.cars.append(new_car)
        elif car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
        else:
            return

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self._find_driver(driver_name)

        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self._find_race(race_name)

        if race:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._find_driver(driver_name)
        new_car = None

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        for c in reversed(self.cars):
            if type(c).__name__ == car_type and not c.is_taken:
                new_car = c
                break

        if not new_car:
            raise Exception(f"Car {car_type} could not be found!")

        if not new_car.is_taken and driver.car is not None:
            old_car_model = driver.car.model
            driver.car.is_taken = False
            driver.car = new_car
            new_car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car_model} to {driver.car.model}."

        driver.car = new_car
        new_car.is_taken = True
        return f"Driver {driver_name} chose the car {driver.car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        # race = self._find_race(race_name)
        # driver = self._find_driver(driver_name)
        #
        # if not race:
        #     raise Exception(f"Race {race_name} could not be found!")
        #
        # if not driver:
        #     raise Exception(f"Driver {driver_name} could not be found!")
        #
        # if driver.car is None:
        #     raise Exception(f"Driver {driver_name} could not participate in the race!")
        #
        # if self._check_if_driver_is_in_race_drivers(driver_name, race.drivers):
        #     raise Exception(f"Driver {driver_name} is already added in {race_name} race.")
        #
        # race.drivers.append(driver)
        # return f"Driver {driver_name} added in {race_name} race."
        if race_name not in [r.name for r in self.races]:
            raise Exception(f"Race {race_name} could not be found!")
        if driver_name not in [d.name for d in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")

        race = [r for r in self.races if r.name == race_name][0]
        driver = [d for d in self.drivers if d.name == driver_name][0]
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self._find_race(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = []
        count = 0

        for driver in sorted(race.drivers, key= lambda x: -x.car.speed_limit):
            if count == 3:
                break

            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
            count += 1
        return '\n'.join(result)
