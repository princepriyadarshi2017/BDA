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

# Q4 There are two sorted arrays. First one is of size m+n containing only m elements. Another one is of size n and contains n elements. Merge these two arrays into the first array of size m+n such that the output is sorted. 
# Input: array with m+n elements (mPlusN[])
# NA => Value is not filled/available in array mPlusN[]. There should be n such array blocks.
# Input: array with n elements (N[]). 



# Q5 Given an array arr[] of size N, the task is to rotate the array by d position to the left.

# Examples: 
# Input:  arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3, 4, 5, 6, 7, 1, 2
# Explanation: If the array is rotated by 1 position to the left, 
# it becomes {2, 3, 4, 5, 6, 7, 1}.
# When it is rotated further by 1 position,
# it becomes: {3, 4, 5, 6, 7, 1, 2}
# Input: arr[] = {1, 6, 7, 8}, d

def question5():
    a=input("input array:- ")
    a=a.split(",")
    c=input("input number of position to the rotated from left")
    c=int(c)
    e=[]
    for i in a:
        e.append(int(i))
    d=[]
    for i in range(c,len(e)):
        d.append(e[i])
    d.extend(e[0:c])

    return d

# Q6 Write a program to print all the LEADERS in the array. An element is a leader 
# if it is greater than all the elements to its right side. And the rightmost element is always a leader. 
# For example:

# Input: arr[] = {16, 17, 4, 3, 5, 2}, 
# Output: 17, 5, 2

# Input: arr[] = {1, 2, 3, 4, 5, 2}, 
# Output: 5, 2

