import math

def calculate_volume(radius):
    volume = (4/3 * math.pi * radius ** 3)
    volume = round(volume, 3)
    return volume

while True:
    try:
        radius = float(input("Enter value of the radius of the sphere: "))
        break
    except ValueError:
        print("Please enter a number value.")

print(f'The volume of a sphere with radius {radius} cm is {calculate_volume(radius)}cm³.')
