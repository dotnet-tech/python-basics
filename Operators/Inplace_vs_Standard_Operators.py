#Inplace vs Standard Operators

import operator

'''
    Normal operator’s “add()” method, implements “a+b” and stores the result in the mentioned variable.
    Inplace operator’s “iadd()” method, implements “a+=b” : (changes the value of passed argument only for Mutable Targets
    not for Immutable Targets).
'''

#Immutable Targets.
x = 5
y = 6
a = 5
b = 6
# using add() to add the arguments passed  
z = operator.add(a,b) 
  
# using iadd() to add the arguments passed  
p = operator.iadd(x,y) 
  
# printing the modified value 
print ("Value after adding using normal operator : ",end="") 
print (z) 
  
# printing the modified value 
print ("Value after adding using Inplace operator : ",end="") 
print (p) 
  
# printing value of first argument 
# value is unchanged 
print ("Value of first argument using normal operator : ",end="") 
print (a) 
  
# printing value of first argument 
# value is unchanged 
print ("Value of first argument using Inplace operator : ",end="") 
print (x)

#output are:

'''
    Value after adding using normal operator : 11
    Value after adding using Inplace operator : 11
    Value of first argument using normal operator : 5
    Value of first argument using Inplace operator : 5
'''

#Mutable Targets
a = [1, 2, 4, 5] 
  
# using add() to add the arguments passed  
z = operator.add(a,[1, 2, 3]) 
  
# printing the modified value 
print ("Value after adding using normal operator : ",end="") 
print (z) 
  
# printing value of first argument 
# value is unchanged 
print ("Value of first argument using normal operator : ",end="") 
print (a) 
  
# using iadd() to add the arguments passed  
# performs a+=[1, 2, 3] 
p = operator.iadd(a,[1, 2, 3]) 
  
# printing the modified value 
print ("Value after adding using Inplace operator : ",end="") 
print (p) 
  
# printing value of first argument 
# value is changed 
print ("Value of first argument using Inplace operator : ",end="") 
print (a)

#output

'''
    Value after adding using normal operator : [1, 2, 4, 5, 1, 2, 3]
    Value of first argument using normal operator : [1, 2, 4, 5]
    Value after adding using Inplace operator : [1, 2, 4, 5, 1, 2, 3]
    Value of first argument using Inplace operator : [1, 2, 4, 5, 1, 2, 3]
'''