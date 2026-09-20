class employee:
    def __init__(self):
        print(f"construtor of employee")
    a = 1


class programmer(employee):
    def __init__(self):
        print(f"constructor of programmer")
    b = 2 


class manager(programmer):
    def __init__(self):
        super().__init__()
        print(f"constructor of manager ")
    c = 3

o = employee()
print(o.a)  # print tha a attribute

o = programmer()
print(o.a,o.b)


o = manager()
print(o.c,o.b,o.a)
