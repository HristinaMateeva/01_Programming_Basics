from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def _find_food(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def _find_drink(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink

    def _find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def add_food(self, food_type: str, name: str, price: float):
        food = self._find_food(name)

        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type == "Bread":
            new_food = Bread(name, price)
            self.food_menu.append(new_food)

        elif food_type == "Cake":
            new_food = Cake(name, price)
            self.food_menu.append(new_food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        drink = self._find_drink(name)

        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            new_drink = Tea(name, portion, brand)
            self.drinks_menu.append(new_drink)

        elif drink_type == "Water":
            new_drink = Water(name, portion, brand)
            self.drinks_menu.append(new_drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self._find_table(table_number)

        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            new_table = InsideTable(table_number, capacity)
            self.tables_repository.append(new_table)

        elif table_type == "OutsideTable":
            new_table = OutsideTable(table_number, capacity)
            self.tables_repository.append(new_table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.is_reserved = True
                table.number_of_people = number_of_people
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        pass

    def order_drink(self, table_number: int, *drink_names):
        pass

    def leave_table(self, table_number: int):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
