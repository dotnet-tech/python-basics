#Sample
'''
x < y <= z is equivalent to x < y and y <= z,
'''

#Difference between == and is operator 
'''
    The == operator compares the values of both the operands and checks for value equality. Whereas is operator checks whether both the operands refer to the same object or not.
'''

list1 = [] 
list2 = [] 
list3=list1 
  
if (list1 == list2): 
    print("True") 
else: 
    print("False") 
  
if (list1 is list2): 
    print("True") 
else: 
    print("False") 
  
if (list1 is list3): 
    print("True") 
else:     
    print("False")

#output
'''
    True
    False
    True
'''

#Identity operators
'''
is	=> True if the operands are identical (refer to the same object):	x is True
is not =>	True if the operands are not identical (do not refer to the same object):	x is not True
'''

x = 5
if (type(x) is int): 
    print ("true") 
else: 
    print ("false") 

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)


#Membership operators

'''
    in =>	True if value/variable is found in the sequence:	5 in x
    not in	=> True if value/variable is not found in the sequence:	5 not in x

'''

list1=[1,2,3,4,5] 
list2=[6,7,8,9] 
for item in list1: 
    if item in list2: 
        print("overlapping")       
else: 
    print("not overlapping") 

#outpou
'''
    not overlapping
'''