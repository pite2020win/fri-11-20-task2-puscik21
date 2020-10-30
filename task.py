# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.


import time as timer


class Diary:
    def __init__(self):
        self.students = []
        self.subjects_names = []

    # def act(self, action, time):
    #     if action == "keep_speed":
    #         self.keep_speed(time)
    #         timer.sleep(1)

    # def print_stats(self):
    #     print("(wheel angle= " + str(self.wheel_angle) + ", speed=" + str(self.speed) + ")")

    def add_student_to_subject(self, student, subject):
        pass

    def print_all_students(self):
        pass

    def print_students_average_in_subject(self, subject):
        pass

    def print_students_attendance(self):
        pass

    def print_student_subject_average(self, student):
        pass


class Student:
    def __init__(self, name, surname):
        self.subjects = []
        self.attendance = 0
        self.name = name
        self.surname = surname

    def get_average(self):
        pass

    def get_attendance(self):
        pass


class Subject:
    def __init__(self):
        self.name = 0
        self.student_scores = []

    def add_score(self, score):
        self.student_scores.append(score)

    def get_scores_average(self):
        return sum(self.student_scores) / len(self.student_scores)


if __name__ == '__main__':
    print('Hello')
