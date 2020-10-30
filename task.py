
class Diary:
    def __init__(self):
        self.students = []
        self.subjects_names = []

    def add_new_subjects_from_file(self, file_path):
        file = open(file_path, "r")
        self.subjects_names = file.read().splitlines()

    def add_new_students_from_file(self, file_path):
        file = open(file_path, "r")
        full_names = [full_name.split(", ") for full_name in file.read().splitlines()]
        for full_name in full_names:
            self.add_new_student(full_name[0], full_name[1])

    def add_new_student(self, name, surname):
        student = Student(name, surname)
        self.students.append(student)

    def add_student_to_subject(self, name, surname, subject):
        pass

    def add_subject(self, subject):
        self.subjects_names.append(subject)

    def print_all_students(self):
        print(self.students)

    def print_all_subjects(self):
        print(self.subjects_names)

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
    diary.add_subject("math")
    diary.add_new_subjects_from_file("subjects.txt")
    diary.add_new_students_from_file("students.txt")
    diary.print_all_students()
    diary.print_all_subjects()
    diary.add_student_to_subject("Jan", "Kowalski", "math")
