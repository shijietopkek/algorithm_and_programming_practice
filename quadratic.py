#quadratic

def search_pair(arr, sumPair):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] + arr[j] == sumPair:
                arr1= [ [i,arr[i]],[j,arr[j]] ]
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
