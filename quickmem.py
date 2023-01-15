
import tracemalloc



def quicksort(array):
    size=len(array)
    if size<=1:
        return array 
    else:
        pivot=array.pop()

    rightside=[]
    leftside=[]

    for item in array:
        if item>pivot:
            rightside.append(item)

        else:
            leftside.append(item)

    return quicksort(leftside)+[pivot]+ quicksort(rightside) 

ArrInput = input('Enter the list of numbers (separated with space): ').split()
ArrInput = [int(x) for x in ArrInput]
tracemalloc.start()

print(quicksort(ArrInput))

print(tracemalloc.get_traced_memory())


tracemalloc.stop()