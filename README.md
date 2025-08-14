# 🗓 Doomsday Calendar (Python)

A Python implementation of **Conway’s Doomsday Algorithm** that calculates the day of the week for any given date between **year 5 and year 3500** (Gregorian calculation).

## 📌 Features
- Works for any date from **AD 5 to AD 3500**  
- Uses **Conway’s Doomsday Algorithm** for fast calculation  
- Handles leap years correctly  
- Simple **command-line interface** (CLI)  
- Validates dates to prevent invalid input (e.g., Feb 30)

## 🚀 Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Khalidsafar007/doomsday-calendar.git
cd doomsday-calendar
```

2️⃣ Run the script
```
python doomsday_calendar.py
```

3️⃣ Example
```
📅 Doomsday Calendar – Any date from year 5 to 3500 (Gregorian calculation)
Enter year (5-3500): 2025
Enter month (1-12): 3
Enter day (1-31): 1
01-03-2025 falls on a Saturday.
```
## 🧮 How the Algorithm Works
John Horton Conway’s **Doomsday Algorithm** is a mental method for determining the day of the week for any given date.

**Main idea:**
1. Each year has certain “Doomsday dates” that always fall on the same weekday.  
   Examples:
   - 4/4 (April 4)
   - 6/6 (June 6)
   - 8/8 (August 8)
   - 10/10 (October 10)
   - 12/12 (December 12)
   - Last day of February

2. The weekday for these dates is found by:
   - Determining the **century anchor day** (e.g., 1900s → Wednesday, 2000s → Tuesday)
   - Calculating an **offset** based on the year’s last two digits
   - Adjusting for leap years

3. Once the year’s Doomsday is known, you can find any other date by counting forward or backward to it.

**Example:**  
For 2025:
- Century anchor (2000s) = Tuesday  
- Year offset for 25 → add 3 days → Friday  
- 4/4/2025 is a Friday, so 1/3/2025 is a Saturday.


📜 License

This project is licensed under the MIT License.

