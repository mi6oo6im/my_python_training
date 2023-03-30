from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):

    def setUp(self) -> None:
        self.student_with_courses = Student('Student_1',
                                            {
                                                'JavaScript': ['Some notes']
                                            })
        self.student_without_courses = Student('Student_2')

    def test_correct_initialization(self):
        self.assertEqual(self.student_without_courses.name, 'Student_2')
        self.assertEqual(self.student_without_courses.courses, {})
        self.assertEqual(self.student_with_courses.courses['JavaScript'][0], 'Some notes')

    def test_enroll_to_enrolled_course_update_notes(self):
        result = self.student_with_courses.enroll('JavaScript', ['Other notes'])
        self.assertEqual(self.student_with_courses.courses['JavaScript'][1], 'Other notes')
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_to_not_enrolled_course_with_notes(self):
        result = self.student_without_courses.enroll('Python', ['Python notes'], 'Y')
        self.assertEqual(self.student_without_courses.courses['Python'][0], 'Python notes')
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_to_not_enrolled_course_with_notes_no_third_param(self):
        result = self.student_without_courses.enroll('Python', ['Python notes'])
        self.assertEqual(self.student_without_courses.courses['Python'][0], 'Python notes')
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_to_not_enrolled_course_without_notes(self):
        result = self.student_without_courses.enroll('Python', ['Python notes'], 'N')
        self.assertEqual(self.student_without_courses.courses['Python'], [])
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_to_existing_course_adds_notes(self):
        result = self.student_with_courses.add_notes('JavaScript', 'New JS notes')
        self.assertEqual(self.student_with_courses.courses['JavaScript'][1], 'New JS notes')
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as context:
            self.student_without_courses.add_notes('JavaScript', 'New JS notes')
        self.assertEqual(str(context.exception), "Cannot add notes. Course not found.")

    def test_leave_course_that_exists_removes_it_from_dict(self):
        result = self.student_with_courses.leave_course('JavaScript')
        self.assertEqual(self.student_with_courses.courses, {})
        self.assertEqual(result, "Course has been removed")

    def test_leave_course_that_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as context:
            self.student_without_courses.leave_course('JavaScript')
        self.assertEqual(str(context.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    main()
