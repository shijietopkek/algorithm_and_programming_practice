#linearithmic

def binary_search(arr,target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else: #arr[mid] < target
            low = mid+1
    return None

def search_pair(arr, sumPair):
    for i in range(len(arr)):
        other_element = sumPair - arr[i]
        index = binary_search(arr[:i],other_element)
        if index != None:
            arr1 = [ [index, arr[index]], [i, arr[i]] ]
            return True, arr1
    return False

#main
print('Enter an array')
arr = [int(i) for i in input().split(' ')]
sumPair = int(input())

condition, result = search_pair(arr,sumPair)
if not condition:
    print('N')
else:
    print('Y')
    for i in result:
        print("pos: {}, val: {}".format(i[0],i[1]))
