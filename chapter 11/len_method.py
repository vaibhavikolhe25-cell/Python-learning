# overide the len method on vector of problem 5 to display the dimention of the class vector
class vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)

#test the implementation
v1 = vector([3,6,8])
print(len(v1))         