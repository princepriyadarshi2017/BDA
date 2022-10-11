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

def question6(arr,size):    
    for i in range(0, size):
        for j in range(i+1, size):
            if arr[i]<=arr[j]:
                break
        if j == size-1:
            print (arr[i],end=' ')



#Q8 You are given an array of 0s and 1s in random order. 
# Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. Traverse array only once. 

# Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
# Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

def question8():
    a=input()
    a=a.split(",")
    b=[]
    for i in a:
        b.append(int(i))
    zero=[]
    one=[]
    for i in b:
        if i==0:
            zero.append(i)
        else:
            one.append(i)
    zero.extend(one)

    return zero


#Q9 Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i]. Solve it without division operator in O(n) time.

# Example : 

# Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}
# 3 * 5 * 6 * 2 product of other array 
# elements except 10 is 180
# 10 * 5 * 6 * 2 product of other array 
# elements except 3 is 600
# 10 * 3 * 6 * 2 product of other array 
# elements except 5 is 360
# 10 * 3 * 5 * 2 product of other array 
# elements except 6 is 300
# 10 * 3 * 6 * 5 product of other array 
# elements except 2 is 900













#Q10 You are given an array of n+2 elements. All elements of the array are in range 1 to n. And all elements occur once except two numbers which occur twice. Find the two repeating numbers. 

# Example:

# Input: 
# arr = [4, 2, 4, 5, 2, 3, 1] 
# n = 5
# Output:
# 4 2
# Explanation:
# The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice. So the output should be 4 2.







#Q11 Given a sorted array of n distinct integers where each integer is in the range from 0 to m-1 and m > n. Find the smallest number that is missing from the array. 

# Examples 

# Input: {0, 1, 2, 6, 9}, n = 5, m = 10 
# Output: 3

# Input: {4, 5, 10, 11}, n = 4, m = 12 
# Output: 0

# Input: {0, 1, 2, 3}, n = 4, m = 5 
# Output: 4

# Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11 
# Output: 8
a=[0, 1, 2, 6, 9]
m=10
for i in range(0,m):
    if i not in a:
        print(i)
        break



#Q12 Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

# Examples : 

#   Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
#   Output: 6  (j = 7, i = 1)

#   Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
#   Output: 8 ( j = 8, i = 0)

#   Input:  {1, 2, 3, 4, 5, 6}
#   Output: 5  (j = 5, i = 0)

#   Input:  {6, 5, 4, 3, 2, 1}
#   Output: -1 
