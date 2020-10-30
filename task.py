
class Diary:
    # todo read students and classes from file
    def __init__(self):
        self.students = []
        self.subjects_names = []

    def add_new_student(self, student):
        self.students.append(student)

    def add_student_to_subject(self, student, subject):
        pass

    def print_all_students(self):
        print(self.students)

    def print_students_average_in_subject(self, subject):
        pass

    def print_students_attendance(self):
        pass

    def print_student_subject_average(self, student):
        pass


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.attendance = 0
        self.subjects = []

    def get_average(self):
        pass

    def get_attendance(self):
        pass

    def __repr__(self):
        return self.name + " " + self.surname


class Subject:
    def __init__(self):
        self.name = 0
        self.student_scores = []

    def add_score(self, score):
        self.student_scores.append(score)

    def get_scores_average(self):
        return sum(self.student_scores) / len(self.student_scores)


if __name__ == '__main__':
    diary = Diary()
    diary.add_new_student(Student("Jan", "Kowalski"))
    diary.print_all_students()
