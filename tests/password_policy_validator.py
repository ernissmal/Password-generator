import re
import string

class PasswordPolicyValidator:
    """Utility class for validating passwords against security policies."""
    
    @staticmethod
    def validate_standard_password(password, min_length=8, require_uppercase=True,
                                   require_lowercase=True, require_digits=True,
                                   require_special=True):
        """Validate standard password against security policies."""
        validation = {
            "valid": True,
            "issues": []
        }
        
        # Check length
        if len(password) < min_length:
            validation["valid"] = False
            validation["issues"].append(
                f"Password length ({len(password)}) is less than minimum required ({min_length})"
            )
        
        # Check for uppercase letters
        if require_uppercase and not any(c.isupper() for c in password):
            validation["valid"] = False
            validation["issues"].append("Password doesn't contain any uppercase letters")
        
        # Check for lowercase letters
        if require_lowercase and not any(c.islower() for c in password):
            validation["valid"] = False
            validation["issues"].append("Password doesn't contain any lowercase letters")
        
        # Check for digits
        if require_digits and not any(c.isdigit() for c in password):
            validation["valid"] = False
            validation["issues"].append("Password doesn't contain any digits")
        
        # Check for special characters
        if require_special and not any(c in string.punctuation for c in password):
            validation["valid"] = False
            validation["issues"].append("Password doesn't contain any special characters")
        
        return validation
    
    @staticmethod
    def validate_passphrase(passphrase, min_words=3, min_word_length=3):
        """Validate a passphrase against security policies."""
        validation = {
            "valid": True,
            "issues": []
        }
        
        # Split the passphrase into words (assuming common delimiters)
        words = re.split(r'[^\w]', passphrase)
        words = [w for w in words if w]  # Remove empty strings
        
        # Check word count
        if len(words) < min_words:
            validation["valid"] = False
            validation["issues"].append(
                f"Passphrase has only {len(words)} words, minimum required is {min_words}"
            )
        
        # Check word lengths
        short_words = [w for w in words if len(w) < min_word_length]
        if short_words:
            validation["valid"] = False
            validation["issues"].append(
                f"Passphrase contains {len(short_words)} words shorter than {min_word_length} characters"
            )
        
        return validation
    
    @staticmethod
    def validate_spell_password(spell, min_length=10):
        """Validate a spell-style password against security policies."""
        validation = {
            "valid": True,
            "issues": []
        }
        
        # Check length
        if len(spell) < min_length:
            validation["valid"] = False
            validation["issues"].append(
                f"Spell length ({len(spell)}) is less than minimum required ({min_length})"
            )
        
        # Check for special character at the end
        if not any(spell.endswith(c) for c in "!@#$%^&*()"):
            validation["valid"] = False
            validation["issues"].append("Spell doesn't end with a special character")
        
        # Check for capitalization (at least first letter should be uppercase)
        if not spell[0].isupper():
            validation["valid"] = False
            validation["issues"].append("Spell doesn't start with an uppercase letter")
        
        return validation
