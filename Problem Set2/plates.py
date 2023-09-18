import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length requirement
    if not 2 <= len(s) <= 6:
        return False

    # Check for invalid characters (periods, spaces, or punctuation marks)
    if not s.isalnum():
        return False

    # If there are numbers, ensure they are at the end and the first digit isn't '0'
    if re.search(r'^[A-Z]{2,}[1-9]\d*$', s):
        return True

    # If there are no numbers, ensure the plate starts with at least two letters
    elif re.search(r'^[A-Z]{2,}$', s):
        return True

    return False

main()
