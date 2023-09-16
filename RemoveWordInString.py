def remove_word(p, s, word, i):
    #base condition
    if i == len(s):
        return p
    # check if start with that word 
    # then plus the i in the len of word
    if s[i : len(s)-1].startswith(word):
         return remove_word(p, s, word, i+len(word))
    else:
          return remove_word(p + s[i], s, word, i+1)
    
s = "aaapplebcdd"
word = "apple"
print(remove_word("", s, word, 0)) 