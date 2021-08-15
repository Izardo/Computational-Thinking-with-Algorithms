
'''
Section 1: Sorting Algorithms

        1. Insertion Sort
        2. Quick Sort
        3. Bucket Sort
        4. Bubble Sort
        5. Merge Sort

Section 2: Benchmarking

Author: Isabella Doyle
'''

# Imports modules
import time
import random
import numpy as np
import pandas as pd


''' 
1. Insertion Sort algorithm | Ref: [1]
'''

def insertionSort(arr):
    
    # Iterates over elements in the given arr starting at index 2
    for i in range(1, len(arr)):
        
        while arr[i - 1] > arr[i] and i > 0:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1  # Moves down one index
    
    return arr

''' 
2. Quick Sort algorithm | Ref: [2]
'''

def quickSort(arr):
    
    # Base case for recursion when the array contains one item
    if len(arr) < 2:       
        return arr
    else:
        
        # Chooses random value in array to use as pivot(position of partition)
        pivot = random.choice(arr)  

        # Empty lists to store partitioned arrays        
        less = []
        pivotList = []
        more = []

        # Partitioning loop creates smaller arrays
        for i in arr: 
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        
        # Recursively calls function breaking down arrays into smaller arrays & sorts them
        less = quickSort(less)
        more = quickSort(more)

        # Merges ordered lists into one sorted list
        return less + pivotList + more

'''
3. Bucket Sort algorithm | Ref: [3]
'''

def bucketSort(arr):
    
    # Finds biggest value in the arr, using length of list to decide what value is placed into each bucket
    maximum = max(arr)
    size = maximum / len(arr)

    # Creates empty buckets corresponding with length of input list
    bucketList = []
    for x in range(len(arr)):
        bucketList.append([]) 

    # Places the items in the arr into the appropriate bucket depending on its size
    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            bucketList[j].append(arr[i])
        else:
            bucketList[len(arr) - 1].append(arr[i])

    # Sorts items in each bucket using the insertionSort() function
    for k in range(len(arr)):
        insertionSort(bucketList[k])
            
    # Concatenates the sorted items from each bucket to form one sorted arr
    final = []
    for l in range(len(arr)):
        final = final + bucketList[l]
    return final

'''
4. Bubble Sort algorithm | Ref: [4]
'''

def bubbleSort(arr):
    
    for i in range(len(arr)):
    
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr

'''
5. Merge Sort algorithm | Ref: 5
'''

# This part of the mergeSort alogrithm carries out the sorting of the elements in the array
def merge(left, right): # Takes in two lists from the mergeSort() function
    
    # If left arr is empty return right
    if len(left) == 0:
        return right

    # If second is empty return left arr
    if len(right) == 0:
        return left

    result = []     # Empty list that stores result of merge
    indexLeft = 0   # Pointers 
    indexRight = 0  

    
    while len(result) < len(left) + len(right):
        

        if left[indexLeft] <= right[indexRight]:
            result.append(left[indexLeft])
            indexLeft += 1
        else:
            result.append(right[indexRight])
            indexRight += 1

        # If you reach the end of either arr, then you can
        # add the remaining elements from the other arr to
        # the result and break the loop
        if indexRight == len(right):
            result += left[indexLeft:]
            break

        if indexLeft == len(left):
            result += right[indexRight:]
            break

    return result

# This part of the merge sort algorithm uses the 'divide and conquer' method
def mergeSort(arr):
    
    # Base case if array has less than 2 items
    if len(arr) < 2:
        return arr

    midpoint = len(arr) // 2    # Identifies midpoint of array

    # Using recursion the partitioned portions of the array are 
    # broken down until they are individual components, after being
    # re-organised with mergeSort() function, two arrays (left and right) 
    # are returned and merged together to create a final sorted list
    return merge(
        left = mergeSort(arr[:midpoint]),
        right = mergeSort(arr[midpoint:]))

'''
Benchmarking the sorting algorithms
'''

# Generates an array of random numbers with parameters for size & min/max values
def genRandomArr(n):
    
    # Creates empty array
    arr = []
    
    # Creates random numbers n times & appends them to 'arr'
    for i in range(0, n):
        num = random.randint(0, 100)
        arr.append(num)
    
    # Returns array to caller
    return arr

# Times algorithm
def timeAlgo(algo, arr):
    
    # Starts timing
    start = time.time()
    
    # Executes algorithm
    algo(arr)
    
    # Ends timing
    end = time.time()
    totalTime = end - start
    return totalTime

# Main program
def main():

    # Array of various input sizes for random number generator
    input = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]

    # Arrays to store results from benchmark
    insertionTimes = []
    quickTimes = []
    bucketTimes = []
    bubbleTimes = []
    mergeTimes = []

    # Loops over input array
    for n in input:

        # Generates random arrays with genRandomArr() function & sizes specified in the 'input' array 
        inputArr = genRandomArr(n)

        # Stores 10 run-time values temporarily for each algorithm
        insertionTemp = []
        quickTemp = []
        bucketTemp = []
        bubbleTemp = []
        mergeTemp = []

        # Executes & times each algorithm 10X for each size specified in 'input' 
        # array & appends result of each execution to the temporary lists
        for j in range(10):
            #insertionTemp.append(timeAlgo(insertionSort, inputArr))
            #quickTemp.append(timeAlgo(quickSort, inputArr))
            #bucketTemp.append(timeAlgo(bucketSort, inputArr))
            bubbleTemp.append(timeAlgo(bubbleSort, inputArr))
            #mergeTemp.append(timeAlgo(mergeSort, inputArr))
        print(j, "bubble", bubbleTemp)  

# Initiates program       
#if __name__ == "__main__":
    main()
arr = genRandomArr(10)
print(arr)
print(bucketSort(arr))
'''
REFERENCES

[1] "Insertion Sort In Python Explained (With Example And Code)" by FelixTechTips. Available at: https://www.youtube.com/watch?v=R_wDA-PmGE4
[2] https://brilliant.org/wiki/quick-sort/
[3] https://stackabuse.com/bucket-sort-in-python/
[4] Code adapted from https://stackabuse.com/bubble-sort-in-python
[5] https://realpython.com/sorting-algorithms-python/
[6] "Random - Generate pseudo-random numbers" https://docs.python.org/3/library/random.html

'''

### THIS FOR BENCHMARKING AND EVERYTHING: https://realpython.com/sorting-algorithms-python/