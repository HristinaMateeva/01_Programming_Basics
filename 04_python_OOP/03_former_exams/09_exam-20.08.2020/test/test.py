from student_report_card import StudentReportCard
from unittest import TestCase, main

class TestStudentReportCard(TestCase):
    def setUp(self):
        self.report_card = StudentReportCard("Test", 2)

    def test_correct_initialization(self):
        self.assertEqual("Test", self.report_card.student_name)
        self.assertEqual(2, self.report_card.school_year)
        self.assertEqual({}, self.report_card.grades_by_subject)

    def test_invalid_student_name_raises_valuer_error(self):
        with self.assertRaises(ValueError) as ex:
            self.report_card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_invalid_school_year_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.report_card.school_year = 14
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.report_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.report_card.school_year = -1
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_successful_year(self):
        self.report_card.school_year = 1
        self.assertEqual(1, self.report_card.school_year)

        self.report_card.school_year = 12
        self.assertEqual(12, self.report_card.school_year)

    def test_add_grade_with_subject_not_in_the_grades_by_subject(self):
        self.report_card.add_grade("Math", 6.00)
        self.assertEqual({"Math": [6.00]}, self.report_card.grades_by_subject)

    def test_add_grade_with_subject_which_is_in_the_grades_by_subject(self):
        self.report_card.add_grade("Math", 6.00)
        self.assertEqual({"Math": [6.00]}, self.report_card.grades_by_subject)
        self.report_card.add_grade("Math", 5.00)
        self.assertEqual({"Math": [6.00, 5.00]}, self.report_card.grades_by_subject)
        self.report_card.add_grade("Literature", 4.00)
        self.assertEqual({"Math": [6.00, 5.00], "Literature": [4.00]}, self.report_card.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.report_card.add_grade("Math", 6.00)
        self.report_card.add_grade("Math", 5.00)
        self.assertEqual("Math: 5.50", self.report_card.average_grade_by_subject())
        self.report_card.add_grade("Literature", 6.00)
        self.report_card.add_grade("Literature", 4.00)
        expected_result = "Math: 5.50\nLiterature: 5.00"
        self.assertEqual(expected_result, self.report_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.report_card.add_grade("Math", 6.00)
        self.report_card.add_grade("Math", 4.00)
        self.assertEqual("Average Grade: 5.00", self.report_card.average_grade_for_all_subjects())
        self.report_card.add_grade("Literature", 6.00)
        self.report_card.add_grade("Literature", 5.00)
        self.assertEqual("Average Grade: 5.25", self.report_card.average_grade_for_all_subjects())

    def test__repr__method_if_returning_correct_result(self):
        self.report_card.add_grade("Math", 6.00)
        self.report_card.add_grade("Math", 5.00)
        self.report_card.add_grade("Literature", 6.00)
        self.report_card.add_grade("Literature", 5.00)
        expected_result = "Name: Test\nYear: 2\n----------\nMath: 5.50\nLiterature: 5.50\n" \
                 "----------\nAverage Grade: 5.50"
        self.assertEqual(expected_result, self.report_card.__repr__())

if __name__ == "__main__":
    main()
