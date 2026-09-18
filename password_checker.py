import re
import getpass
import string


def check_password_strength(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Display result
    print("\n" + "=" * 40)

    if score <= 2:
        print("Password Strength: WEAK")
    elif score <= 4:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: STRONG")

    print(f"Security Score: {score}/5")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("- " + suggestion)
    else:
        print("\nExcellent! Your password meets all requirements.")

    print("=" * 40)


# Get password securely
password = getpass.getpass("Enter your password: ")

# Check password
check_password_strength(password)