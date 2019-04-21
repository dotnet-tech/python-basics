#Ternary Operator
'''
Syntax => [on_true] if [expression] else [on_false]
'''
a,b =20,10
result =True if a>b else False
print('result: A is grater then B : {}'.format(result))

'''
using tuples, Dictionary and lambda
'''
result1 =(b,a) [a>b]                        #tuple : flase and true
print(f'result 1: A is grater then B : {result1}')  

result2 ={True:a,False:b}[a>b]              #Dictionary : true and flase
print(f'result 2: A is grater then B : {result2}')

result3 =(lambda:b,lambda:a)[a>b]()         #lambda : flase and true
print(f'result 3: A is grater then B : {result3}') 


'''
using Nested if-else
'''
result4 = 'Both a and b are equal' if a==b else 'a is greater than b'  if a>b else 'b is greater than a'
print("result 4: " + result4)

#Output are:
'''
    result: A is grater then B : True
    result 1: A is grater then B : 20
    result 2: A is grater then B : 20
    result 3: A is grater then B : 20
    result 4: a is greater than b
'''