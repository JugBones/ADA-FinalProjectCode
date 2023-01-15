import time

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

tic = time.perf_counter()
print('Sorted list: ', end='')
print(ArrInput)
toc = time.perf_counter()
print("time complexity for the algorithm is in", (toc - tic)*1000, "miliseconds")