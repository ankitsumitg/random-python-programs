class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        if x == self.x:
            return False
        self.x = x
        return True

    def setY(self, y):
        if y == self.y:
            return False
        self.y = y
        return True
    def move(self,x,y):
        if x == 0 and y == 0:
            return False
        self.x += x
        self.y += y
        return True


class Circle(Shape):
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r

    def getRadius(self):
        return self.r

    def setRadius(self, r):
        if r == self.r or r<0:
            return False
        self.r = r
        return True

c = Circle(1, 3, 2.5)# -> c is a Circle object with position 1, 3, and radius 2.5.
print(c.getX())# -> 1
print(c.getY()) #-> 3
print(c.getRadius())# -> 2.5
print(c.setRadius(4.5))# -> True
print(c.getRadius()) #-> 4.5
print(c.setRadius(4.5)) #-> False
print(c.setRadius(0) )#-> True
print(c.getRadius())# -> 0
print(c.setRadius(-0.0001))# -> False
print(c.getRadius())# -> 0

class Rectangle(Shape):
    def __init__(self,x,y,w,h):
        Shape.__init__(self,x,y)
        self.w = w
        self.h = h
    def getHeight(self):
        return self.h
    def getWidth(self):
        return self.w
    def setWidth(self,w):
        if w== self.w or w <0:
            return False
        self.w =w
        return True
    def setHeight(self,h):
        if h == self.h or h <0:
            return False
        self.h = h
        return True

class Square(Rectangle):
    def __init__(self,x,y,s):
        Rectangle.__init__(self,x,y,s,s)
    def getSize(self):
        return self.h
    def setSize(self,s):
        if s == self.h or s < 0:
            return False
        self.h = s
        self.w = s
        return True


def test_01():
    positions = [(-10, -10), (10, -10), (10, 10), (-10, 10), (10, 10), ]
    s = Shape(0, 0)
    assert (0 == s.getX())
    assert (0 == s.getY())

    for x, y in positions:
        if x != s.getX():
            assert True == s.setX(x)
        else:
            assert False == s.setX(x)
        if y != s.getY():
            assert (True == s.setY(y))
        else:
            assert (False == s.setY(y))
        assert (x == s.getX())
        assert (y == s.getY())
    return


test_01()
