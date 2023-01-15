import tracemalloc

tracemalloc.start()

def insertion_sort(ArrInput):
    for i in range(1, len(ArrInput)):
        temp = ArrInput[i]
        j = i - 1
        while (j >= 0 and temp < ArrInput[j]):
            ArrInput[j + 1] = ArrInput[j]
            j = j - 1
        ArrInput[j + 1] = temp
 
 
ArrInput = input('Enter the list of numbers (separated with space): ').split()
ArrInput = [int(x) for x in ArrInput]
insertion_sort(ArrInput)
print('Sorted list: ', end='')
print(ArrInput)
print("Byte and peak",tracemalloc.get_traced_memory())
tracemalloc.stop()
