def selection_sort(arr):
    n = len(arr)

    for i in range(0,n-1):
        small = i
        for j in range(i+1,n): 
            if arr[j]<arr[small]:
                small =    j
            arr[i],arr[small] = arr[small],arr[i]

arr=[1,25,89,96,36,2,45,77]

selection_sort(arr)

print(arr)


                