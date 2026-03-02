#QUESTION 10
#Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how many days
# have passed since your birthday (without counting the days in your birth year and the current year, so just whole years).
#The function takes your birthday as a parameter in string format.
#Do not import anything, use only what we learned in class

def days_since_birthday(bday):
    # bday format: "DD-MM-YYYY"
    parts = bday.split("-")      # ["DD", "MM", "YYYY"]
    birth_year = int(parts[2])   # take the year part and convert to int

    # In class, we used a fixed "current year" number (ex: 2025 - int(age)) (Session5&6)
    current_year = 2026

    # "whole years only" means: do NOT count the birth year and do NOT count the current year
    whole_years = current_year - birth_year - 1

    days = whole_years * 365
    return days


print(days_since_birthday("12-12-2006")) # Example (My birthday)