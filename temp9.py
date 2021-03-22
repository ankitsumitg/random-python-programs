class KetchupBottle:
    def __init__(self,k):
        self.k = k
    def squeeze(self,s):
        if self.k ==0:
            return 0
        t = self.k
        if s > self.k:
            self.k = 0
            return t
        self.k -= s
        return s
b = KetchupBottle( 16 )
print( b.squeeze( 2 ) ) # displays 2
print( b.squeeze( 5 ) ) # displays 5
print( b.squeeze( 4 ) ) # displays 4
print( b.squeeze( 4 ) ) # displays 4
print( b.squeeze( 3 ) ) # displays 1
print( b.squeeze( 1 ) ) # displays 0