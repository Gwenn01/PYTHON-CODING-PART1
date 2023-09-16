def two_sum(arr, target):
    result = []
    for i in range(len(arr)):
         for j in range(i+1, len(arr)):
               sum = arr[i] + arr[j]
               if sum == target:
                   result.append(i)
                   result.append(j)
                   break
    return result                   

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))
                                      