array = [7, 3, 9, 12, 11, 1]

n = len(array)
print(range(n - 1))

for i in range(n - 1):
    print(f"outer loop {i}")
    print("list to loop outer: ", list(range(n - 1)))
    swapped = False
    for j in range(n - i - 1):
        print(f"inner loop {j}")
        print("list to loop inner: ", list(range(n - i - 1)))
        if array[j] > array[j + 1]:
            print("actual state: ", array[j], array[j + 1])
            array[j], array[j + 1] = array[j + 1], array[j]
            print("new state: ", array[j], array[j + 1])
            swapped = True
    if not swapped:
        break
