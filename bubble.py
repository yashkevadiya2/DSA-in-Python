def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range (0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break

arr = [20,25,1,2,89,56,75]

arris = bubble_sort(arr)

print(arr)