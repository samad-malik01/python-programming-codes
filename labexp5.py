'''Write a program to perform searching activity using Linear and binary search.'''

 # Linear Search

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Binary Search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main Program
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

# Linear Search
result = linear_search(arr, key)

if result != -1:
    print("Linear Search: Element found at position", result + 1)
else:
    print("Linear Search: Element not found")


# Binary Search
arr.sort()
result = binary_search(arr, key)

if result != -1:
    print("Binary Search: Element found at position", result + 1)
else:
    print("Binary Search: Element not found")