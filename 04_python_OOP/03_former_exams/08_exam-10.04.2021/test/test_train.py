from train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Test", 5)

    def test_correct_initialization(self):
        self.assertEqual("Test", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_initial_class_attributes(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_add_method_when_the_train_is_full_raises_value_error(self):
        self.train.passengers = ["P1", "P2", "P3", "P4", "P5"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("P6")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_method_when_passenger_already_exists_raises_value_error(self):
        self.train.passengers = ["P1", "P2", "P3", "P4"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("P1")
        self.assertEqual("Passenger P1 Exists", str(ex.exception))

    def test_add_methods_if_working_correctly(self):
        result = self.train.add("P1")
        self.assertEqual(["P1"], self.train.passengers)
        self.assertEqual("Added passenger P1", result)

    def test_remove_passenger_that_doest_not_exist_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("P2")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_method_if_working_correctly(self):
        self.train.passengers = ["P1", "P2"]
        result = self.train.remove("P2")
        self.assertEqual(["P1"], self.train.passengers)
        self.assertEqual("Removed P2", result)


if __name__ == "__main__":
    main()
