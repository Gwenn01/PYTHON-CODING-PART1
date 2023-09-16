def subset(arr):
    container = [[]]
    for i in range(len(arr)):
        for j in range(len(container)):
            # create a new list
            list = []
            # add the prev in container
            list.extend(container[j])
            list.append(arr[i])
            # the add to container
            container.append(list)
    return container

arr = [1, 2, 3]
print(subset(arr))