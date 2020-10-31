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

    def add_student_to_subject(self, name, surname, subject_name):
        student = self.get_student_by_personal_data(name, surname)
        student.add_to_subject(subject_name)

    def add_student_score_in_subject(self, name, surname, score, subject_name):
        student = self.get_student_by_personal_data(name, surname)
        student.add_score_in_subject(score, subject_name)

    def get_student_by_personal_data(self, name, surname):
        student = next(filter(lambda s: s.name == name and s.surname == surname, self.students), None)
        if student is not None:
            return student
        else:
            raise Exception("No student {} {} in diary".format(name, surname))

    def print_all_students(self):
        print(self.students)

    def print_all_subjects(self):
        print(self.subjects_names)

    def print_all_subjects_average_scores(self, subject):
        # todo
        pass

    def print_subject_average_scores(self, subject):
        # todo
        pass

    def print_all_students_average_scores(self, student, subject_name):
        # todo
        pass

    def print_student_average_score(self, student, subject_name):
        # todo
        pass

    def print_student_averages_in_all_subjects(self, name, surname):
        print("\n{} {} scores are:".format(name, surname))
        for subject_name in self.subjects_names:
            self.print_student_average_in_subject(name, surname, subject_name)

    def print_student_average_in_subject(self, name, surname, subject_name):
        student = self.get_student_by_personal_data(name, surname)
        print("{} average score in {} is {}".format(student, subject_name, student.get_subject_average(subject_name)))

    def print_all_students_attendance(self):
        # todo
        pass

    def print_student_attendance(self):
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

    def add_score_in_subject(self, score, subject_name):
        subject = self.get_subject_by_name(subject_name)
        subject.add_score(score)

    def get_subject_by_name(self, subject_name):
        subject = next(filter(lambda s: s.name == subject_name, self.subjects), None)  # todo None -> Subject("")
        if subject is not None:
            return subject
        else:
            raise Exception("Student is not in subject {}".format(subject_name))

    def get_average(self):
        # todo count average from all subjects averages
        pass

    def get_subject_average(self, subject_name):
        subject = self.get_subject_by_name(subject_name)
        return subject.get_scores_average()

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
        if len(self.student_scores) == 0:
            return "NaN"
        else:
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

    diary.add_student_score_in_subject("Jan", "Kowalski", 5, "math")
    diary.add_student_score_in_subject("Jan", "Kowalski", 1, "math")
    diary.print_student_averages_in_all_subjects("Jan", "Kowalski")

# todo uzywac setow jesli chodzi o subjecty studenta i studentow w dzienniku
# todo zrobic obiekt subject jako cos duzego, z wlasna lista studentow
# todo ladowanie ocen z pliku
