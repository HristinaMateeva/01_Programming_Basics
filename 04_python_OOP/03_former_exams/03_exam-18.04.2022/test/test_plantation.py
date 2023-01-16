from plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(5)

    def test_correct_initialization(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_if_works_properly_with_incorrect_data(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_raise_value_error(self):
        self.plantation.workers = ["Ivan"]
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Ivan")
        self.assertEqual("Worker already hired!", str(ex.exception))

        self.plantation.workers = ["Ivan", "Georgi"]
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Georgi")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_works_properly(self):
        result = self.plantation.hire_worker("Ivan")
        self.assertEqual(["Ivan"], self.plantation.workers)
        self.assertEqual("Ivan successfully hired.", result)

        result = self.plantation.hire_worker("Georgi")
        self.assertEqual(["Ivan", "Georgi"], self.plantation.workers)
        self.assertEqual("Georgi successfully hired.", result)

    def test__len__return_count_of_plants(self):
        self.assertEqual(0, self.plantation.plants.__len__())

        self.plantation.plants = {"Ivan": ["plant1", "plant2"]}
        self.assertEqual(2, self.plantation.__len__())

        self.plantation.plants = {"Ivan": ["plant1", "plant2"], "Georgi": ["plant3", "plant4"]}
        self.assertEqual(4, self.plantation.__len__())

    def test_planting_if_worker_does_not_exist_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Dimitar", "Tomatoes")
        self.assertEqual("Worker with name Dimitar is not hired!", str(ex.exception))

        self.plantation.workers = ["Ivan"]
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Dimitar", "Tomatoes")
        self.assertEqual("Worker with name Dimitar is not hired!", str(ex.exception))

    def test_planting_when_there_is_no_enough_space_for_plants_raise_value_error(self):
        self.plantation.workers = ["Ivan"]
        self.plantation.plants = {"Ivan": ["Tomatoes", "Cucumbers", "Cherry tomatoes", "Potatoes", "Peppers"]}
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Ivan", "plant")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_if_worker_exists_works_properly(self):
        self.plantation.workers = ["Ivan"]
        self.plantation.plants = {"Ivan": ["Tomatoes"]}
        result = self.plantation.planting("Ivan", "Cucumbers")
        self.assertEqual({"Ivan": ["Tomatoes", "Cucumbers"]}, self.plantation.plants)
        self.assertEqual("Ivan planted Cucumbers.", result)

    def test_planting_first_plant_works_properly(self):
        self.plantation.workers = ["Ivan"]
        self.plantation.plants = {}
        result = self.plantation.planting("Ivan", "Tomatoes")
        self.assertEqual({"Ivan": ["Tomatoes"]}, self.plantation.plants)
        self.assertEqual("Ivan planted it's first Tomatoes.", result)

    def test_planting_wrong_dict_assignment(self):
        self.pl = Plantation(2)
        self.pl.hire_worker('Martin')
        self.pl.planting('Martin', 'Radishes')
        self.pl.planting('Martin', 'carrots')
        self.assertEqual(len(self.pl.plants['Martin']), 2)

    def test__str__if_works_properly(self):
        self.plantation.workers = ["Ivan", "Georgi"]
        self.plantation.plants = {"Ivan": ["Tomatoes", "Cucumbers"], "Georgi": ["Potatoes", "Peppers"]}
        expected_result = "Plantation size: 5\n" \
                          "Ivan, Georgi\n" \
                          "Ivan planted: Tomatoes, Cucumbers\n" \
                          "Georgi planted: Potatoes, Peppers"
        self.assertEqual(expected_result, self.plantation.__str__())

    def test__repr__if_works_properly(self):
        self.plantation.workers = ["Ivan", "Georgi"]
        expected_result = "Size: 5\n" \
                          "Workers: Ivan, Georgi"
        self.assertEqual(expected_result, self.plantation.__repr__())

if __name__ == "__main__":
    main()
