def quick_sort(arr,a,b):
    if a>=b:
        return
    pivot=arr[b]
    left=a
    right=b-1
    while left<=right:
        while left<=right and arr[left]<pivot:
            left=left+1
        while left<=right and arr[right]>pivot:
            right=right-1
        if left<=right:
            arr[left],arr[right]=arr[right],arr[left]
            left=left+1
            right=right-1
    arr[left],arr[b]=arr[b],arr[left]
    quick_sort(arr,a,left-1)
    quick_sort(arr,left+1,b)
        

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

arr = [85, 24, 63, 45, 17, 31, 96, 50]
print("Given array is")
print_list(arr)

quick_sort(arr, 0, len(arr) - 1)
print("\nSorted array is")
print_list(arr)
