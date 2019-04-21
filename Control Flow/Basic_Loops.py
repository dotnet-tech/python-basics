#Loops

'''
    1. While Loop
    2. For Loop
    3. Else with While and For Loop
    4. Loops and Control Statements (continue, break and pass) : this normal for c#
'''
#While Loop
i =0
while (i<5):
    i+=1
    print(i)

#While with Else Statement

count = 0
while (count < 3):     
    count = count + 1
    print(count) 
else: 
    print("In Else Block") 

#output
'''
1
2
3
In Else Block
'''    
#For Loop

l = ["One", "Two", "Three"] 
for i in l: 
    print(i) 
       
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("One", "Two", "Three") 
for i in t: 
    print(i) 
       
# Iterating over a String 
print("\nString Iteration")     
s = "One"
for i in s : 
    print(i) 
 
#output
'''
    One
    Two
    Three

    Tuple Iteration
    One
    Two
    Three   

    String Iteration
    O
    n
    e
'''

#Different looping techniques
#Using enumerate()
for key,value in enumerate(['One','Two','Three']):
    print(f'{key} is {value}')

#output
'''
    0 is One
    1 is Two
    2 is Three
'''

#Using zip()
questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 

for question,answer in zip(questions,answers):
    print('What is your {0}?  I am {1}.'.format(question, answer))

#output
'''
    What is your name?  I am apple.
    What is your colour?  I am red.
    What is your shape?  I am a circle.
'''
#Using dictionary
d = {"One":"1", "Two":"2", "Three":"3"}

for v in d:
    print('Value is: {}'.format(v))

#output
'''
    Value is: One
    Value is: Two
    Value is: Three
'''

for k,v in d.items():
    print('Value is: {} and Key is {}'.format(k,v))
#output
'''
    Value is: One and Key is 1
    Value is: Two and Key is 2
    Value is: Three and Key is 3
'''
for v in d.values():
    print('Value is: {}'.format(v))