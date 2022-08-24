class Student:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age

class Teacher(Student):
    pass
    def __init__(self,firstname,lastname,age):
        super().__init__(firstname,lastname,age)

object1=Teacher("Destiny","Bakret",23)
object2=Teacher("Joel","Shehu",22)

print(Teacher.lastname(object1))
print(Teacher.firstname(object2))
