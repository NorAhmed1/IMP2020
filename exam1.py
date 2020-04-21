#!/usr/bin/env python
# coding: utf-8

# ### Write a function to count the number 4 in a given list.

# In[2]:


def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))


# ### write a  function to check whether a number is divisible by another number.

# In[3]:


def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))


# ### write a function to find the maximum and minimum numbers from a sequence of numbers.

# In[4]:


def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))


# ### Write a Python function that takes two lists and returns True if they have at least one common member.

# In[5]:


def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))


# ### Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number from the user

# In[6]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# ### Write a Python function to check whether a number is in a given range.
# 
# ### The range is from 3 to 11
# 

# In[8]:


def test_range(n):
    if n in range(3,11):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)


# ### Write a  program to create the multiplication table (from 1 to 10) of a number.

# In[9]:


n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)


# ### Good Job!
