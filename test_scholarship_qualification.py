import unittest
from student import scholarship_qualification

class TestScholarshipQualification(unittest.TestCase):

    def test_qualifies(self):
        name = "Alice"
        years = 3 
import unittest
from student import scholarship_qualification

class TestScholarshipQualification(unittest.TestCase):

    def test_qualifies(self):
        name = "Alice"
        years = 3 
        gpa = 3.8
        
        expected_output = "Alice, you qualify for a scholarship in Rutgers university!"
        actual_output = scholarship_qualification(name, years, gpa)
        self.assertEqual(expected_output, actual_output)

    def test_does_not_qualify_years(self):
        name = "Bob"
        years = 1
        gpa = 3.9 
        expected_output = "Bob, you do not qualify for a scholarship in Rutgers university."
        actual_output = scholarship_qualification(name, years, gpa)
        self.assertEqual(expected_output, actual_output)

    def test_does_not_qualify_gpa(self):
        name = "Charlie"
        years = 2
        gpa = 3.4
        expected_output = "Charlie, you do not qualify for a scholarship in Rutgers university."
        actual_output = scholarship_qualification(name, years, gpa)
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()

        expected_output = "Bob, you do not qualify for a scholarship in Rutgers university."
        actual_output = scholarship_qualification(name, years, gpa)
        self.assertEqual(expected_output, actual_output)

    def test_does_not_qualify_gpa(self):
        name = "Charlie"
        years = 2
        gpa = 3.4
        expected_output = "Charlie, you do not qualify for a scholarship in Rutgers university."
        actual_output = scholarship_qualification(name, years, gpa)
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
