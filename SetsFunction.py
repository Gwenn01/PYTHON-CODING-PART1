# set = {} can't be edit one value in set
# union combining the two set
def union(set_one, set_two):
    edit_one = sorted(list(set_one))
    edit_two = sorted(list(set_two))
    result = []
    i = 0
    j = 0
    while i < len(edit_one) and j < len(edit_two):
        if edit_one[i] < edit_two[j]:
            result.append(edit_one[i])
            i += 1
        elif edit_two[j] < edit_one[i]:
            result.append(edit_two[j])
            j += 1
        else:
           result.append(edit_one[i])
           i += 1
           j += 1         

    while i < len(edit_one):
        result.append(edit_one[i])
        i += 1
    while j < len(edit_two):
        result.append(edit_two[j])
        j += 1                               
    return result                    
# difference returning the dif value in only one set
def difference(set_one, set_two):
    edit_one = sorted(list(set_one))
    edit_two = sorted(list(set_two))
    result = [] 
    for i in range(len(edit_one)):
        is_equal = False
        for j in range(len(edit_two)):
            if edit_one[i] == edit_two[j]:
                is_equal = True
                break                     
        if not is_equal:
            result.append(edit_one[i])
    return result
# intersection returning the same value 
def intersection(set_one, set_two):
    edit_one = sorted(list(set_one))
    edit_two = sorted(list(set_two))
    result = [] 
    for i in range(len(edit_one)):
        is_equal = False
        for j in range(len(edit_two)):
            if edit_one[i] == edit_two[j]:
                is_equal = True
                break                     
        if is_equal:
            result.append(edit_one[i])
    return result   
# difference returning the dif value in same set
def symmetric_difference(set_one, set_two):
    edit_one = sorted(list(set_one))
    edit_two = sorted(list(set_two))
    result = []
    for i in range(len(edit_one)):
        is_equal = False
        for j in range(len(edit_two)):
            if edit_one[i] == edit_two[j]:
                is_equal = True
                break                     
        if not is_equal:
            result.append(edit_one[i])
    i = 0
    j = 0   
    for i in range(len(edit_two)):
        is_equal = False
        for j in range(len(edit_one)):
            if edit_two[i] == edit_one[j]:
                is_equal = True
                break                     
        if not is_equal:
            result.append(edit_two[i])
    return result
# is disjoint return true if there is no same value in two set
def is_disjoint(set_one, set_two):
    edit_one = sorted(list(set_one))
    edit_two = sorted(list(set_two))
    for i in range(len(edit_one)):
        for j in range(len(edit_two)):
            if edit_one[i] == edit_two[j]:
                return False                 
    return True      
# is subset return if set one contains all the value in set two
def is_subset(set_one, set_two):
    edit_one = sorted(list(set_one))
    edit_two = sorted(list(set_two))
    for i in range(len(edit_one)):
        is_equal = False
        for j in range(len(edit_two)):
            if edit_one[i] == edit_two[j]:
                is_equal = True
                break
        if not is_equal:
             return False    
    return True      
# is subset return if set two contains all the value in set one
def is_superset(set_one, set_two):
    edit_one = sorted(list(set_one))
    edit_two = sorted(list(set_two))
    for i in range(len(edit_two)):
        is_equal = False
        for j in range(len(edit_one)):
            if edit_two[i] == edit_one[j]:
                is_equal = True
                break
        if not is_equal:
             return False    
    return True               
set_one = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_two = {2, 4, 6}
set_three = is_subset(set_one, set_two)
print(set_three)