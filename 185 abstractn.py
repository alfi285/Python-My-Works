class Student:
    def __init__(self, name, roll_number, grades=None):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = grades if grades else {}

    def add_grade(self, subject, grade):
        self.__grades[subject] = grade
        print(f"Added grade for {subject}: {grade}")

    def remove_grade(self, subject):
        if subject in self.__grades:
            del self.__grades[subject]
            print(f"Removed grade for {subject}")
        else:
            print(f"No grade found for {subject}")

    def display_grades(self):
        print(f"Grades for {self.__name}:")
        for subject, grade in self.__grades.items():
            print(f"{subject}: {grade}")

    def calculate_gpa(self):
        total_grade = sum(self.__grades.values())
        average_grade = total_grade / len(self.__grades)
        print(f"GPA: {average_grade:.2f}")

# Create a Student object
student = Student("John Doe", "123456")

# Use the student object without knowing internal details
student.add_grade("Math", 85)
student.add_grade("Science", 90)
student.display_grades()
student.calculate_gpa()
student.remove_grade("Math")
student.display_grades()

