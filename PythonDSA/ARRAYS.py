# Q1. Given an array A[] of n numbers and another number x, the task is to check whether 
# or not there exist two elements in A[] whose sum is exactly x. 

# Examples: 

# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation:  If we calculate the sum of the output,1 + (-3) = -2

# Input: arr[] = {1, -2, 1, 0, 5}, x = 0
# Output: No

def question1():
    a=input()
    a=a.split(",")
    c=[]
    for i in a:
        c.append(int(i))
    d=sum(c)
    if d in c:
        e="yes"
    else:
        e="no"

    return e

# Q2 Find the majority element in the array. A majority element in an array 
# A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

# Examples : 

# Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size. 

# Input : {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is greater than the half of the size of the array size.

def question2():
    a=input()
    a=a.split(",")
    c=[]
    d={}
    for i in a:
        c.append(int(i))
    for i in c:
        d[i]=c.count(i)
    if max(d.values()) > len(d) :
        e=max(zip(d.values(), d.keys()))[1]
    else:
        e="No Majority Element"
    
    return e

# Q3 Given an array of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant space.

# Examples : 

# Input : arr = {1, 2, 3, 2, 3, 1, 3}
# Output : 3

# Input : arr = {5, 7, 2, 7, 5, 2, 5}
# Output : 5

def question3(arr, arr_size):
     
    for i in range(0,arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count+=1
             
        if (count % 2 != 0):
            return arr[i]
         
    return -1