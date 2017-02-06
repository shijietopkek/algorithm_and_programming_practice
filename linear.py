#linear

def search_pair(arr, sumPair):
    for i in range(len(arr)):
        other = sumPair - arr[i]
        if other in arr:
            arr1 = [ [i,arr[i]] , [arr.index(other), other] ]
            return True, arr1
    return False, None

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
