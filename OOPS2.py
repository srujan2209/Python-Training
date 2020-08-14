# Objects Oriented Programming with multiple class


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:

    def __init__(self,name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grades(self):
        value = 0

        for student in self.students:
            value += student.get_grade()

            return value / len(self.students)

s1 = Student("Jim", 25, 95)
s2 = Student("Sim", 26, 75)
s3 = Student("chino", 28, 65)

course = Course("DevOps", 2)
course.add_students(s1)
course.add_students(s3)
print(course.get_avg_grades())

