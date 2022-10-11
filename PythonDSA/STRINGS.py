#Q1 Remove duplicates from a given string
a=input()
b=[]
for i in a:
    b.append(i)
    remove=[]
for i in b:
    if i not in remove:
        remove.append(i)
removedup=""
for i in remove:
    removedup=removedup+i
print(removedup)

#Q2 Remove characters from the first string which are present in the second string
