def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
result = linear_search(arr, target)
print("Linear Search Result:", result)
