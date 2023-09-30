def get_valid_int_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

sum_result = 0

for i in range(5):
    user_input = get_valid_int_input(f"Enter integer #{i + 1}: ")
    sum_result += user_input

print("Your Sum is :", sum_result)
