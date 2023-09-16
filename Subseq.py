def subset(p, up, i):
    if i == len(up):
        print(p)
        return 
    subset(p + up[i], up, i+1)
    subset(p, up, i+1)

subset("", "abc", 0)
     