count = 1
list = []

while count <= 5:
    while True:
        try:
            value = float(input('Enter a value: '))
            list.append(value)
            count += 1
            break
        except ValueError:
            print('Please enter a number value')

average = sum(list)/len(list)
average = round(average, 3)
print(f'The average of the following values {list} is {average}')
