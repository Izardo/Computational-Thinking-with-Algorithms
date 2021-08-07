
'''
Sorting Algorithms

        1. Insertion Sort
        2. Quick Sort
        3. Bucket Sort
        4. Bubble Sort
        5. Merge Sort

Author: Isabella Doyle
'''

# Imports modules
import random

# Ref: "Insertion Sort In Python Explained (With Example And Code)" by FelixTechTips. Available at: https://www.youtube.com/watch?v=R_wDA-PmGE4
# Function sorts a given array... Explain 
def insertionSort(arr):
    
    # Iterates over elements in the given array starting at index 2
    for i in range(1, len(arr)):
        j = i
        
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

'''
def bubbleSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
'''

# Ref: random — Generate pseudo-random numbers https://docs.python.org/3/library/random.html 
# Generates an array of random numbers with a specified length
amount = 200
arr = []
for i in range(1, amount):
    num = random.randint(1, 1000)
    arr.append(num)
    print("Unsorted array: " , arr)
print("Sorted array: " , insertionSort(arr))
