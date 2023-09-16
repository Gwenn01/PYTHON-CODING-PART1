def countCharOccurances(char, string):
    count = 0
    for s in string: 
        if s == char: 
            count+=1
    return count
    
char = 'o'
string = "hello world"
print(countCharOccurances(char, string))