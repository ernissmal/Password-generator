import unittest
import sys
import os
import logging
from io import StringIO

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.model import generate_password, generate_passphrase, generate_spell
from tests.detailed_test_logger import DetailedTestLogger
from tests.password_policy_validator import PasswordPolicyValidator

# Configure logging
log_filename = f"password_generator_detailed_tests_{os.getpid()}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
detailed_logger = DetailedTestLogger(logger)

class EnhancedPasswordGeneratorTests(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment before each test."""
        self.logger = logger
        self.detailed_logger = detailed_logger
        self.logger.info("\n" + "="*50)
        self.logger.info(f"Starting test: {self._testMethodName}")
    
    def tearDown(self):
        """Clean up after each test."""
        self.logger.info(f"Finished test: {self._testMethodName}")
        self.logger.info("="*50 + "\n")
        
    def test_standard_password_with_detailed_analysis(self):
        """Test standard password generation with detailed analysis."""
        # Test various configurations
        test_configs = [
            {"length": 12, "use_digits": True, "use_special_chars": True, 
             "use_uppercase": True, "use_lowercase": True},
            {"length": 16, "use_digits": True, "use_special_chars": False, 
             "use_uppercase": True, "use_lowercase": True},
            {"length": 8, "use_digits": True, "use_special_chars": True, 
             "use_uppercase": False, "use_lowercase": True},
            {"length": 20, "use_digits": False, "use_special_chars": False, 
             "use_uppercase": True, "use_lowercase": True},
        ]
        
        for config in test_configs:
            password = generate_password(**config)
            
            # Log detailed password analysis
            self.detailed_logger.log_password("Standard", password, config)
            
            # Validate against policy
            validation = PasswordPolicyValidator.validate_standard_password(
                password,
                min_length=config["length"],
                require_uppercase=config["use_uppercase"],
                require_lowercase=config["use_lowercase"],
                require_digits=config["use_digits"],
                require_special=config["use_special_chars"]
            )
            
            self.assertTrue(validation["valid"], 
                           f"Password failed validation: {validation['issues']}")
    
    def test_passphrase_with_detailed_analysis(self):
        """Test passphrase generation with detailed analysis."""
        # Test various configurations
        test_configs = [
            {"word_count": 3, "delimiter": "-"},
            {"word_count": 4, "delimiter": "_"},
            {"word_count": 5, "delimiter": "."},
            {"word_count": 6, "delimiter": "#"}
        ]
        
        for config in test_configs:
            passphrase = generate_passphrase(**config)
            
            # Log detailed passphrase analysis
            self.detailed_logger.log_password("Passphrase", passphrase, config)
            
            # Check word count
            words = passphrase.split(config["delimiter"])
            self.assertEqual(len(words), config["word_count"], 
                            f"Expected {config['word_count']} words but got {len(words)}")
            
            # Validate against policy
            validation = PasswordPolicyValidator.validate_passphrase(
                passphrase,
                min_words=config["word_count"],
                min_word_length=3
            )
            
            self.assertTrue(validation["valid"], 
                           f"Passphrase failed validation: {validation['issues']}")
    
    def test_spell_password_with_detailed_analysis(self):
        """Test spell password generation with detailed analysis."""
        # Test various lengths
        test_lengths = [10, 15, 20, 25]
        
        for length in test_lengths:
            spell = generate_spell(length=length)
            
            # Log detailed spell analysis
            self.detailed_logger.log_password("Spell", spell, {"length": length})
            
            # Check length
            self.assertEqual(len(spell), length, 
                            f"Expected length {length} but got {len(spell)}")
            
            # Validate against policy
            validation = PasswordPolicyValidator.validate_spell_password(
                spell,
                min_length=length
            )
            
            self.assertTrue(validation["valid"], 
                           f"Spell failed validation: {validation['issues']}")

if __name__ == '__main__':
    unittest.main()
