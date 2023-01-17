from movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("The Da Vinci Code", 2006, 6.60)

    def test_correct_initialization(self):
        self.assertEqual("The Da Vinci Code", self.movie.name)
        self.assertEqual(2006, self.movie.year)
        self.assertEqual(6.60, self.movie.rating)

    def test_name_setter_with_incorrect_name(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_setter_with_incorrect_year(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1820
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_that_already_exists(self):
        self.movie.actors = ["Tom Hanks"]
        result = self.movie.add_actor("Tom Hanks")
        self.assertEqual("Tom Hanks is already added in the list of actors!", result)

    def test_add_actor_if_works_properly(self):
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor("Tom Hanks")
        self.assertEqual(["Tom Hanks"], self.movie.actors)
        self.movie.add_actor("Audrey Tautou")
        self.assertEqual(["Tom Hanks", "Audrey Tautou"], self.movie.actors)

    def test__gt__method_with_other_movie_with_lower_rating(self):
        other = Movie("Inferno", 2016, 6.20)
        result = self.movie.__gt__(other)
        self.assertEqual('"The Da Vinci Code" is better than "Inferno"', result)

    def test__gt__method_with_other_movie_with_higher_rating(self):
        other = Movie("Angels & Demons", 2009, 6.70)
        result = self.movie.__gt__(other)
        self.assertEqual('"Angels & Demons" is better than "The Da Vinci Code"', result)

    def test__repr__if_works_properly(self):
        self.movie.add_actor("Tom Hanks")
        self.movie.add_actor("Audrey Tautou")
        expected_result = "Name: The Da Vinci Code\n" \
                          "Year of Release: 2006\n" \
                          "Rating: 6.60\n" \
                          "Cast: Tom Hanks, Audrey Tautou"
        self.assertEqual(expected_result, self.movie.__repr__())

if __name__ == "__main__":
    main()
