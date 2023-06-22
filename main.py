

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 30]
target = 9
index = binary_search(array, target)
if index != -1:
    print("Элемент", target, "найден в позиции", index)
else:
    print("Элемент", target, "не найден")
