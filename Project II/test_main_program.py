#Project II - Chasyl De Guzman

import unittest
from unittest.mock import patch
import main_program

class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['3', '85', '90', '78'])  # Mock user inputs
    @patch('builtins.print')  # Mock the print function
    def test_main_valid_input(self, mock_print, mock_input):
       main_program.main()
       mock_print.assert_called_with("The average grade for 3 students is: 84.33")
       self.assertIn(
           unittest.mock.call("The average grade for 3 students is: 84.33"),
           mock_print.mock_calls
       )
       


if __name__ == "__main__":
    unittest.main()       