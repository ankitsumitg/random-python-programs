class MathProblem:
  def __init__(self,lhs,rhs):
    self.rhs = rhs
    self.lhs = lhs
    self.op = ''
  def getLHS(self):
    return self.lhs
  def getRHS(self):
    return self.rhs
  def getOperator(self):
    return self.op
  def setLHS(self,lhs):
    if self.lhs == lhs:
      return False
    self.lhs = lhs
    return True
  def setRHS(self,rhs):
    if self.rhs == rhs:
      return False
    self.rhs = rhs
    return True
  def setOperator(self,op):
    if self.op == op:
      return False
    self.op = op
    return True
  def getString(self):
    return ''
  def checkAnswer(self,ans):
    if self.op == '':
      return False
    temp = str(self.rhs)+self.op+str(self.lhs)
    a = eval(temp)
    return a == ans

class AdditionProblem(MathProblem):
  def __init__(self, lhs, rhs):
    MathProblem.__init__(self, lhs, rhs)
    self.setOperator('+')
  def getString(self):
    return str(self.lhs) +' '+self.op +' '+ str(self.rhs)

class MultiplicationProblem(MathProblem):
  def __init__(self, lhs, rhs):
    MathProblem.__init__(self, lhs, rhs)
    self.setOperator('*')
  def getString(self):
    return str(self.lhs) + ' ' + self.op + ' ' + str(self.rhs)
import random
def make_problems(a,b,p):
  pp =  [AdditionProblem,MultiplicationProblem]
  ans = list()
  for _ in range(p):
    ans.append(random.choice(pp)(random.randint(a,b),random.randint(a,b)))
  return ans
def check_problems(p,ans):
  count = 0
  for i in range(len(p)):
    if p[i].checkAnswer(ans[i]):
      count += 1
  return count
make_problems(3,5,3)
print(check_problems(make_problems(3,5,3),[3,6,16]))
p = MathProblem(1, 3)
p.getString()
print(p.checkAnswer(19))
q = AdditionProblem(1, 3)
print(q.checkAnswer(4))