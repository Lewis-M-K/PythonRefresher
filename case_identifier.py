def determine_case(character):
    if character.lower() == character:
        print('The character is in lowercase.')
    elif character.upper() == character:
        print('The character is in uppercase.')
    else:
        print('The character is neither in lowercase or uppercace')

max_length = 1

while True:
        character = input("Enter any character: ")
        if len(character) != max_length:
            print('The input should be just one character')
        elif not character.isalpha():
            print('Please enter a character that is alphabetic')
        else:
             break
    
determine_case(character)
