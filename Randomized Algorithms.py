import random
import sys
import time

# Function to swap_elements two elements in an array
def swap_elements(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


# Function to find the kth order statistic using the Floyd-Rivest Algorithm with Partition Method:
'''
The algorithm works by recursively partitioning the input array into subarrays based on a randomly selected
pivot element. It then narrows down the search range by focusing on the relevant subarray that contains the
desired element. This process continues until the k-th smallest element is found.
'''

def kthOrderStatistic(k, size, arr):
    size = size - 1

    # Partition the array using the last element as the pivot
    def partition(arr, low, high):
        # pivot = random.randrange(low, high)
        pivot_index = random.randint(low, high)  # Choose random pivot index
        swap_elements(arr, high, pivot_index)
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        swap_elements(arr, high, i+1)
        return i + 1

    if k > size or k<0:
        print("Invalid value of k")
        return -1

    # Recursive helper function to find the kth order statistic
    def get_kth_order(arr, low, high, k):
        if low == high:
            return arr[low]

        pivot = partition(arr, low, high)

        if k == pivot:
            return arr[pivot]
        elif k < pivot:
            return get_kth_order(arr, low, pivot - 1, k)
        else:
            return get_kth_order(arr, pivot + 1, high, k)

    return get_kth_order(arr, 0, size, k)



# Second Method : Floyd-Rivest Without Separate Partition Method

def FloydRivest_Without_Partition_Method(k, size, arr):
    size = size - 1
    if k > size or k<0:
        print("Invalid value of k")
        return -1
    def kthOrderStatistic_(arr, low, high, k):
        while high > low:
            pivot_index = random.randint(low, high)  # Choose random pivot index
            pivot = arr[pivot_index]  # Get pivot element
            left = low
            right = high

            # Move pivot to the leftmost position
            swap_elements(arr, low, pivot_index)
            if arr[high] > pivot:
                swap_elements(arr, high, low)
            # Find the correct position of the pivot
            while left < right:
                swap_elements(arr, left, right)
                left = left + 1
                right = right - 1

                while arr[left] < pivot:
                    left = left + 1
                while arr[right] > pivot:
                    right = right - 1
            if arr[low] == pivot:
                swap_elements(arr, low, right)
            else:
                right = right + 1
                swap_elements(arr, high, right)
            if right <= k:
                low = right + 1
            if k <= right:
                high = right - 1
        return arr[k]
    return kthOrderStatistic_(arr, 0, size, k)



# Function to find the kth order statistic using the naive Bubble Sort algorithm
def Naive_Method_Bubble_Sort(k, size, arr):
    if k > (size-1) or k < 0:
        print("Invalid value of k")
        return -1

    size = len(arr)
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr[k]



# Function to find the kth order statistic using Python's inbuilt sorted() method
def Python_Inbuilt_Method(k, size, arr):
    if k > (size-1) or k < 0:
        print("Invalid value of k")
        return -1

    sorted(arr)  # Sort the array in-place
    return arr[k]



# Check if command line arguments are provided correctly
if len(sys.argv) < 4:
    print("Usage: python M22MA003.py K size arr[1] arr[2] ... arr[size]")
    sys.exit(1)

# Get values of k, size, and array from command line arguments
k = int(sys.argv[1])
size = int(sys.argv[2])
args = sys.argv[3:]
arr = [int(arg) for arg in args]


print("\nFloyd-Rivest Algorithm without Partition Method:-")

begin = time.time()
result = FloydRivest_Without_Partition_Method(k, size, arr)
finish = time.time()

print(result)
print(f"Time : {finish - begin}")

print("\nkthOrderStatistic Method : Floyd-Rivest Algorithm :-")

begin = time.time()
result = kthOrderStatistic(k, size, arr)
finish = time.time()

print(result)
print(f"Time : {finish - begin}")


print("\nNaive Method : Base is Bubble Sort Algo:-")

begin = time.time()
result = Naive_Method_Bubble_Sort(k, size, arr)
finish = time.time()

print(result)
print(f"Time : {finish - begin}")

print("\nPython Inbuilt Sorted Method")
begin = time.time()
result = Python_Inbuilt_Method(k, size, arr)
finish = time.time()

print(result)
print(f"Time : {finish - begin}")



######################################----OUTPTS----######################################


'''
Test 1: k=5

python3 M22MA003.py 5 10 3 4 5 2 0 6 1 7 9 8

Floyd-Rivest Algorithm without Partition Method:-
5
Time : 4.696846008300781e-05

kthOrderStatistic Method : Floyd-Rivest Algorithm :-
5
Time : 2.09808349609375e-05

Naive Method : Base Bubble Sort Algo:-
5
Time : 9.059906005859375e-06

Python Inbuilt Sorted Method
5
Time : 2.1457672119140625e-06

Result : kthOrderStatistic Floyd-Rivest Method Performs Best



Test 2: k=0

python3 M22MA003.py 0 10 3 4 5 2 0 6 1 7 9 8

Floyd-Rivest Algorithm without Partition Method:-
0
Time : 5.5789947509765625e-05

kthOrderStatistic Method : Floyd-Rivest Algorithm :-
0
Time : 1.52587890625e-05

Naive Method : Base Bubble Sort Algo:-
0
Time : 1.1920928955078125e-05

Python Inbuilt Sorted Method
0
Time : 3.0994415283203125e-06

Result : kthOrderStatistic Floyd-Rivest Method Performs Best


Test 3: k=11 when size=11

python3 M22MA003.py 11 11 3 4 5 2 0 6 1 7 9 8 14

Floyd-Rivest Algorithm without Partition Method:-
Invalid value of k
-1
Time : 8.821487426757812e-06

kthOrderStatistic Method : Floyd-Rivest Algorithm :-
Invalid value of k
-1
Time : 3.814697265625e-06

Naive Method : Base Bubble Sort Algo:-
Invalid value of k
-1
Time : 2.86102294921875e-06

Python Inbuilt Sorted Method
Invalid value of k
-1
Time : 3.0994415283203125e-06

Result : Return -1

Test 4 : Larger Array

python3 M22MA003.py 11 40 3 4 5 2 0 6 1 7 9 8 14 16 15 17 10 11 23 47 54 82 13 26 38 42 44 22 49 37 31 42 47 18 25 35 40 29 33 45 41 49

Floyd-Rivest Algorithm without Partition Method:-
11
Time : 5.817413330078125e-05

kthOrderStatistic Method : Floyd-Rivest Algorithm :-
11
Time : 2.9087066650390625e-05

Naive Method : Base Bubble Sort Algo:-
11
Time : 8.0108642578125e-05

Python Inbuilt Sorted Method
11
Time : 3.0994415283203125e-06

Result : kthOrderStatistic Floyd-Rivest Method Performs Best

'''