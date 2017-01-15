def merge(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(n1):
        L[i] = arr[start + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    i = j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    return arr

def mergesort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        return merge(arr, l, m, r)


if __name__ == "__main__":
    arr = [3, 6, 7, 8, 3, 4, 2, 3, 7, 8, 9]
    print(mergesort(arr, 0, len(arr)-1))