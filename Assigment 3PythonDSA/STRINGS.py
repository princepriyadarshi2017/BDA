#Q1 Remove duplicates from a given string
from unittest import skip


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
a=input("First String:- ")
b=input("second String:- ")
a1=[]
for i in a:
    a1.append(i)
b1=[]
for i in b:
    b1.append(i)
c=[]
for i in a1:
    if i not in b1:
        c.append(i)

# Given a string s1 and a string s2, write a function to check whether s2 is a rotation of s1. 

def check_rotation(s, goal):
 
    if (len(s) != len(goal)):
        skip
 
    q1 = []
    for i in range(len(s)):
        q1.insert(0, s[i])
 
    q2 = []
    for i in range(len(goal)):
        q2.insert(0, goal[i])
 
    k = len(goal)
    while (k > 0):
        ch = q2[0]
        q2.pop(0)
        q2.append(ch)
        if (q2 == q1):
            return True
 
        k -= 1

# Write a program to print all permutations of a given string
def toString(List): 
    return ''.join(List) 
  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
def permute(a, l, r): 
    if l==r: 
        print (toString(a))
    else: 
        for i in range(l,r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] 

# # Reverse words in a given string
# Input: s = “geeks quiz practice code” 
# Output: s = “code practice quiz geeks”

