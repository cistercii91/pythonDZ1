print ('привет мир')
# print('спасибо Димасик')
# ctrl + '/'
# alt + 4 - запустить

class Student:

    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    @staticmethod
    def avg_grade_students(student_list, course):
        s = 0
        counter = 0
        for student in student_list:
            if course in student.courses_in_progress:
                s += student.count_avg_grade()
                counter += 1
        return s/counter

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and\
                course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.count_avg_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}\n"

    def count_avg_grade(self):
        if len(self.grades.values()) > 0:
            return sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])
        else:
            return 0

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.count_avg_grade() < other.count_avg_grade():
                return True
            else:
                return False
        else:
            pass


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    lecturer_list = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_avg_grade()}\n"

    def __init__(self, name, surname):
        Lecturer.lecturer_list.append(self)
        self.grades = {}
        super().__init__(name, surname)

    def count_avg_grade(self):
        if len(self.grades.values()) > 0:
            return sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])
        else:
            return 0

    @staticmethod
    def avg_grade_lectors(lecturer_list, course):
        s = 0
        counter = 0
        for lecturer in lecturer_list:
            if course in lecturer.courses_attached:
                s += lecturer.count_avg_grade()
                counter += 1
        return s/counter

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.count_avg_grade() < other.count_avg_grade():
                return True
            else:
                return False
        else:
            pass


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and\
                course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Roy', 'Eman', 'male')
worst_student = Student('Edward', 'Bill', 'male')
best_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Python']

best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Python']
best_student.rate_lec(best_lecturer, 'Python', 10)

worst_lecturer = Lecturer('Once', 'Told')
worst_lecturer.courses_attached += ['Python']
best_student.rate_lec(worst_lecturer, 'Python', 2)

cool_reviewer = Reviewer('World', 'Gonna')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)

bad_reviewer = Reviewer('Aleksey', 'Goncharov')
bad_reviewer.courses_attached += ['Python']
bad_reviewer.rate_hw(worst_student, 'Python', 1)

mentor_first = Mentor('Alexander', 'Some')
mentor_first.courses_attached += ['Python']
mentor_second = Mentor('Example', 'Ment')
mentor_second.courses_attached += ['Python']

print(Student.avg_grade_students(Student.student_list, 'Python'))
# отразит среднюю оценку студентов

print(Lecturer.avg_grade_lectors(Lecturer.lecturer_list, 'Python'))
# отразит среднюю оценку Лекторов

print(best_student > worst_student)
# сравнит оценку студентов

print(best_lecturer > worst_lecturer)
# сравнит оценку лекторов

print(worst_lecturer, best_student,)
# выводит общую информацию через метод __str__
