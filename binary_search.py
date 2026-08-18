def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high ) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return -1

num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = binary_search(num, 60)
print("Index : ", result)