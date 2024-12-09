class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    @property
    def cpu(self):
        return self.cpu

    @cpu.setter
    def cpu(self, value):
        self.cpu = value

    @property
    def memory(self):
       return self.memory

    @memory.setter
    def memory(self, value):
        self.memory = value

    def introduce_myself(self):
        marital_status = "женат" if self.is_married else "не женат"
        print(f"Меня зовут {self.full_name}, мне {self.age} лет, я {marital_status}.")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks=None):
        super().__init__(full_name, age, is_married)
        self.marks = marks if marks is not None else {}

    def average_grade(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    def __init__(self, full_name, age, is_married, subject):
        super().__init__(full_name, age, is_married)
        self.subject = subject

    def introduce_myself(self):
        marital_status = "женат" if self.is_married else "не женат"
        print(f"Меня зовут {self.full_name}, мне {self.age} лет, я {marital_status}, я преподаватель по {self.subject}.")



student = Student("", 20, False, {"": 5, "": 4, "": 5})
teacher = Teacher("", 35, True, "")

student.introduce_myself()
print(f"Средняя оценка: {student.average_grade()}")

teacher.introduce_myself()
class Teacher:
    def __init__(self, name, subject, base_salary, years_of_experience):
        self.name = name
        self.subject = subject
        self.base_salary = base_salary
        self.years_of_experience = years_of_experience

    def calculate_salary(self):
        bonus = 0.05 * self.base_salary * max(0, self.years_of_experience - 3)
        return self.base_salary + bonus

    def __str__(self):
        return (f"Teacher Name: {self.name}\n"
                f"Subject: {self.subject}\n"
                f"Base Salary: {self.base_salary}\n"
                f"Years of Experience: {self.years_of_experience}\n"
                f"Calculated Salary: {self.calculate_salary()}")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student Name: {self.name}, Grade: {self.grade}"

def create_students():
    students = []
    students.append(Student("имя", ""))
    students.append(Student("имя", ""))
    students.append(Student("имя", ""))
    return students


teacher = Teacher("имя", "фамилия", 50000, 5)

print(teacher)


students = create_students()
for student in students:
    print(student)