def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >=0 and key < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = key
    return a

def bubble_sort(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                a[i],a[j] = a[j],a[i]
    return a

def selection_sort(a):
    for i in range(0,len(a)):
        min_index = i
        for j in range(i+1,len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i],a[min_index] = a[min_index], a[i]
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = a[:mid]
    right = a[mid:]
 
    return mergeSortedArray(merge_sort(left),merge_sort(right))
 
def mergeSortedArray(left, right):
    sorted_array = [None]*(len(left)+len(right))
    i = j = k = 0
 
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            sorted_array[k] = left[i]
            i+=1
        else:
            sorted_array[k] = right[j]
            j+=1
        k+=1
 
    while i<len(left):
        sorted_array[k] = left[i]
        i+=1
        k+=1
    
    while j<len(right):
        sorted_array[k] = right[j]
        j+=1
        k+=1
 
    return sorted_array

def partition(a, low, high, pivot):
    i = low+1
    j = high
    
    while j>= i:
        if a[i] > a[pivot] and a[j] < a[pivot]:
            swap(i,j,a)
        
        if a[i] <= a[pivot]:
            i +=1
        
        if a[j] >= a[pivot]:
            j-=1
        
    swap(pivot,j,a)
    return j

def swap(i,j,a):
    a[i],a[j] = a[j],a[i]

def quick_sort(a):
    low = 0
    high = len(a)-1
    return quick_sort_helper(a,low, high)

def quick_sort_helper(a, low, high):
    if low < high:
        p = partition(a, low, high, low)
        quick_sort_helper(a, low, p-1)
        quick_sort_helper(a, p+1, high)
    
    return a

def run_sort(sorting_algo, a):
    return sorting_algo(a)

def heapify(a, n, i):
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2
  
    if l < n and a[i] < a[l]:
        largest = l
  
    if r < n and a[largest] < a[r]:
        largest = r
  
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        heapify(a, n, largest)

def heap_sort(a):
    n = len(a)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
 
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
    
    return a