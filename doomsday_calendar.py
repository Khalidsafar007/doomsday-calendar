# doomsday_calendar.py

WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def is_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def century_anchor(year: int) -> int:
    """
    Returns the century anchor day as 0=Sunday ... 6=Saturday.
    """
    c = year // 100
    return (5 * (c % 4) + 2) % 7

def year_doomsday(year: int) -> int:
    """
    Returns the weekday (0=Sunday ... 6=Saturday) of the Doomsday for the given year.
    """
    y = year % 100
    a = y // 12
    b = y % 12
    c = b // 4
    s = a + b + c
    return (century_anchor(year) + s) % 7

def month_doomsday_date(month: int, leap: bool) -> int:
    """
    Returns the 'doomsday date' within the given month.
    """
    if month == 1:
        return 4 if leap else 3
    if month == 2:
        return 29 if leap else 28
    table = {3: 14, 4: 4, 5: 9, 6: 6, 7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
    return table[month]

def weekday_of_date(year: int, month: int, day: int) -> str:
    leap = is_leap(year)
    doom = year_doomsday(year)
    md = month_doomsday_date(month, leap)
    diff = (day - md) % 7
    return WEEKDAYS[(doom + diff) % 7]

# ---- Main Program ----
if __name__ == "__main__":
    print("📅 Doomsday Calendar – Find the weekday for any date!")
    try:
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        weekday = weekday_of_date(year, month, day)
        print(f"{day:02d}-{month:02d}-{year} falls on a {weekday}.")
    except Exception as e:
        print("❌ Invalid input:", e)
