import json
import statistics


def load_diary_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def add_class_from_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    _school = lines[0]
    _class = lines[1]
    class_body = prepare_class_body(lines[2::])

    if _school not in data:
        data[_school] = {}
    data[_school][_class] = class_body
    save_data_to_file()


def prepare_class_body(lines):
    body = {}
    subjects = parse_subjects(lines[0])
    body["subjects"] = subjects
    body["students"] = parse_students(lines[1::], subjects)
    return body


def parse_subjects(subjects_string):
    return [subject.strip() for subject in subjects_string.split(";")]


def parse_students(lines, subjects):
    students = []
    for student_line in lines:
        students.append(prepare_student_body(student_line, subjects))
    return students


def prepare_student_body(student_line, subjects):
    student_info = [info.strip() for info in student_line.split(";")]
    student_grades = json.loads(student_info[3])
    subjects_body = prepare_student_subjects_body(student_grades, subjects)
    student_body = {"name": student_info[0], "surname": student_info[1], "attendance": student_info[2],
                    "subjects": subjects_body}
    return student_body


def prepare_student_subjects_body(student_grades, subjects):
    subjects_body = []
    for i in range(len(subjects)):
        subject = {
            "name": subjects[i],
            "student_grades": student_grades[i]
        }
        subjects_body.append(subject)
    return subjects_body


def save_data_to_file():
    with open('diaryData.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


# todo refactor
def add_student_grade_in_subject(name, surname, subject_name, grade):
    students = get_students_in_current_class()
    for student in students:
        if student['name'] == name and student['surname'] == surname:
            for subject in student['subjects']:
                if subject['name'] == subject_name:
                    subject['student_grades'].append(grade)
    save_data_to_file()


def get_all_students():
    result = {}
    for _school in data.keys():
        result[_school] = {}
        for _class in data[_school].keys():
            result[_school][_class] = ["{} {}".format(student['name'], student['surname']) for student in
                                       data[_school][_class]['students']]
    return result


def get_all_subjects():
    result = {}
    for _school in data.keys():
        result[_school] = list(data[_school].keys())
    return result


def get_students_in_current_class():
    return data[school_name][class_name]['students']


def get_all_students_names_in_current_class():
    return [[student['name'], student['surname']] for student in get_students_in_current_class()]


def get_averages_in_subject(subject_name):
    students = get_students_in_current_class()
    averages = {}
    for student in students:
        name, surname = student['name'], student['surname']
        names = "{} {}".format(name, surname)
        averages[names] = get_student_average_in_subject(name, surname, subject_name)
    return averages


def get_student_average_in_subject(name, surname, subject_name):
    grades = get_student_grades_in_subject(name, surname, subject_name)
    return statistics.mean(grades)


def get_student_grades_in_subject(name, surname, subject_name):
    student = get_student_by_personal_data(name, surname)
    subject = next(filter(lambda x: x['name'] == subject_name, student['subjects']), {})
    return subject['student_grades']


def get_student_by_personal_data(name, surname):
    students = get_students_in_current_class()
    return next(filter(lambda x: x['name'] == name and x['surname'] == surname, students), {})


def get_all_students_average_grades():
    students = get_all_students_names_in_current_class()
    averages = {}
    for student in students:
        name, surname = student[0], student[1]
        names = "{} {}".format(name, surname)
        averages[names] = get_student_average_from_all_subjects(name, surname)
    return averages


def get_student_average_from_all_subjects(name, surname):
    student = get_student_by_personal_data(name, surname)
    averages = []
    for subject in student['subjects']:
        averages.append(statistics.mean(subject['student_grades']))
    return statistics.mean(averages)


if __name__ == '__main__':
    data = load_diary_data('diaryData.json')
    # add_class_from_text_file("medycyna_data.txt")
    print(get_all_students())
    # print(get_all_subjects())

    school_name = "AGH"
    class_name = "medycyna"
    # add_student_grade_in_subject('Piotr', 'Konieczny', 'math', 5)
    # add_student_grade_in_subject('Zbigniew', 'Wesolek', 'biology', 5)

    # print(get_student_by_personal_data('Piotr', 'Konieczny'))
    # print(get_student_grades_in_subject('Piotr', 'Konieczny', 'math'))

    # print(get_student_grades_in_subject('Piotr', 'Konieczny', 'math'))
    # print(get_student_average_subject('Piotr', 'Konieczny', 'math'))
    # print(get_student_averages_in_all_subjects("Jan", "Kowalski"))
    # print(get_all_students_average_grades())

    # print(get_averages_in_subject("math"))

    # todo attendance
    # diary.print_student_attendance("Jan", "Kowalski")
    # diary.print_all_students_attendance()
    # diary.add_next_day_in_semester()
    # diary.print_all_students_attendance()
    # diary.add_attendance_to_student("Jan", "Kowalski")
    # diary.print_all_students_attendance()
    # diary.add_next_day_in_semester()
    # diary.add_attendance_to_all_students()
    # diary.print_all_students_attendance()

#########################

# todo ladowanie ocen z pliku
# todo jakis interfejs ktorym by sie dodawalo oceny, obecnosci itp


# todo think about adding to json from text files
# def add_class_to_diary_data(file_path, school_name, class_name):
#     class_body = prepare_class_body(file_path, class_name)
#     class_body["name"] = class_name
#
#     if school_name not in data:
#         data[school_name] = {}
#
#     if 'classes' not in data[school_name]:
#         data[school_name]['classes'] = []
#
#     if
#
#     data[school_name]['classes'].append(class_body)
#
#     with open('diaryData.json', 'w') as json_file:
#         json.dump(data, json_file)
