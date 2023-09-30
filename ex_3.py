def count_letters(inputString):
    letter_count = {}
    inputString = inputString.lower()
    for char in inputString:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

user_input = input("Enter a string: ")
result = count_letters(user_input)
print(result)
