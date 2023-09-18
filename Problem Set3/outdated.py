import re

def main():
    while True:
        date = input("Date: ")
        iso_date = convert_to_iso(date)
        if iso_date:
            print(f"{iso_date}",end = "")
            break
        else:
            pass

def convert_to_iso(date):
    # Attempt to match MM/DD/YYYY format
    match1 = re.match(r'(\d{1,2})/(\d{1,2})/(\d{4})', date)
    # For Month DD, YYYY format
    match2 = re.match(r'(\w+) (\d{1,2}), (\d{4})', date)

    if match1:
        first, second, year = match1.groups()
        # Check if it's in DD/MM/YYYY format
        if int(first) > 12:
            day, month = first, second
        # Otherwise, it's in MM/DD/YYYY format
        else:
            month, day = first, second
    elif match2:
        month, day, year = match2.groups()
        month = month_to_number(month)
        if not month:
            return None
    else:
        return None

    # Check day value
    if not 1 <= int(day) <= 31:
        return None

    return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

def month_to_number(month):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    try:
        return str(months.index(month) + 1)
    except ValueError:
        return None

main()
