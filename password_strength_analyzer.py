
import re

def password_strength(password):
    strength = 0
    # Patterns
    patterns = {
        "length": r".{8,}",            # At least 8 characters
        "lower": r"[a-z]",             # At least one lowercase letter
        "upper": r"[A-Z]",             # At least one uppercase letter
        "digit": r"\d",               # At least one digit
        "special": r"[@$!%*?&]"        # At least one special character
    }
    
    # Check each criterion
    if re.search(patterns["length"], password):
        strength += 1
    if re.search(patterns["lower"], password):
        strength += 1
    if re.search(patterns["upper"], password):
        strength += 1
    if re.search(patterns["digit"], password):
        strength += 1
    if re.search(patterns["special"], password):
        strength += 1

    # Display results
    if strength == 5:
        return "Strong"
    elif 3 <= strength < 5:
        return "Moderate"
    else:
        return "Weak"

# Example usage
if __name__ == "__main__":
    password = input("Enter password to check strength: ")
    print("Password strength:", password_strength(password))
