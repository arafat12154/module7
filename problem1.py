seasons = ("Winter", "Spring", "Summer", "Autumn", "Winter")
month = int(input("Enter the month number (1-12): "))
if 1 <= month <= 12:
    season = seasons[(month - 1) // 3]
    print(f"The corresponding season is {season}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")