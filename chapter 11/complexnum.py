# write a class complex  to represent a complex number along with overloaded operators + and * which adds and multiply them
class complex:
    def __init__(self,i,r):
        self.r = r
        self.i = i


    def __add__(self, c2):
        return complex(self.r + c2.r , self.i + c2.i)


    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return complex(real_part,imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i" 

c1 = complex(2,4)
c2 = complex(6,7)
print(c1 + c2)
print(c1*c2)    