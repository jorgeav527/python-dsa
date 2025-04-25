# Initialize variables number_1 and number_2 (0, 1)
number_1, number_2 = 0, 1
print(number_1)
print(number_2)

for i in range(18):
    # Calculate the next Fibonacci number
    new_number = number_1 + number_2
    print(new_number)
    # Update the variables for the next iteration
    number_1 = number_2
    number_2 = new_number
