days = {'january': 31, 'february': 28,'march':31, 
        'april': 30, 'may': 31, 'june': 30, 'july': 31 , 
        'august': 31, 'september': 30, 'october': 31, 'november': 30, 
        'december': 31}

user_month = input("Enter a month name: ").lower()
if user_month in days:
    print(f"There are {days[user_month]} days in {user_month.capitalize()}.")
else:
    print("Invalid month name.")

print()

print("Months in alphabetical order:")
for month in sorted(days.keys()):
    print(month.capitalize())

print()

print("Months with 31 days:")
for month, days_count in days.items():
    if days_count == 31:
        print(month.capitalize())

print()
sorted_months = sorted(days.items(), key=lambda x: x[1])

print("Months sorted by the number of days:")
for month, days_count in sorted_months:
    print(f"{month.capitalize()}: {days_count} days")
