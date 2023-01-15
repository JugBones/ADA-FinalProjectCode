import tracemalloc

tracemalloc.start()
 
def bubble_sort(ArrInput):
    n = len(ArrInput)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if ArrInput[j] > ArrInput[j + 1]:
                swapped = True
                ArrInput[j], ArrInput[j + 1] = ArrInput[j + 1], ArrInput[j]
        if not swapped:
            return

ArrInput = input('Enter the list of numbers (separated with space): ').split()
ArrInput = [int(x) for x in ArrInput]
bubble_sort(ArrInput)

print('Sorted list: ', end='')
print(ArrInput)
print("Byte and peak",tracemalloc.get_traced_memory())
tracemalloc.stop()