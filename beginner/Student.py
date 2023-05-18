class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def is_on_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False


student1 = Student("Mike", "psychology", 3.5, False)
student2 = Student("Jim", "Art", 3.7, False)
student3 = Student("Dan", "Business", 2.8, True)

print(student3.is_on_honor_roll())
