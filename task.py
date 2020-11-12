import json


def add_class_to_diary_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    school_name = lines[0]
    class_name = lines[1]
    class_body = prepare_class_body(lines[2::])

    if school_name not in data:
        data[school_name] = {}
    data[school_name][class_name] = class_body
    with open('diaryData.json', 'w') as json_file:
        json.dump(data, json_file)


def load_diary_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


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
    for student_line in lines[1::]:
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
            "student_scores": student_grades[i]
        }
        subjects_body.append(subject)
    return subjects_body


def get_all_students():
    students = data['AGH']['classes'][0]['students']
    return ["{} {}".format(student['name'], student['surname']) for student in students]


def get_all_subjects():
    subjects = data['AGH']['classes'][0]['subjects']
    return subjects


if __name__ == '__main__':
    data = load_diary_data('diaryData.json')
    add_class_to_diary_data("medycyna_data.txt")
    print(get_all_students())
    print(get_all_subjects())

#########################

# TODO build json from files
# TODO add json to data


# TODO generate json from studens, subjects files

# TODO adding scores testing
# diary.add_student_score_in_subject("Jan", "Kowalski", 5, "math")
# diary.add_student_score_in_subject("Jan", "Kowalski", 1, "math")

# TODO print student average and average in subject
# diary.print_student_averages_in_all_subjects("Jan", "Kowalski")
# diary.print_student_average_score("Jan", "Kowalski")

# todo subjects averages
# diary.print_all_students_average_scores()
# diary.print_subject_average_scores("IT")
# diary.print_all_subjects_average_scores()

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

# change scores to grades
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
