class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,other):
        return self.n + other.n


n = Number(20)
m = Number(10) 

print(n+m)

# The key point is:
# self → first object (n)
# other → second object (m)
# self.n → value of first object
# other.n → value of second object
# - Subtraction — __sub__()
class number:

    def __init__(self,n):
        self.n = n

    def __sub__(self, other):
        return self.n - other.n

n = number(10)
m = number(3)        

print(n - m)
# * Multiplication — __mul__()
class number:

    def __init__(self,n):
        self.n = n

    def __mul__(self, other):
        return self.n * other.n

n = number(30)
m = number(2)

print(n*m)

# / Division — __truediv__()

class number:

    def __init__(self,n):
        self.n = n

    def __truediv__(self, other):
        return self.n / other.n

n = number(25)
m = number (5)   

print(n/m)

# // Floor Division — __floordiv__()
class number:

    def __init__(self,n):

        self.n = n

    def __floordiv__(self, other):
        return self.n // other.n

n = number(25) 
m = number (4)

print(n//m)

# % Modulus — __mod__()
class number:

    def __init__(self,n):
        self. n = n


    def __mod__(self, other):
        return self.n % other.n

n = number(11)
m = number(3)        

print(n % m)
# ** Power — __pow__()
class number:

    def __init__(self,n):
        self.n = n

    def __pow__(self, other):
        return self.n ** other.n

n = number(2)
m = number(3)

print(2**3)

# < Less Than — __lt__()
class number:

    def __init__(self,n):
        self.n = n

    def __lt__(self, other):
        return self.n < other.n

n =number(3)
m = number(10)

print(n<m)


class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return self.n / other.n

    def __gt__(self, other):
        return self.n > other.n

    def __lt__(self, other):
        return self.n < other.n

    def __eq__(self, other):
        return self.n == other.n

    def __str__(self):
        return str(self.n)


a = Number(10)
b = Number(5)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a > b)
print(a < b)
print(a == b)
print(a)

# > Greater Than — __gt__()
class Number:
    def __init__(self, n):
        self.n = n

    def __gt__(self, other):
        return self.n > other.n


a = Number(20)
b = Number(10)

print(a > b)
# == Equal To — __eq__()
class Number:
    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        return self.n == other.n


a = Number(10)
b = Number(10)

print(a == b)
# != Not Equal — __ne__()
class Number:
    def __init__(self, n):
        self.n = n

    def __ne__(self, other):
        return self.n != other.n


a = Number(10)
b = Number(20)

print(a != b)

# <= Less Than or Equal — __le__()
class Number:
    def __init__(self, n):
        self.n = n

    def __le__(self, other):
        return self.n <= other.n


a = Number(10)
b = Number(20)

print(a <= b)

# >= Greater Than or Equal — __ge__()
class Number:
    def __init__(self, n):
        self.n = n

    def __ge__(self, other):
        return self.n >= other.n


a = Number(20)
b = Number(10)

print(a >= b)
# Unary means the operator works on one object.
# Unary - — __neg__()
class Number:
    def __init__(self, n):
        self.n = n

    def __neg__(self):
        return -self.n


a = Number(10)

print(-a)

# Unary + — __pos__()
class Number:
    def __init__(self, n):
        self.n = n


    def __pos__(self):
        return +self.n

a = Number(10)

print(+a)

# ~ Bitwise NOT — __invert__()
class Number:
    def __init__(self, n):
        self.n = n


    def __invert__(self):
        return ~self.n

a = Number(5)

print(~a)
        
# Real Example — Complex Numbers
# This is a good practical example.

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary


    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )


    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


c1 = Complex(2, 3)
c2 = Complex(4, 5)

c3 = c1 + c2
print(c3)

# Output: 6 + 8i