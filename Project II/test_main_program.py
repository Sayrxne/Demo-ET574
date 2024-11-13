#Project II - Chasyl De Guzman

import unittest
from unittest.mock import patch
import main_program

class TestMainFunction(unittest.TestCase):
    
    #test_main_valid_input
    @patch('builtins.input', side_effect=['3', '85', '90', '78'])  # Mock user inputs
    @patch('builtins.print')  # Mock the print function
    def test_main_valid_input(self, mock_print, mock_input):
       # Simulate the main function behavior
       main_program.main()
       mock_print.assert_called_with("The average grade for 3 students is: 84.33")
       self.assertIn(
           unittest.mock.call("The average grade for 3 students is: 84.33"),
           mock_print.mock_calls
       )

    #test_invalid_number_of_students
    @patch('builtins.input', side_effect=['-1', '0', '3', 85, 90, 78])  # Simulate invalid and then valid inputs for the number of students
    @patch('builtins.print')  # Mock the print function to capture output
    def test_invalid_number_of_students(self, mock_print, mock_input):
        # Simulate the main function behavior
        main_program.main()
        mock_print.assert_called_with("The average grade for 3 students is: 84.33")
        self.assertIn(
           unittest.mock.call("The average grade for 3 students is: 84.33"),
           mock_print.mock_calls
       )

    #test_invalid_grades    
    @patch('builtins.input', side_effect=['3', '-5', '110', '85', '90', '78'])  # Simulate invalid and valid inputs for grades
    @patch('builtins.print')  # Mock the print function to capture output
    def test_invalid_grades(self, mock_print, mock_input):
        # Simulate the main function behavior 
        main_program.main()
        mock_print.assert_called_with("The average grade for 3 students is: 84.33")
        self.assertIn(
           unittest.mock.call("The average grade for 3 students is: 84.33"),
           mock_print.mock_calls)
        
    #Additional Test Case Trial
    @patch('builtins.input', side_effect=['3', '-10', '150', '85', '90', '78'])  # Invalid grades followed by valid grades
    @patch('builtins.print')  # Mock the print function to capture output
    def test_invalid_grades_then_valid(self, mock_print, mock_input):
        # Simulate the main function behavior 
        main_program.main()
        mock_print.assert_called_with("The average grade for 3 students is: 84.33")
        self.assertIn(
           unittest.mock.call("The average grade for 3 students is: 84.33"),
           mock_print.mock_calls)



if __name__ == "__main__":
    unittest.main()