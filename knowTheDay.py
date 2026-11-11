from codes4daycalculator import normal_year_month_codes, leap_year_month_codes, century_codes, day_codes

Givendate = input("Enter the Date including year and month (e.g. 20 may 2021): ")

# .split() automatically makes a list, so we can unpack it directly
user_input = Givendate.lower().split()
DATe = int(user_input[0])  # Convert to integer for the addition later
Month = user_input[1]
GivenYear = user_input[2]

century_digits = int(GivenYear[:2])
Year = int(GivenYear[-2:])

# Use floor division (//) to count leap years, not modulo (%)
No_ofLeapyears_Happened = Year // 4

# Convert GivenYear to an integer to do the math properly
full_year = int(GivenYear)
is_leap_year = (full_year % 4 == 0 and full_year % 100 != 0) or (full_year % 400 == 0)

# Assign the correct dictionary based on the leap year check
if is_leap_year:
    current_month_codes = leap_year_month_codes
else:
    current_month_codes = normal_year_month_codes

# Fetch the codes
if Month in current_month_codes:
    month_code = current_month_codes[Month]

if century_digits in century_codes:  # Fixed the typo here
    century_code = century_codes[century_digits]

# Calculate the sum (using 'total_sum' since 'sum' is a built-in Python function)
total_sum = DATe + month_code + century_code + Year + No_ofLeapyears_Happened

# The most crucial mathematical step: divide by 7 and get the remainder
remainder = total_sum % 7

# Fetch the actual day using the remainder
if remainder in day_codes:
    Day = day_codes[remainder]
    print(f"It's {Day} on {Givendate}")
else:
    print("Could not calculate the day.")