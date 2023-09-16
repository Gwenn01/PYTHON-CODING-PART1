def display_dup(sample_list):
    length = len(sample_list)
    for i in range(length):
        temp = sample_list[i]
        if temp in sample_list[i+1: length]:
            print(temp)

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
display_dup(sample_list)