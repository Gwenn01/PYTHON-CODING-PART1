s = "python"
for i in range(1, len(s)+1):
    for j in range(0, i):
        print(s[j], end="")
    print()
for i in range(1, len(s)+1):
    for j in range(0, len(s)-i):
        print(s[j], end="")
    print()

