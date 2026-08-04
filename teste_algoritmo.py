def find_min(array, start=0):
    min_pos = start

    for i in range(start, len(array)):
        if array[i] < array[min_pos]:
            min_pos = i
            

    return min_pos

#Swap adjacent elements if they're not in order
#O(N**2) time complexity

def bubble_sort(array):
    for _ in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

#Set a pivot (Starting at 1)
#Iterate through elements to the left of the pivot, in descending order
#Check if the current element is greater than the pivot
#If it is, move the current element to the right
#Then, move the pivot to the spot where the current element was
#O(N**2) time complexity

def insertion_sort(array):
    pivot = 0

    for i in range(1, len(array)):
        pivot = array[i]

        for j in range(i, -1, -1):
            if array[j] > pivot:
                array[j+1] = array[j]
                array[j] = pivot



#Iterate through each element in the array
#Find the smallest number in i to len(array) range
#Swap the element in i with the smallest number
#O(N**2) time complexity

def selection_sort(array):
    min_pos = 0

    for i in range(len(array)):
        min_pos = find_min(array, i)
        array[i], array[min_pos] = array[min_pos], array[i]
        
        
    

#Set a pivot (Normally the last element of the array, in this case as well)
#The goal is to find the final resting spot for this pivot
#Create 2 iterators, i and j
#j will begin at 0, and i will being at j-1
#Check if the pivot is greater than j
#If it is, increment i and swap i element with j element
#At the end of each iteration of the while loop, increment j
#After the while loop ends, the final resting spot for the pivot will be found (i+1)
#Swap the element in i+1 with the pivot
#Recursevly call quick_sort twice: one on the subarray to the right of the pivot, and the other on the subarray to the left of the pivot. 
#The recursion's convergence case will be if the absolute value of the start index and end index of the current quick_sort call will be less than or equal to 1.
#O(nlog(n)) time complexity and O(log(n)) space complexity. However, this algorithm has an O(N**2) time complexity in the worst case scenario, which is if the array is already sorted.

def quick_sort(array, start, end):
    
    if abs(start - end) <= 1:
        return

    pivot = end-1

    i = start-1
    j = start

    while array[j] != array[pivot]:
        if array[pivot] > array[j]:
            i += 1
            array[i], array[j] = array[j], array[i]
        
        j += 1
    
    i += 1
    array[i], array[pivot] = array[pivot], array[i]
    
    quick_sort(array, start, i)
    quick_sort(array, i+1, end)