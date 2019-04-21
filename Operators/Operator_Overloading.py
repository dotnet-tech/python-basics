#Operator Overloading

print(1 + 2) 
print("Python"+"is")  
print(3 * 4) 
print("Python"*4) 

#output
'''
    3
    Pythonis
    12
    PythonPythonPythonPython
'''

class AddNumbers:
    def __init__(self,a):
        self.a =a

    def __add__(self,b):        #magic method (+ overloading)
        return self.a + b.a    

    def addTwoNumbers(self,b):  #normal method
        return self.a + b


a = AddNumbers(10)
b =AddNumbers(20)
print("Result A + B  = {} ".format(a.addTwoNumbers(40)))
print('Overloading result A + B  = {}'.format(a+b))

#output
'''
    Result A + B  = 50
    Overloading result A + B  = 30
'''

'''
Binary Operators:
OPERATOR	MAGIC METHOD
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)

Comparison Operators :
OPERATOR	MAGIC METHOD
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)

Assignment Operators :
OPERATOR	MAGIC METHOD
-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
/=	__idiv__(self, other)
//=	__ifloordiv__(self, other)
%=	__imod__(self, other)
**=	__ipow__(self, other)

Unary Operators :
OPERATOR	MAGIC METHOD
–	__neg__(self, other)
+	__pos__(self, other)
~	__invert__(self, other)
'''
