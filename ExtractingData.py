students = [
                    ["BSIT",["gwen", "ben"]],
                    ["BSCS", ["cpp", "java", "csharp"]]
                    ]

for i in range(len(students)):
    for j in range(len(students[i])):
         if j == 0:
             print(students[i][j])
         else:
             for k in range(len(students[i][j])):
                 print(" - " + students[i][j][k])