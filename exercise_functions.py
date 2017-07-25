#Write merge sort function

def merge_sort(a):
  l = len(a)
  if l < 2:
    return a
  b = merge_sort(a[ :l/2])
  c = merge_sort(a[l/2: ])
  res = []
  i = 0
  j = 0
  while (i < len(b) and j < len(c)):
    if b[i] <= c[j]:
      res.append(b[i])
      i += 1
    else:
      res.append(c[j])
      j += 1
  while (i == len(b) and j < len(c)):
    res.append(c[j])
    j += 1
  while (i < len(b) and j == len(c)):
    res.append(b[i])
    i += 1
  return res
      
print merge_sort([8, 4, 1, 6, 3, 2, 5])    
  



'''If you are given two sorted lists of same size (N), 
write a program that combines the two lists into a single sorted 
list of size 2N.

def merge(a, b):
  res = []
  i = 0
  j = 0
  n = len(a)
  while (i < n and j < n):           
    if a[i] <= b[j]:
      res.append(a[i])
      i += 1
    elif a[i] > b[j]:
      res.append(b[j])
      j += 1
  while (i < n or j < n):
    if i < n:
      res.append(a[i])
      i += 1
    else:
      res.append(b[j])
      j += 1
  print(res)
  return res

merge([1, 2, 3], [4, 5, 6])
exit()'''

def combine_list(list1, list2):
  new_list = []
  length = len(list1)
  i = 0
  j = 0
  while (i < length and j < length):
    if list1[i] < list2[j]:
      new_list.append(list1[i])
      i += 1
    else:
      new_list.append(list2[j])
      j += 1
  while (i == length and j < length):
    new_list.append(list2[j])
    j += 1
  while (i < length and j == length):
    new_list.append(list1[i])
    i += 1
  print new_list
  
#combine_list([3,4,6], [1,2,8])  
#combine_list([3,4], [1,2])  
#combine_list([3,4,8], [1,2,6])  
#combine_list([1,2,3,4,5], [6,7,8,9,10])


'''Write a function that takes in a base and an exp and recursively 
computes baseexp. You are not allowed to use the ** operator!'''

def base_exp(base, exp):
  if exp == 0:
    return 1
  return base * base_exp(base, exp - 1)

#print base_exp(2, 10)



'''Write a function using recursion that takes in a string and 
returns a reversed copy of the string. The only string operation 
you are allowed to use is string concatenation.'''

def reverse_string(word):
  length = len(word)
  if length == 1:
    return word
  return word[length - 1] + reverse_string(word[:length - 1])

#print reverse_string("string")



'''Write a recursive function that determines whether an array is a
 palindrome, where the array and its size are given as parameters.'''

# returns true if the passed string is a palindrome, false otherwise
def is_palindrome(array):
  print array
  length = len(array)
  if length <= 1:
    return True
  elif array[0] == array[length - 1]:
    return is_palindrome(array[1 : length - 1])
  else:
    return False
  
#print is_palindrome("abcba")



'''Write a recursive function that computes and returns the sum 
of all elements in an array, where the array and its size are given 
as parameters.'''

def add_array(array):
  length = len(array)
  if length == 1:
    return array[0]
  return (array[length - 1] + add_array(array[:length - 1]))

#print add_array([1, 3, 5, 4, 2])



'''Write a recursive function that finds and returns the minimum 
element in an array, where the array and its size are given as 
parameters.'''

def min_array(list_array):
  length = len(list_array)
  if length == 1:
    return list_array[0]
  return min(list_array[length - 1], min_array(list_array[:length-1]))

#print min_array([11, 3, 5, 4, 25])



'''Write a recursive function that computes the sum of all numbers 
from 1 to n, where n is given as parameter.'''

def addition(n):
  if n == 1:
    return n
  return n + addition(n-1)

#print addition(5)



'''Write a function called digit_sum that takes a positive integer 
n as input and returns the sum of all that number's digits.
For example: digit_sum(1234) should return 10 which 
is 1 + 2 + 3 + 4.'''

def digit_sum(x):
    sum = 0
    while x / 10 > 0:
       sum = sum + (x % 10)
       x = x / 10
    else:
        sum += x
    return sum
       
print digit_sum(1234)


'''Define a function factorial that takes an integer x as input.
Calculate and return the factorial of that number.'''

def factorial(x):
    result = 1
    while x >= 1:
        result = result * x
        x = x - 1
    return result
    
print factorial(20)


'''Define a function which tells whether given number is prime 
or not.'''

def is_prime(x):
    if x >= 2:
        for n in range(2, x):
            if not (x % n):
                return False
    else:
        return False
    return True
