#!/usr/bin/env python
# coding: utf-8

# ## Python Basic Programming Exercises

# In[ ]:


pip install pandas


# In[110]:


import pandas as pd
import numpy as np

Q1: What is the output of following expression
    5 + 4 * 9 % (3 + 1) / 6 - 1
# In[1]:


5 + 4 * 9 % (3 + 1) / 6 - 1
   

Q2: Write a program to check if a Number is Odd or Even. Take number as a input from user at runtime.
# In[19]:


num = int(input("Enter the number here : "))
print(num , "is even") if num%2==0 else print(num , "is odd")

Q3: Write a program to display the multiplication table by taking a number as input. 
    [Hint : Use print statement inside of a loop]
# In[27]:


num1 = int(input("Enter your number here : "))

for i in range(1, 11, 1) :
    print(num1 , '*' , i , '=', num1 * i )

Q4: Write a program which will find all numbers between 2000 and 3200 which are divisible by 7 
    but are not a multiple of 5.
 
Note: The numbers obtained should be printed in a comma-separated sequence on a single line.
# In[43]:


for i in range(2000 , 3201 , 1 ) :
    if i % 7 == 0 and i % 5 != 0 :
        print(i , end = ",")
    

Q5: Count the elements of each datatype inside the list and display in output
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]    
# In[78]:


integer = []
string = []
floatt = []
boolean = []

for i in l :
    if type(i)== int :
        integer.append(i)
    elif type(i)== float :
        floatt.append(i)
    elif type(i) == str :
        string.append(i)
    else:
        boolean.append(i)

print("integer" , '=' , integer)
print("floatt" , '=' , floatt)
print("string" , '=' , string)
print("boolean",'=',boolean)

Q6: Add all values from the list with numeric datatypes 
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
# In[221]:


l = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]
ass = 0

for i in l :
    if (type(i) == int) or (type(i) == float) :
        ass = ass + i 
        
print(ass)

Q7: Concat all str datatypes with hyphen as a delimiter
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
# In[224]:


list1 = list([2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] )
strt = " "
for i in list1 :
    if type(i) == str:
        strt = strt + i + '-'

        
print(strt )

Q8: Write a UDF that takes list as input and returns sum of all numbers 
    (exclude bool) and count of all str 
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
    
Hint:
-----
def my_func:
    # your code
        
my_func(l1)
# output --> {'Sum': xxx, 'Count_of_Strs': xxx}
# In[258]:


def ques(l1):
    num = 0
    string = 0
    
    for i in l1:
        if (type(i) == float )or (type(i) == int ):
            num = num + i 
        elif type(i) == str:
            string = string + 1 
    d = {"sum" : num , "Count_of_str" : string}
    return( d)


# In[259]:


ques( [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7])

Q9: Get only odd numbers from the following list and store the numbers in new list
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

    i. Use loops to get the answer
   ii. Use list comprehensions
  iii. Use lambda function with filter
# In[261]:


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
l2 = []
for i in li:
    if i%2!=0:
        l2.append(i)
print(l2)


# In[264]:


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
[i for i in li if i % 2 != 0 ]


# In[ ]:




Q10: Write a UDF to return the descriptives [sum, count, min, mean, max] for a list of n number of input 
    numbers.
# In[295]:


def q10(lis):
    sums=0
    count=0
    mins=0
    maxs=0
    mean=0
    for i in lis :
        if (type(i) == int) or (type(i)== float) :
            sums = sums + i
    count = len(lis)
    mins = min(lis)
    maxs = max(lis)
    mean = np.mean(lis)
    
    result = {"Sum": sums  ,"Count" : count ,"Min" : mins , "Max" : maxs ,"Mean" :mean }
    return(result)


# In[296]:


q10([5, 7, 22, 97, 54, 62, 77, 23, 73, 61])

Q11: Write an udf to calculate the area of different shapes

Take shape and dimensions as arguments to udf as follows : 

1. square which has side
2. rectangle which has length and width
3. circle which has radius

The shape should be a positional argument and it's dimensions are taken as kwargs

Perform proper validation for the user inputs and then calculate area.

E.g. if shape is square, ensure kwargs has "side" and if so, then you may return the area, else display appropriate error message like "Please enter 'side' for a square"
# In[ ]:




Q12: Write a UDF to reconcile the values within two lists.
    l1 = ['January', 'February', 'March', 'May', 'June', 'September', 'December']
    l2 = ['January', 'February', 'April', 'June', 'October', 'December']

Hint:
-----
def func(l1, l2):
    your code here...
    
Output:
{'Matched': ['January', 'February', 'June', 'December'],
    'Only in l1': ['March', 'May', 'September'],
        'Only in l2': ['April', 'October']}
# In[297]:


def func(l1,l2) :
    s1 = set(l1)
    s2 = set(l2)
    Matched = s1.intersection(s2)
    Only_l1 = s1.difference(s2)
    Only_l2 = s2.difference(s1)
    
    d = {"Match" : list(Matched) , "Only_l1" : list(Only_l1) , "Only_l2 ": list(Only_l2) }
    
    return(d)

    


# In[298]:


func(['January', 'February', 'March', 'May', 'June', 'September', 'December'],['January', 'February', 'April', 'June', 'October', 'December'])

Q13: write a UDF to check if a number is prime or not.
# In[314]:


n = int(input("Enter your number here : "))
for i in range(2,n,1) :
    if n % i == 0 :
        print(n ,'is','not prime')
        break
else :
    print(n,'is','prime')
        


# In[325]:


def prime(n) :
    count = 0
    for i in range(2,n,1) :
        if n % i == 0 :
            count = count + 1
            break
    else:
            
        
        
    
    
    
    
    


# In[305]:


prime(5)

Q14. Write a program which can compute the factorial of a given numbers. 
#   The results should be printed in a comma-separated sequence on a single line. 
# input() function can be used for getting user(console) input


#Suppose the input is supplied to the program:  8  
#Then, the output should be:  40320 
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 

# In[2]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(result)

if __name__ == "__main__":
    main()

Q15. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

#Suppose the following input is supplied to the program: 8
#Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider using dict()


# In[3]:


def generate_squared_dict(n):
    squared_dict = {}
    for i in range(1, n + 1):
        squared_dict[i] = i * i
    return squared_dict

def main():
    num = int(input("Enter a number: "))
    squared_dict = generate_squared_dict(num)
    print(squared_dict)

if __name__ == "__main__":
    main()

Q16. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program: 34,67,55,33,12,98
    #Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. you may use tuple() method to convert list to tuple

# In[201]:


num = input("Enter your numbers : ")

list1 = list(num.split(sep = ','))
tup = tuple(num.split(sep = ','))

print(type(list1), list1 , type(tup ) , tup)

Q17. Write a program that accepts a comma separated sequence of words as input and 
# prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# In[195]:


csv = input("Enter your words :")
print(sorted(csv.split(sep = ',')))

Q18. Write a program that accepts a sequence of whitespace separated words 
# as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again
# Then, the output should be: again and hello makes perfect practice world

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
#We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# In[148]:


words = "hello world and practice makes perfect and hello world again"
split = words.split()
unique_words = set(split)
output = " ".join(sorted(unique_words))
print(output)

Q19. Write a program that accepts a sentence and calculate the number of upper case 
# letters and lower case letters.
#Suppose the following input is supplied to the program: Hello world!
#Then, the output should be: UPPER CASE 1 LOWER CASE 9

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# In[136]:


sent = input("Enter teh sentence here : ")
uppercase = 0
lowercase = 0
for i in sent :
    if i.isupper():
        uppercase = uppercase + 1
    elif i.islower():
        lowercase = lowercase + 1 
print(" Uppercase" ,'=', uppercase)
print(" Lowercase" , '=',lowercase)

