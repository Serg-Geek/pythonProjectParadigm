

def count_li(arr: list,num:int):
    count = 0
    for i in range(len(arr)):
        if arr[i] == num:
            count += 1
    return count

def sort_buble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,10,11,12,13,14,15,16]
    print(count_li(arr, 12))

    print(sort_buble(arr))

