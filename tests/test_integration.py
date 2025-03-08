import unittest
import sys
import os
import logging
from unittest.mock import patch
from io import StringIO

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.controller import get_user_choice, get_user_input, get_passphrase_config, main

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("integration_tests.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment before each test."""
        self.logger = logger
        self.logger.info("\n" + "="*50)
        self.logger.info(f"Starting integration test: {self._testMethodName}")
    
    def tearDown(self):
        """Clean up after each test."""
        self.logger.info(f"Finished integration test: {self._testMethodName}")
        self.logger.info("="*50 + "\n")
    
    @patch('builtins.input')
    def test_standard_password_flow(self, mock_input):
        """Test the complete flow for generating a standard password."""
        # Mock user inputs for standard password
        mock_input.side_effect = ['1', '12', 'yes', 'yes', 'yes', 'yes']
        
        # Capture stdout to verify output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            # Run the main function
            main()
            output = captured_output.getvalue()
            
            # Log captured output
            self.logger.info(f"Standard password test output:\n{output}")
            
            # Verify that a password was generated
            self.assertIn("Generated password:", output)
            # Check that the password is displayed
            self.assertTrue(len(output.split("Generated password: ")[1].strip()) > 0)
        finally:
            sys.stdout = sys.__stdout__
    
    @patch('builtins.input')
    def test_passphrase_flow(self, mock_input):
        """Test the complete flow for generating a passphrase."""
        # Mock user inputs for passphrase
        mock_input.side_effect = ['2', '4', '_']
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            main()
            output = captured_output.getvalue()
            
            self.logger.info(f"Passphrase test output:\n{output}")
            
            self.assertIn("Generated Passphrase:", output)
            self.assertIn("Generated password:", output)
        finally:
            sys.stdout = sys.__stdout__
    
    @patch('builtins.input')
    def test_spell_flow(self, mock_input):
        """Test the complete flow for generating a spell-style password."""
        # Mock user inputs for spell password
        mock_input.side_effect = ['3', '14']
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            main()
            output = captured_output.getvalue()
            
            self.logger.info(f"Spell password test output:\n{output}")
            
            self.assertIn("Generated Spell:", output)
            self.assertIn("Generated password:", output)
        finally:
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
