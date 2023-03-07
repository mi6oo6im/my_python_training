from project.child import Child
from project.person import Person

p = Person('Peter', 23)
c = Child('Derek', 12)

print(p.name, p.age)
print(c.name, c.age)
print(Child.mro())