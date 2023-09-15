class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class D:
  def method(self):
    print("D.method() called")

class C(A, D):
  pass

class E(D, C):
  pass

e = E()
e.method()