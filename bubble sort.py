def bubble_sort(arr):
    for n in range(len(arr)):

        for i in range(len(arr)-n-1): #8-0-1-7
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i + 1]=temp

#another type of swap #arr[1], arr[1+1] arr[i+1], arr[i]

arr=[39, 12, 18, 85, 72, 18, 2, 18]

print("Unsorted list is:")

print(arr)
bubble_sort(arr)

print("Sorted list is:")

print(arr)
