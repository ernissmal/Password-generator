import logging
import string
import math
import re

class PasswordAnalyzer:
    """Utility class for analyzing and logging password characteristics."""
    
    @staticmethod
    def analyze_password(password):
        """Analyze password characteristics and return detailed metrics."""
        metrics = {
            "length": len(password),
            "uppercase_count": sum(1 for c in password if c.isupper()),
            "lowercase_count": sum(1 for c in password if c.islower()),
            "digit_count": sum(1 for c in password if c.isdigit()),
            "special_char_count": sum(1 for c in password if c in string.punctuation),
            "unique_chars": len(set(password)),
            "entropy_bits": PasswordAnalyzer.calculate_entropy(password)
        }
        return metrics
    
    @staticmethod
    def calculate_entropy(password):
        """Calculate the entropy (bits of randomness) in a password."""
        # Count the character sets being used
        has_uppercase = any(c.isupper() for c in password)
        has_lowercase = any(c.islower() for c in password)
        has_digits = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        # Calculate the character pool size
        pool_size = 0
        if has_uppercase:
            pool_size += 26  # A-Z
        if has_lowercase:
            pool_size += 26  # a-z
        if has_digits:
            pool_size += 10  # 0-9
        if has_special:
            pool_size += 33  # Special characters
            
        # Calculate entropy
        if pool_size == 0:  # Shouldn't happen but just in case
            return 0
        return len(password) * math.log2(pool_size)

class DetailedTestLogger:
    """Logger class with enhanced password logging capability."""
    
    def __init__(self, logger):
        """Initialize with an existing logger."""
        self.logger = logger
        self.analyzer = PasswordAnalyzer()
    
    def log_password(self, password_type, password, parameters=None):
        """Log detailed information about a generated password."""
        self.logger.info(f"\n{'='*20} {password_type.upper()} PASSWORD {'='*20}")
        self.logger.info(f"Generated password: {password}")
        
        # Log parameters if provided
        if parameters:
            self.logger.info("Parameters used:")
            for key, value in parameters.items():
                self.logger.info(f"  {key}: {value}")
        
        # Analyze and log password metrics
        metrics = self.analyzer.analyze_password(password)
        self.logger.info("Password analysis:")
        self.logger.info(f"  Length: {metrics['length']} characters")
        self.logger.info(f"  Uppercase letters: {metrics['uppercase_count']}")
        self.logger.info(f"  Lowercase letters: {metrics['lowercase_count']}")
        self.logger.info(f"  Digits: {metrics['digit_count']}")
        self.logger.info(f"  Special characters: {metrics['special_char_count']}")
        self.logger.info(f"  Unique characters: {metrics['unique_chars']}")
        self.logger.info(f"  Entropy: {metrics['entropy_bits']:.2f} bits")
        
        # Strength assessment
        strength = "Very weak"
        if metrics['entropy_bits'] >= 128:
            strength = "Very strong"
        elif metrics['entropy_bits'] >= 80:
            strength = "Strong"
        elif metrics['entropy_bits'] >= 60:
            strength = "Moderate"
        elif metrics['entropy_bits'] >= 40:
            strength = "Weak"
            
        self.logger.info(f"  Assessed strength: {strength}")
        self.logger.info("="*60)
