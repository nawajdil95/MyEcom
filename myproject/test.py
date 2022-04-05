class a():
    def _str_(self):
        return '1'
class b(a):
    def _init_(self):
        super()._init_()
class c(b):
    def _init_(self):
        super()._init_()
obj1 = b()
obj2 = a()
obj3 = c()
print(obj1,obj2,obj3)