# write __str__ method  to print thr vector  as follows
# 7i + 8j + 10k
# assume vector of dimentions  3 for this problem
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
        return f"({self.x}i + {self.y}j +{self.z}k )"

# test the implementation 
v1 = vector(2,6,9)
v2 = vector(4,1,8)
v3 = vector(6,7,3)    # same dimension vector

print(v1 + v2)           # output = vector(6,7,17)
print(v1 * v2)           #output = 86

print(v1 + v3)           # output = vector (8,13,12)
print(v1 * v3)           #output = 81