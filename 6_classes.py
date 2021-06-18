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

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade(self.grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return output

    def rate_lecturer(self, specific_lecturer, course, grade):
        if isinstance(specific_lecturer, lecturer) \
                and course in specific_lecturer.courses_attached \
                and course in self.courses_in_progress \
                and 0 < grade <= 10:

            specific_lecturer.grades.append(grade)

        else:
            return 'Ошибка'


# Класс преподавателей
class mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


# Класс лекторов
class lecturer(mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade(self.grades)}'
        return output


# Класс экспертов
class reviewer(mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

    # Метод класса оценки студентов
    def rate_hw(self, specific_student, course, grade):
        if isinstance(specific_student, student) \
                and course in self.courses_attached \
                and course in specific_student.courses_in_progress:

            if course in specific_student.grades:
                specific_student.grades[course] += [grade]
            else:
                specific_student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Функция расчета среднего значения оценок:
def average_grade(all_grades):
    if type(all_grades) is dict:
        amount_grades = []
        for grades in all_grades.values():
            for grade in grades:
                amount_grades.append(grade)
        return average_grade(amount_grades)
    elif type(all_grades) is list and all_grades[0] != None:
        average = round(sum(all_grades) / len(all_grades), 2)
        return average
    else:
        return "Ошибка! Оценки храняться не в словаре и не в списке, или список состоит из вложенных списков"


# Функция расчета среднего значения оценок:
def average_course_grade(all_students, current_course):
    all_course_grades = []
    for current_student in all_students:
        if current_course in current_student.grades.keys():
            for every_grade in current_student.grades.get(current_course):
                all_course_grades.append(every_grade)
        else: print(f'Курс {current_course} отсутствует у студента {current_student.name} {current_student.surname}')
    return average_grade(all_course_grades)


# Функция расчета среднего значения оценок:
def average_lecturers_grade(all_lecturers):
    all_lecturers_grades = []
    for current_lecturer in all_lecturers:
        for every_grade in current_lecturer.grades:
            all_lecturers_grades.append(every_grade)
    return average_grade(all_lecturers_grades)


# Функция сравнения оценок:
def average_grade_diff(person_1, person_2):
    if isinstance(person_1, student) and isinstance(person_2, student):
        if average_grade(person_1.grades) > average_grade(person_2.grades):
            print(
                f'Средняя оценка студента {person_1.name} {person_1.surname} больше чем у студента {person_2.name} {person_2.surname}')
        elif average_grade(person_1.grades) < average_grade(person_2.grades):
            print(
                f'Средняя оценка студента {person_1.name} {person_1.surname} меньше чем у студента {person_2.name} {person_2.surname}')
        else:
            print(
                f'Средние оценки студентов {person_1.name} {person_1.surname} и {person_2.name} {person_2.surname} равны')
    elif isinstance(person_1, lecturer) and isinstance(person_2, lecturer):
        if average_grade(person_1.grades) > average_grade(person_2.grades):
            print(
                f'Средняя оценка лектора {person_1.name} {person_1.surname} больше чем у лектора {person_2.name} {person_2.surname}')
        elif average_grade(person_1.grades) < average_grade(person_2.grades):
            print(
                f'Средняя оценка лектора {person_1.name} {person_1.surname} меньше чем у лектора {person_2.nam} {person_2.surname}')
        else:
            print(
                f'Средние оценки лекторов {person_1.name} {person_1.surname} и {person_2.name} {person_2.surname} равны')
    else:
        print('Ошибка! Выберите или двух студентов или двух преподавателей')
    pass


# Создание экземпляра класса студент1:
student_no_1 = student('Roy', 'Eman', '25')
student_no_1.courses_in_progress += ['Python']
student_no_1.courses_in_progress += ['English for IT']
student_no_1.finished_courses += ['Git']
student_no_1.add_courses('Math')
student_no_1.grades['Git'] = [7, 2, 6]
student_no_1.grades['Python'] = [10, 10, 8, 10, 10, 10]
student_no_1.grades['English for IT'] = [10, 10]
# Создание экземпляра класса студент2:
student_no_2 = student('Mike', 'Red', '45')
student_no_2.courses_in_progress += ['Python']
student_no_2.finished_courses += ['Git']
student_no_2.grades['Git'] = [9, 5, 2]
student_no_2.grades['Python'] = [8, 10]
# Допустим мы их храним в списке (для функции average_course_grade):
student_list = [student_no_1, student_no_2]

# Создание экземпляра класса лектор1:
lecturer_1 = lecturer('Bill', 'Boops')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['English for IT']
lecturer_1.courses_attached += ['Git']

# Создание экземпляра класса лектор2:
lecturer_2 = lecturer('Ray', 'Bitts')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['English for IT']
lecturer_2.courses_attached += ['Git']

# Допустим мы их храним в списке (для функции average_lecturers_grade):
lecturer_list = [lecturer_1, lecturer_2]

# Создание экземпляра класса Эксперт:
cool_reviewer = reviewer('Anton', 'Green')
cool_reviewer.courses_attached += ['Python']

# Создание экземпляра класса Эксперт2:
cool_reviewer_2 = reviewer('Eddy', 'Grey')
cool_reviewer_2.courses_attached += ['Git']

# Проверяем

print('*****Результат проверки работы функций добавления оценок*****')
# Сценарий №1 Эксперт проставляет оценки студену:
cool_reviewer.rate_hw(student_no_1, 'Python', 1)
cool_reviewer.rate_hw(student_no_1, 'Python', 1)
cool_reviewer.rate_hw(student_no_1, 'English for IT', 1)
print(f'Сценарий №1 {student_no_1.grades}')

# Сценарий №2 лектор проставляет оценки студену:
# cool_Lecturer.rate_hw(student_no_1, 'Python', 2)
# cool_Lecturer.rate_hw(student_no_1, 'Python', 2)
# cool_Lecturer.rate_hw(student_no_1, 'English for IT', 2)
# print(f'Сценарий №2 {student_no_1.grades}')

# Сценарий №3 Студент1 проставляет оценки лектору):
student_no_1.rate_lecturer(lecturer_1, 'Python', 3)
student_no_1.rate_lecturer(lecturer_1, 'Python', 3)
student_no_1.rate_lecturer(lecturer_1, 'English for IT', 3)
print(f'Сценарий №3 {lecturer_1.grades}')

# Сценарий №4 Студент2 проставляет оценки лектору (добавление к существующим):
student_no_2.rate_lecturer(lecturer_1, 'Python', 4)
student_no_2.rate_lecturer(lecturer_2, 'Python', 4)
print(f'Сценарий №4 {lecturer_1.grades}')

# Сценарий №5 Студент1 проставляет оценки Эксперту :
# student_no_1.cool_reviewer(cool_reviewer, 'Python', 9)
# student_no_1.cool_reviewer(cool_reviewer, 'Python', 8)
# student_no_1.cool_reviewer(cool_reviewer, 'English for IT', 5)
# print(f'Сценарий №5 {cool_reviewer.lecturers_grades}')

# Сценарий №6 Студент2 проставляет оценки Эксперту:
# student_no_2.cool_reviewer(cool_reviewer, 'Python', 9)
# student_no_2.cool_reviewer(cool_reviewer, 'Python', 8)
# print(f'Сценарий №5 {cool_reviewer.lecturers_grades}')

print('*****Результат проверки работы функции печати для классов*****')
print(lecturer_2)
print()
print(cool_reviewer)
print()
print(student_no_1)
print()
print(student_no_2)
print()

print('*****Результат проверки работы функции сравнения*****')
average_grade_diff(student_no_1, student_no_2)
print()
average_grade_diff(lecturer_2, lecturer_1)
print()
average_grade_diff(student_no_1, lecturer_1)

print('*****Результат проверки работы функции рассчета среднего балла студентов по определенному курсу*****')
print(average_course_grade(student_list, 'Git'))

print('*****Результат проверки работы функции рассчета среднего балла лекторов по всем курсам (почему-то..)*****')
print(average_lecturers_grade(lecturer_list))
