from library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Test")

    def test_correct_initialization(self):
        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_method(self):
        self.library.add_book("Dan Brown", "Angels and Demons")
        self.assertEqual({"Dan Brown": ["Angels and Demons"]}, self.library.books_by_authors)
        self.library.add_book("Dan Brown", "Inferno")
        self.assertEqual({"Dan Brown": ["Angels and Demons", "Inferno"]}, self.library.books_by_authors)

    def test_add_reader_which_does_not_exist(self):
        self.library.add_reader("Tina")
        self.assertEqual({"Tina": []}, self.library.readers)

    def test_add_reader_which_exists(self):
        self.library.readers = {"Tina": []}
        result = self.library.add_reader("Tina")
        self.assertEqual("Tina is already registered in the Test library.", result)

    def test_rent_book_if_reader_does_not_exist(self):
        self.library.readers = {"Tina": []}
        result = self.library.rent_book("Miro", "Dan Brown", "Angels and Demons")
        self.assertEqual("Miro is not registered in the Test Library.", result)

    def test_rent_book_if_author_does_not_exist(self):
        self.library.add_book("Dan Brown", "Angels and Demons")
        self.library.add_reader("Tina")
        result = self.library.rent_book("Tina", "Stephen King", "Fairy Tale")
        self.assertEqual("Test Library does not have any Stephen King's books.", result)

    def test_rent_book_if_title_does_not_exist(self):
        self.library.add_book("Dan Brown", "Angels and Demons")
        self.library.add_reader("Tina")
        result = self.library.rent_book("Tina", "Dan Brown", "Inferno")
        self.assertEqual("""Test Library does not have Dan Brown's "Inferno".""", result)

    def test_rent_book_works_correctly(self):
        self.library.add_book("Dan Brown", "Angels and Demons")
        self.library.add_book("Dan Brown", "Inferno")
        self.library.add_reader("Tina")
        self.library.rent_book("Tina", "Dan Brown", "Inferno")
        self.assertEqual({"Tina": [{"Dan Brown": "Inferno"}]}, self.library.readers)
        self.assertEqual({"Dan Brown": ["Angels and Demons"]}, self.library.books_by_authors)

if __name__ == "__main__":
    main()
