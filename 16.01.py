'''1. Find the Missing Number
Given an array of n-1 numbers in the range 1 to n, find the missing number.
Example:
arr = [1, 2, 4, 5]
# Missing number is 3

'''
nu=int(input("ENter the number of elements in the array:"))
nums=[]
for i in range(nu):
    l=int(input(f"Enter the elements in the array{i+1}:"))
    nums.append(l)
    n=len(nums)+1
    expected_sum=n*(n+1)//2
    actual_sum=sum(nums)
    missing_num=expected_sum-actual_sum
print(missing_num)


'''2. Find the Duplicates
Given an array where each number appears twice except one number, find the number that appears once.
arr = [4, 3, 2, 7, 8, 2, 3]
# 4 and 7 are the numbers that appear once'''
n = int(input("Enter the number of elements in the array: "))
num = []
for i in range(n):
    l = int(input(f"Enter value {i+1}: "))
    num.append(l)
for nu in num:
    count = num.count(nu)
    if count == 1:
        print(nu, "occurred 1 time")
    else:
        print(nu, "occurred", count, "times")
'''3. Check if Array is Sorted
Check whether a given array is sorted in ascending order.

Example:
arr = [1, 2, 3, 4]
# Output: True
'''
n = int(input("Enter the number of elements in the array: "))
num = []
for i in range(n):
    l = int(input(f"Enter value {i+1}: "))
    num.append(l)
if num==sorted(num):
    print("True")
else:
    print("False")

'''4. Find the Majority Element
Given an array, find the majority element (the element that appears more than n//2 times).
	
Example:
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# Output: 4
'''
n = int(input("Enter the number of elements in the array: "))
num = []
for i in range(n):
    l = int(input(f"Enter value {i+1}: "))
    num.append(l)
for nu in set(num):
    count = num.count(nu)
    if count > 1:
        print(nu)
    
