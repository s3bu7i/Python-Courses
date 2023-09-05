#classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is "+ self.name)
p1 = Person("John", 33)
p1.age = 22
del p1.age
print(p1.myfunc())

"""-----------------------------------------------"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
print(p1)    
        
class myClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} \n{self.age}"

a = myClass("Lina", 222)
print(a)
print(a.name)
print(a.age)
