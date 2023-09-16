def permutation(p, up, index):
    if index == len(up):
        print(p)
        return
    ch = up[index]
    for i in range(len(p)+1):
        f = p[0 : i]
        s = p[i : len(p)]
        permutation(f + ch + s, up, index+1)
        
permutation("", "abc", 0)         