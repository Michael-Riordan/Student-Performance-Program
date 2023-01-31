
class AverageCalculator: #will also calculate and store total grades and averages from a group of students passed to functions
                         #necessary to create a new instance of this class for each different group
    
    def __init__(self, num_of_students, subjects): #stores total grades and average from the group as a whole
        self.num_of_students = num_of_students
        self.subjects = subjects
        self.math_average = 0
        self.science_average = 0
        self.history_average = 0
        self.english_average = 0
        self.geography_average = 0
        self.total_math_grade = 0
        self.total_science_grade = 0
        self.total_history_grade = 0
        self.total_english_grade = 0
        self.total_geography_grade = 0
        self.overall_average = 0

    def average_by_class(self, grades_by_class, number_of_students, subjects):

        for key in grades_by_class:
            grade = grades_by_class[key]
            if key == "math":
                self.total_math_grade += grade
            if key == "science":
                self.total_science_grade += grade
            if key == "history":
                self.total_history_grade += grade
            if key == "english":
                self.total_english_grade += grade
            if key == "geography":
                self.total_geography_grade += grade

        self.math_average = self.total_math_grade / number_of_students
        self.science_average = self.total_science_grade / number_of_students
        self.history_average = self.total_history_grade / number_of_students
        self.english_average = self.total_english_grade / number_of_students
        self.geography_average = self.total_geography_grade / number_of_students
        self.overall_average = (self.math_average + self.science_average + self.history_average + self.english_average + self.geography_average) / len(subjects)

    
    def find_hardest_subject(self):

        subject_averages = {"math": self.math_average,
                            "science": self.science_average, 
                            "history": self.history_average, 
                            "english": self.english_average,
                            "geography": self.geography_average
                            }

        lowest_average = self.math_average
        hardest_subject = None
        for key in subject_averages:
            average = subject_averages[key]
            if average < lowest_average:
                lowest_average = average
                hardest_subject = key

        return hardest_subject

    def find_easiest_subject(self):
        subject_averages = {"math": self.math_average,
                            "science": self.science_average, 
                            "history": self.history_average, 
                            "english": self.english_average,
                            "geography": self.geography_average
                            }

        highest_average = self.math_average
        easiest_subject = None
        for key in subject_averages:
            average = subject_averages[key]
            if average > highest_average:
                highest_average = average
                easiest_subject = key

        return easiest_subject

    def student_average(student, subjects):
        student_total_grade = 0
        num_of_subjects = len(subjects)
        for key in student:
            for subject in subjects:
                if key == subject:
                    grade = student[key]
                    student_total_grade += grade

        average = student_total_grade / num_of_subjects
        return average

    def average_student_grade(self, student_averages):
        return student_averages / self.num_of_students

    def subject_average(self, subject_total_grade):
        subject_average = subject_total_grade / self.num_of_students
        return subject_average

        
        

    







