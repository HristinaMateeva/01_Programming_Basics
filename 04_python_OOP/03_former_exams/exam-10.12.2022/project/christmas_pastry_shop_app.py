from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def _find_delicacy(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy

    def _find_booth(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = self._find_delicacy(name)

        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            new_delicacy = Gingerbread(name, price)
            self.delicacies.append(new_delicacy)

        elif type_delicacy == "Stolen":
            new_delicacy = Stolen(name, price)
            self.delicacies.append(new_delicacy)

        else:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = self._find_booth(booth_number)

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            new_booth = OpenBooth(booth_number, capacity)
            self.booths.append(new_booth)

        elif type_booth == "Private Booth":
            new_booth = PrivateBooth(booth_number, capacity)
            self.booths.append(new_booth)

        else:
            raise Exception(f"{type_booth} is not a valid booth!")

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        available_booth = None
        for bth in self.booths:
            if not bth.is_reserved and bth.capacity >= number_of_people:
                available_booth = bth
                break

        if not available_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        available_booth.reserve(number_of_people)
        return f"Booth {available_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._find_booth(booth_number)
        delicacy = self._find_delicacy(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._find_booth(booth_number)
        bill = 0

        for delicacy in booth.delicacy_orders:
            bill += delicacy.price

        bill += booth.price_for_reservation
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
