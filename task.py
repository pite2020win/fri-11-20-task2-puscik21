
class Diary:
    def __init__(self):
        self.students = []
        self.subjects_names = set()

    def add_new_subjects_from_file(self, file_path):
        file = open(file_path, "r")
        for subject in file.read().splitlines():
            self.add_subject(subject)

    def add_subject(self, subject_name):
        self.subjects_names.add(subject_name)

    def add_new_students_from_file(self, file_path):
        file = open(file_path, "r")
        full_names = [full_name.split(", ") for full_name in file.read().splitlines()]
        for full_name in full_names:
            self.add_new_student(full_name[0], full_name[1])

    def add_new_student(self, name, surname):
        student = Student(name, surname)
        self.students.append(student)

    def add_all_students_to_subjects(self):
        for student in self.students:
            for subject_name in self.subjects_names:
                student.add_to_subject(subject_name)

    def add_student_to_subject_by_student_names(self, name, surname, subject_name):
        student = next(filter(lambda s: s.name == name and s.surname == surname, self.students), None)
        student.add_to_subject(subject_name)

    def print_all_students(self):
        print(self.students)

    def print_all_subjects(self):
        print(self.subjects_names)

    def print_students_average_in_subject(self, subject):
        # todo
        pass

    def print_students_attendance(self):
        # todo
        pass

    def print_student_subject_average(self, student):
        # todo
        pass


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.attendance = 0
        self.average = 0
        self.subjects = set()

    def add_to_subject(self, subject_name):
        self.subjects.add(Subject(subject_name))

    def get_average(self):
        # todo count average from all subjects averages
        pass

    def get_attendance(self):
        # todo
        pass

    def __repr__(self):
        return self.name + " " + self.surname


class Subject:
    def __init__(self, name):
        self.name = name
        self.student_scores = []

    def add_score(self, score):
        self.student_scores.append(score)

    def get_scores_average(self):
        return sum(self.student_scores) / len(self.student_scores)

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    diary = Diary()
    diary.add_new_subjects_from_file("subjects.txt")
    diary.add_new_students_from_file("students.txt")
    diary.add_all_students_to_subjects()

    diary.print_all_students()
    diary.print_all_subjects()
    diary.add_student_to_subject_by_student_names("Jan", "Kowalski", "math")


# todo uzywac setow jesli chodzi o subjecty studenta i studentow w dzienniku
# todo zrobic obiekt subject jako cos duzego, z wlasna lista studentow