from pet_shop import PetShop
from unittest import TestCase, main

class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("PetShop")

    def test_correct_initialization(self):
        self.assertEqual("PetShop", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_negative_quantity_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("Granuls", -1)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food_with_zero_quantity_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("Granuls", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food_successfully(self):
        result = self.pet_shop.add_food("Granuls", 100)
        self.assertEqual({"Granuls": 100}, self.pet_shop.food)
        self.assertEqual("Successfully added 100.00 grams of Granuls.", result)
        self.pet_shop.add_food("Granuls", 100)
        self.assertEqual({"Granuls": 200}, self.pet_shop.food)

    def test_add_pet_already_existing_pet_raise_exception(self):
        self.pet_shop.pets = ["Lou"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Lou")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_successfully(self):
        result = self.pet_shop.add_pet("Lou")
        self.assertEqual(["Lou"], self.pet_shop.pets)
        self.assertEqual("Successfully added Lou.", result)

    def test_feed_pet_which_does_not_exist_in_pets_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Granuls", "Lou")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_food_which_does_not_exist(self):
        self.pet_shop.add_pet("Lou")
        result = self.pet_shop.feed_pet("Granuls", "Lou")
        self.assertEqual("You do not have Granuls", result)

    def test_feed_pet_with_lower_than_100_grams_food(self):
        self.pet_shop.pets = ["Lou"]
        self.pet_shop.food = {"Granuls": 50}
        result = self.pet_shop.feed_pet("Granuls", "Lou")
        self.assertEqual("Adding food...", result)
        self.assertEqual({"Granuls": 1050}, self.pet_shop.food)

    def test_feed_pet_successfully(self):
        self.pet_shop.pets = ["Lou"]
        self.pet_shop.food = {"Granuls": 500}
        result = self.pet_shop.feed_pet("Granuls", "Lou")
        self.assertEqual({"Granuls": 400}, self.pet_shop.food)
        self.assertEqual("Lou was successfully fed", result)

    def test__repr__method(self):
        self.pet_shop.add_pet("Lou")
        self.pet_shop.add_pet("Cashew")
        expected_result = 'Shop PetShop:\nPets: Lou, Cashew'
        self.assertEqual(expected_result, self.pet_shop.__repr__())

if __name__ == "__main__":
    main()
