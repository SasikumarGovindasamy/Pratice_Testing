from abc import ABC, abstractmethod   # For abstraction

# -----------------------------
# Encapsulation: Using private attributes
# -----------------------------
class Person:
    def __init__(self, name, age):
        self._name = name        # protected attribute
        self.__age = age         # private attribute

    def get_name(self):          # getter
        return self._name

    def get_age(self):           # getter for private
        return self.__age

    def set_age(self, age):      # setter
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")


# -----------------------------
# Abstraction: Abstract Base Class
# -----------------------------
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


# -----------------------------
# Inheritance: Teacher inherits from Person and Employee
# -----------------------------
class Teacher(Person, Employee):
    def __init__(self, name, age, subject, base_salary):
        super().__init__(name, age)   # super() usage
        self.subject = subject
        self.base_salary = base_salary

    # Polymorphism: overriding abstract method
    def calculate_salary(self):
        return self.base_salary + 5000

    def get_subject(self):
        return self.subject


# -----------------------------
# Inheritance: Student inherits from Person
# -----------------------------
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_grade(self):
        return self.grade


# -----------------------------
# Polymorphism: Same method name, different behavior
# -----------------------------
def show_details(person_obj):
    # This function works differently depending on object type
    if isinstance(person_obj, Teacher):
        print(f"Teacher: {person_obj.get_name()}, Subject: {person_obj.get_subject()}, Salary: {person_obj.calculate_salary()}")
    elif isinstance(person_obj, Student):
        print(f"Student: {person_obj.get_name()}, Grade: {person_obj.get_grade()}")
    else:
        print(f"Person: {person_obj.get_name()}, Age: {person_obj.get_age()}")


# -----------------------------
# Static Method: Utility function
# -----------------------------
class Utils:
    @staticmethod
    def welcome_message():
        print("Welcome to the School Management System!")


# -----------------------------
# Class Method: Works with class variables
# -----------------------------
class School:
    school_name = "ABC International School"

    @classmethod
    def get_school_name(cls):
        return cls.school_name


# -----------------------------
# MAIN PROGRAM
# -----------------------------
if __name__ == "__main__":
    Utils.welcome_message()   # Static method call

    print("School Name:", School.get_school_name())  # Class method call

    # Create objects
    teacher = Teacher("Alice", 35, "Maths", 40000)
    student = Student("Bob", 12, "6th Grade")

    # Encapsulation demo
    print("Teacher Age (via getter):", teacher.get_age())
    teacher.set_age(36)
    print("Updated Teacher Age:", teacher.get_age())

    # Polymorphism demo
    show_details(teacher)
    show_details(student)
