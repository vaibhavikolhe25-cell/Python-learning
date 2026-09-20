# write a class vector representing a vector of n dimentions. overload the + and * operator which calculates the sum and dot (.) product of them
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z 

    def __add__(self, other):
        result = vector(self.x + other.x , self.y + other.y , self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"vector ({self.x},{self.y},{self.z})"

# test the implementation 
v1 = vector(2,6,9)
v2 = vector(4,1,8)
v3 = vector(6,7,3)    # same dimension vector

print(v1 + v2)           # output = vector(6,7,17)
print(v1 * v2)           #output = 86

print(v1 + v3)           # output = vector (8,13,12)
print(v1 * v3)           #output = 81



