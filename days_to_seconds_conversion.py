def convert_to_seconds(days):
    seconds = int(days)
    seconds = days * 60 ** 3
    return round(seconds, 3)

while True:
    try:
        days = float(input("Enter number of days: "))
        break
    except ValueError:
        print("Please enter a number value for the number of days days")

print(f'{days} days are equivalent to {convert_to_seconds(days)} seconds')
