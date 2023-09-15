class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class D:
  def method(self):
    print("D.method() called")

class C(A, B):
  pass

class E(C, D):
  pass

e = E()
e.method()