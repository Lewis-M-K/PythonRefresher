def calculate_perimeter(side):
    perimeter = side * 4
    return round(perimeter, 3)

def calculate_area(side):
    area = side ** 2
    return round(area, 3)

while True:
    try:
        side = float(input("Enter value of the side of the square: "))
        break
    except ValueError:
        print("Please enter a number value")

print(f'The perimeter of a square with side {side} cm is {calculate_perimeter(side)} cm.')
print(f'The area of a square with side {side} cm is {calculate_area(side)} cm².')
