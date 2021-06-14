# Класс студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

# Класс преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Создание экземпляра класса студент:
student_no_1 = Student('Ruoy', 'Eman', '25')
student_no_1.courses_in_progress += ['Python']
student_no_1.courses_in_progress += ['English for IT']
student_no_1.finished_courses += ['Git']
student_no_1.grades['Git'] = [10, 8, 10]
student_no_1.grades['Python'] = [10, 8, 9, 7, 10, 9]
student_no_1.grades['English for IT'] = [9, 9]

# Создание экземпляра класса преподаватель:
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['English for IT']
# Проставляем оценки (добавление к существующим):
cool_mentor.rate_hw(student_no_1, 'Python', 10)
cool_mentor.rate_hw(student_no_1, 'Python', 8)
cool_mentor.rate_hw(student_no_1, 'English for IT', 10)


# Проверка:
print(student_no_1.finished_courses)
print(student_no_1.courses_in_progress)
print(student_no_1.grades)
print(cool_mentor.courses_attached)
print(cool_mentor.name)
print(cool_mentor.surname)