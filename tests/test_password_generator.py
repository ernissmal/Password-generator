import unittest
import re
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = PasswordGenerator()

    def test_standard_password_character_types(self):
        """Test that standard passwords contain expected character types"""
        password = self.generator.generate()
        
        # This is the failing assertion - the password doesn't contain digits
        self.assertTrue(any(c.isdigit() for c in password), "Password should contain digits")
        
        self.assertTrue(any(c.isalpha() for c in password), "Password should contain letters")
        self.assertTrue(any(c.isupper() for c in password), "Password should contain uppercase letters")
        self.assertTrue(any(c.islower() for c in password), "Password should contain lowercase letters")
        self.assertTrue(any(not c.isalnum() for c in password), "Password should contain special characters")

    # ...other tests...

if __name__ == '__main__':
    unittest.main()
