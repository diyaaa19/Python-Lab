class BubbleSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

bubble_sort = BubbleSort()
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort.sort(arr)
print("Bubble Sort Result:", sorted_arr)
