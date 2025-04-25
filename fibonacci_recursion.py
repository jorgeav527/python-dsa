print(0)
print(1)
# count starting from 2
count = 2


def fibo(number_1, number_2):
    # get the count form globals context
    global count
    if count <= 19:
        new_number = number_1 + number_2
        print(new_number)
        number_1 = number_2
        number_2 = new_number
        count += 1
        fibo(number_1, number_2)
    else:
        return


fibo(0, 1)
