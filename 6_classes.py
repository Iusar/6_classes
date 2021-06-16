# Класс студентов
class student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, specific_lecturer, course, grade):
        if isinstance(specific_lecturer,
                      lecturer) and course in specific_lecturer.courses_attached and course in self.courses_in_progress and 0 < grade <= 10:
            if course in specific_lecturer.lecturers_grades:
                specific_lecturer.lecturers_grades[course] += [grade]
            else:
                specific_lecturer.lecturers_grades[course] = [grade]
        else:
            return 'Ошибка'


# Класс преподавателей
class mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Класс лекторов
class lecturer(mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturers_grades = {}


# Класс экспертов
class reviewer(mentor):

    def rate_hw(self, specific_student, course, grade):
        if isinstance(specific_student,
                      student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in specific_student.grades:
                specific_student.grades[course] += [grade]
            else:
                specific_student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создание экземпляра класса студент1:
student_no_1 = student('Roy', 'Eman', '25')
student_no_1.courses_in_progress += ['Python']
student_no_1.courses_in_progress += ['English for IT']
student_no_1.finished_courses += ['Git']
student_no_1.grades['Git'] = [10, 8, 10]
student_no_1.grades['Python'] = [10, 8, 9, 7, 10, 9]
student_no_1.grades['English for IT'] = [9, 9]
# Создание экземпляра класса студент2:
student_no_2 = student('Roy', 'Eman', '25')
student_no_2.courses_in_progress += ['Python']
student_no_2.finished_courses += ['Git']
student_no_2.grades['Git'] = [10, 8, 10]
student_no_2.grades['Python'] = [7, 7]

# Создание экземпляра класса лектор:
cool_Lecturer = lecturer('Another', 'Buddy')
cool_Lecturer.courses_attached += ['Python']
cool_Lecturer.courses_attached += ['English for IT']
cool_Lecturer.courses_attached += ['Git']

# Создание экземпляра класса Эксперт:
cool_reviewer = reviewer('Another', 'Buddy')
cool_Lecturer.courses_attached += ['Python']

# Проверяем
# Сценарий №1 Эксперт проставляет оценки студену:
cool_reviewer.rate_hw(student_no_1, 'Python', 9)
cool_reviewer.rate_hw(student_no_1, 'Python', 8)
cool_reviewer.rate_hw(student_no_1, 'English for IT', 10)
print(f'Сценарий №1 {student_no_1.grades}')

# Сценарий №2 лектор проставляет оценки студену:
# cool_Lecturer.rate_hw(student_no_1, 'Python', 9)
# cool_Lecturer.rate_hw(student_no_1, 'Python', 8)
# cool_Lecturer.rate_hw(student_no_1, 'English for IT', 10)
# print(f'Сценарий №2 {student_no_1.grades}')

# Сценарий №3 Студент1 проставляет оценки лектору):
student_no_1.rate_lecturer(cool_Lecturer, 'Python', 9)
student_no_1.rate_lecturer(cool_Lecturer, 'Python', 8)
student_no_1.rate_lecturer(cool_Lecturer, 'English for IT', 5)
print(f'Сценарий №3 {cool_Lecturer.lecturers_grades}')

# Сценарий №4 Студент2 проставляет оценки лектору (добавление к существующим):
student_no_2.rate_lecturer(cool_Lecturer, 'Python', 9)
student_no_2.rate_lecturer(cool_Lecturer, 'Python', 8)
print(f'Сценарий №4 {cool_Lecturer.lecturers_grades}')

# Сценарий №5 Студент1 проставляет оценки Эксперту :
# student_no_1.cool_reviewer(cool_reviewer, 'Python', 9)
# student_no_1.cool_reviewer(cool_reviewer, 'Python', 8)
# student_no_1.cool_reviewer(cool_reviewer, 'English for IT', 5)
# print(f'Сценарий №5 {cool_reviewer.lecturers_grades}')

# Сценарий №6 Студент2 проставляет оценки Эксперту:
# student_no_2.cool_reviewer(cool_reviewer, 'Python', 9)
# student_no_2.cool_reviewer(cool_reviewer, 'Python', 8)
# print(f'Сценарий №5 {cool_reviewer.lecturers_grades}')
