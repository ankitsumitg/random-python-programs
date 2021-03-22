import math

KIND_PLAYER = 1
KIND_FOOD = 2
KIND_AI = 3


class Blob:

    def __init__(self, mass, x, y, world_width, world_height, kind):
        self.mMass = float(mass)  # mass
        self.mX = float(x)  # x position
        self.mY = float(y)  # y position
        self.mDx = 0.  # portion of speed that comes from x
        self.mDy = 0.  # portion of speed that comes from y
        self.mKind = kind  # kind of blob
        self.mAlive = True  # blob's life status

        # size of the world, used for bounding motion
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        # used to scale the speed to tune game play
        self.mSpeedMultiplier = 10.0
        # used to scale the display size of blobs
        self.mRadiusMultiplier = 5.0
        # used to make sure 1 frame's motion doesn't overshoot the destination
        self.mDestinationSpeed = 0.0
        return

    def __ne__(self, other):
        return self.mX != other.mX and self.mY != other.mY

    def __gt__(self, other):
        return self.mMass >= 1.25 * other.mMass

    def __iadd__(self, other):
        self.mMass += other.mMass
        other.mMass = 0
        other.mAlive = False
        return self

    def __xor__(self, other):
        return ((self.mX - other.mX) ** 2 + (self.mY - other.mY) ** 2) ** 0.5 <= (
            self.getRadius() if self.getRadius() > other.getRadius() else other.getRadius())

    def __ilshift__(self, other):
        diffX =  other[0] - self.mX
        diffY =  other[1] - self.mY
        self.mDestinationSpeed = (diffX**2+diffY**2)**.5
        if self.mDestinationSpeed > 0:
            self.mDx = diffX/self.mDestinationSpeed
            self.mDy = diffY/self.mDestinationSpeed
        return self
    def __irshift__(self, other):
        self.mX += other*self.mDx
        self.mY += other*self.mDy
        return self
    def getMass(self):
        return self.mMass

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getAlive(self):
        return self.mAlive

    def getKind(self):
        return self.mKind

    def getSpeed(self):
        return self.mDestinationSpeed if self.mDestinationSpeed < self.mSpeedMultiplier / math.log(
            self.mMass) else self.mSpeedMultiplier / math.log(self.mMass)

    def getRadius(self):
        return self.mRadiusMultiplier * math.sqrt(self.mMass / math.pi)
'''
b1 = Blob(1.5, 23, 37, 800, 600, KIND_PLAYER)
b1 <<= [ 314, 271 ]
print(b1)

b1 = Blob(1.1, 2.2, 3.3, 500, 400, KIND_AI)
b2 = Blob(2.1, 3.2, 4.3, 600, 500, KIND_PLAYER)
b3 = Blob(3.1, 2.2, 3.3, 700, 600, KIND_FOOD)

b1 += b2
assert 3.2==b1.getMass()
assert True==b1.getAlive()
assert 0.0==b2.getMass()
assert False==b2.getAlive()'''
