class MyInteger:
    def __init__(self,num) -> None:
        self.num = num
    def __hash__(self) -> int:
        return ((self.num + 0x9E3779B1) * 0x85EBCA77) & 0xFFFFFFFF 
    
class MyString:
    def __init__(self,s) -> None:
        self.s = s
        self.mul = 0x85EBCA77
    def __hash__(self) -> int:
        hash = 0
        for i in self.s:
            hash += hash*self.mul+MyInteger(ord(i)).__hash__()
        return hash & 0xFFFFFFFF 
    
class MyArray:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.mul = 0x85EBCA77
    def __hash__(self) -> int:
        hash = 0
        for i,val in enumerate(self.arr):
            hash += hash*self.mul
            if type(val) == int:
                hash += MyInteger(val).__hash__()
            elif type(val) == str:
                 hash += MyString(val).__hash__()
            hash = hash^MyInteger(i).__hash__()
        return hash & 0xFFFFFFFF 
    
c = MyInteger(97)
print(hash(c))
c = MyString('b')
print(hash(c))
c = MyArray([1,2,3,4,5])
print(hash(c))
c = MyArray([1,2,3,4,5])
print(hash(c))
c = MyArray([1,2,4,3,5])
print(hash(c))
c = MyArray([2,1,4,3,5])
print(hash(c))
c = MyArray(['a','b',4,5])
print(hash(c))