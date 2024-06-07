def  binary_search(list, num):
    l= 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u)//2
        if list[mid] == num:
            return mid
        elif list[mid] < num:
            l = mid + 1
        else:
            u = mid -1 

list=[20,25,66,100,525,365,900,1005]

num = 1005

index = binary_search(list, num)

print("Index of given number is:", index)




