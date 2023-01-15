from bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self):
        self.book_store = Bookstore(10)

    def test_correct_initialization(self):
        self.assertEqual(10, self.book_store.books_limit)
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store._Bookstore__total_sold_books)

    def test_books_limit_with_incorrect_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = -1
        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test__len__if_works_properly(self):
        self.book_store.availability_in_store_by_book_titles = {}
        self.assertEqual(0, self.book_store.__len__())
        self.book_store.availability_in_store_by_book_titles = {"Angels & Demons": 5, "Inferno": 4}
        self.assertEqual(9, self.book_store.__len__())

    def test_receive_book_if_there_is_no_enough_space_raise_exception(self):
        self.book_store.availability_in_store_by_book_titles = {}
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book("The Da Vinci Code", 11)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

        self.book_store.availability_in_store_by_book_titles = {"Angels & Demons": 5, "Inferno": 4}
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book("The Da Vinci Code", 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_if_there_is_enough_space(self):
        self.book_store.availability_in_store_by_book_titles = {}
        result = self.book_store.receive_book("The Da Vinci Code", 3)
        self.assertEqual({"The Da Vinci Code": 3}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual("3 copies of The Da Vinci Code are available in the bookstore.", result)

        self.book_store.availability_in_store_by_book_titles = {"The Da Vinci Code": 3}
        result = self.book_store.receive_book("Inferno", 4)
        self.assertEqual({"The Da Vinci Code": 3, "Inferno": 4}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual("4 copies of Inferno are available in the bookstore.", result)

    def test_receive_book_if_new_quantity_received(self):
        self.book_store.availability_in_store_by_book_titles = {"Inferno": 3}
        result = self.book_store.receive_book("Inferno", 4)
        self.assertEqual({"Inferno": 7}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual("7 copies of Inferno are available in the bookstore.", result)

    def test_sell_book_if_book_is_not_available_in_the_store_raise_exception(self):
        self.book_store.availability_in_store_by_book_titles = {}
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Angels & Demons", 1)
        self.assertEqual("Book Angels & Demons doesn't exist!", str(ex.exception))

        self.book_store.availability_in_store_by_book_titles = {"The Da Vinci Code": 3, "Inferno": 4}
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Angels & Demons", 1)
        self.assertEqual("Book Angels & Demons doesn't exist!", str(ex.exception))

    def test_sell_book_if_there_is_no_enough_copies_of_that_book_raise_exception(self):
        self.book_store.availability_in_store_by_book_titles = {"The Da Vinci Code": 3, "Inferno": 4}
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book("Inferno", 5)
        self.assertEqual(4, self.book_store.availability_in_store_by_book_titles["Inferno"])
        self.assertEqual("Inferno has not enough copies to sell. Left: 4", str(ex.exception))

    def test_sell_book_if_works_properly(self):
        self.book_store.availability_in_store_by_book_titles = {"The Da Vinci Code": 3, "Inferno": 4}
        result = self.book_store.sell_book("Inferno", 4)
        self.assertEqual(0, self.book_store.availability_in_store_by_book_titles["Inferno"])
        self.assertEqual(4, self.book_store._Bookstore__total_sold_books)
        self.assertEqual("Sold 4 copies of Inferno", result)

        self.book_store.availability_in_store_by_book_titles = {"The Da Vinci Code": 3, "Inferno": 0}
        result = self.book_store.sell_book("The Da Vinci Code", 2)
        self.assertEqual(1, self.book_store.availability_in_store_by_book_titles["The Da Vinci Code"])
        self.assertEqual(6, self.book_store._Bookstore__total_sold_books)
        self.assertEqual("Sold 2 copies of The Da Vinci Code", result)


    def test__str__if_works_properly(self):
        self.book_store.availability_in_store_by_book_titles = {"The Da Vinci Code": 5, "Inferno": 4}
        self.book_store.sell_book("Inferno", 2)
        self.book_store.sell_book("The Da Vinci Code", 2)
        expected_result = "Total sold books: 4\n" \
                          "Current availability: 5\n" \
                          " - The Da Vinci Code: 3 copies\n" \
                          " - Inferno: 2 copies"
        self.assertEqual(expected_result, self.book_store.__str__())

        self.book_store.availability_in_store_by_book_titles = {"The Da Vinci Code": 3, "Inferno": 2}
        self.book_store.sell_book("Inferno", 2)
        expected_result = "Total sold books: 6\n" \
                          "Current availability: 3\n" \
                          " - The Da Vinci Code: 3 copies\n" \
                          " - Inferno: 0 copies"
        self.assertEqual(expected_result, self.book_store.__str__())

if __name__ == "__main__":
    main()
