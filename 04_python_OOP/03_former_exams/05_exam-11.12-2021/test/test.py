from team import Team
from unittest import TestCase, main

class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Test")

    def test_correct_initialization(self):
        self.assertEqual("Test", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = "Test123"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        result = self.team.add_member(Tina=27, Miro=27)
        self.assertEqual("Successfully added: Tina, Miro", result)
        result = self.team.add_member(Tina=25, Miro=25)
        self.assertEqual("Successfully added: ", result)

    def test_remove_member_which_does_not_exist(self):
        self.team.add_member(Tina=27, Miro=27)
        result = self.team.remove_member("Ivan")
        self.assertEqual("Member with name Ivan does not exist", result)

    def test_remove_member_which_exist(self):
        self.team.add_member(Tina=27, Miro=27)
        result = self.team.remove_member("Tina")
        self.assertEqual("Member Tina removed", result)
        self.assertEqual({"Miro": 27}, self.team.members)

    def test__gt__if_returns_true(self):
        other = Team("Other")
        self.team.members = {"Tina": 27, "Miro": 27}
        other.members = {"Tina": 27}
        self.assertEqual(True, self.team.__gt__(other))

    def test__gt__if_returns_false(self):
        other = Team("Other")
        self.team.members = {"Tina": 27}
        other.members = {"Tina": 27, "Miro": 27}
        self.assertEqual(False, self.team.__gt__(other))

    def test__len__if_works_properly(self):
        self.team.add_member(Tina=27, Miro=27)
        self.assertEqual(2, self.team.__len__())

    def test__add__if_works_properly(self):
        other = Team("Other")
        self.team.members = {"Tina": 27}
        other.members = {"Miro":  27}
        new_team = self.team.__add__(other)
        self.assertEqual("TestOther", new_team.name)
        self.assertEqual({"Tina": 27, "Miro": 27}, new_team.members)

    def test__str__if_works_properly(self):
        self.team.members = {"Tina": 27, "Miro": 27, "Misho": 29}
        expected_result = "Team name: Test\n" \
                          "Member: Misho - 29-years old\n" \
                          "Member: Miro - 27-years old\n" \
                          "Member: Tina - 27-years old"
        self.assertEqual(expected_result, self.team.__str__())


if __name__ == "__main__":
    main()
