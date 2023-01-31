import json
import os
from student_sorter import StudentSorter
from average import AverageCalculator


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]


student_sorter = StudentSorter(SUBJECTS)
calculator = AverageCalculator(NUM_STUDENTS, SUBJECTS)


def load_report_card(directory, student_number): #opens the json files and returns the dict of each student
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

def main():
    starting_id = 0

    for i in range(NUM_STUDENTS):
        student_details = load_report_card("students", starting_id)
        student_sorter.student_by_year(student_details)
        grades_by_class = student_sorter.class_grades(student_details)
        calculator.average_by_class(grades_by_class, NUM_STUDENTS, SUBJECTS)
        starting_id += 1

    average_grade = calculator.overall_average
    hardest_subject = calculator.find_hardest_subject()
    easiest_subject = calculator.find_easiest_subject()
    print(f"Average Student Grade: {round(average_grade, 2)}")
    print(f"Hardest Subject: {hardest_subject}")
    print(f"Easiest Subject: {easiest_subject}")
    student_sorter.average_sorter_by_grade()
    best_year, worst_year = student_sorter.find_best_and_worst_year(1)
    print(f"Best Performing Grade: {best_year}")
    print(f"Worst Performing Grade: {worst_year}")
    best_student, worst_student = student_sorter.find_best_and_worst_student()
    print(f"Best Student ID: {best_student}")
    print(f"Worst Student ID: {worst_student}")
       
main()




    


