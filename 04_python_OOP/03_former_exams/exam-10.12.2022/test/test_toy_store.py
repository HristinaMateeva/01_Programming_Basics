from toy_store import ToyStore
from unittest import TestCase, main

class TestToyStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_correct_initialization(self):
        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        self.assertEqual(None, self.toy_store.toy_shelf["B"])
        self.assertEqual(None, self.toy_store.toy_shelf["C"])
        self.assertEqual(None, self.toy_store.toy_shelf["D"])
        self.assertEqual(None, self.toy_store.toy_shelf["E"])
        self.assertEqual(None, self.toy_store.toy_shelf["F"])
        self.assertEqual(None, self.toy_store.toy_shelf["G"])
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,}
        self.assertEqual(expected_result, self.toy_store.toy_shelf)

    def test_add_toy_if_shelf_not_in_toys_keys_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("H", "Teddy bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_if_toy_already_in_the_shelf_raise_exception(self):
        self.toy_store.toy_shelf = {
            "A": "Teddy bear",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,}
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Teddy bear")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

        self.toy_store.toy_shelf = {
            "A": "Teddy bear", "B": None,
            "C": None,
            "D": None,
            "E": "Car",
            "F": None,
            "G": None,}

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("E", "Car")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_if_shelf_is_none_raise_exception(self):
        self.toy_store.toy_shelf = {
            "A": "Teddy bear", "B": None,
            "C": None,
            "D": None,
            "E": "Car",
            "F": None,
            "G": None, }
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("E", "Doll")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_if_works_properly(self):
        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None, }
        result = self.toy_store.add_toy("C", "Doll")
        expected_result = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": None,
            "G": None, }
        self.assertEqual(expected_result, self.toy_store.toy_shelf)
        self.assertEqual("Doll", self.toy_store.toy_shelf["C"])
        self.assertEqual("Toy:Doll placed successfully!", result)

        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": None,
            "G": None, }
        result = self.toy_store.add_toy("F", "Flamingo")
        expected_result = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": "Flamingo",
            "G": None, }
        self.assertEqual(expected_result, self.toy_store.toy_shelf)
        self.assertEqual("Flamingo", self.toy_store.toy_shelf["F"])
        self.assertEqual("Toy:Flamingo placed successfully!", result)

    def test_remove_toy_if_shelf_not_in_shelf_keys_raise_exception(self):
        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": "Flamingo",
            "G": None, }
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("H", "Baby doll")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_if_toy_name_is_incorrect_raise_exception(self):
        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": "Flamingo",
            "G": None, }
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("C", "Baby doll")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_if_remove_toy_works_correctly(self):
        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": "Flamingo",
            "G": None, }
        expected_result = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": None,
            "G": None, }
        result = self.toy_store.remove_toy("F", "Flamingo")
        self.assertEqual(expected_result, self.toy_store.toy_shelf)
        self.assertEqual(None, self.toy_store.toy_shelf["F"])
        self.assertEqual("Remove toy:Flamingo successfully!", result)

        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": None,
            "G": None, }
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None, }
        result = self.toy_store.remove_toy("C", "Doll")
        self.assertEqual(expected_result, self.toy_store.toy_shelf)
        self.assertEqual(None, self.toy_store.toy_shelf["C"])
        self.assertEqual("Remove toy:Doll successfully!", result)

if __name__ == "__main__":
    main()
