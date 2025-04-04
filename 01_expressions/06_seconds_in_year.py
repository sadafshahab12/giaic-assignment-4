# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
def main():
  DAYS_IN_YEAR = 365
  HOURS_IN_DAY = 24
  MINUTES_IN_HOUR = 60
  SEC_PER_MINUTE = 60
  
  second_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SEC_PER_MINUTE
  print(f"There are {second_in_year} seconds in a year!")
  
if __name__ == "__main__":
  main()