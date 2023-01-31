from average import AverageCalculator


class StudentSorter: #sorts groups of students into grade

    def __init__(self, subjects):
        self.subjects = subjects

        self.students_by_year = {1: [], 2: [], 3: [], 4: [],
                                 5: [], 6: [], 7: [], 8: []}

        self.average_by_year = {1: 0, 2: 0, 3: 0, 4: 0,
                                5: 0, 6: 0, 7: 0, 8: 0}

        


    def class_grades(self, student): #Will return a dictionary of only subjects/grades for a single student
        grades_by_class = {"math": 0, "science": 0, "history": 0, "english": 0, "geography": 0}
        for key in student:
            for subject in self.subjects:
                if key == subject:
                    grades_by_class[subject] = student[key]

        return grades_by_class

    def student_by_year(self, students):  #will sort students into dict depending on year
        for key in students:
            if key == "grade":
                year = students[key]
                self.students_by_year[year].append(students)

    def averages_by_year(self, students, year):   #will create overall average for each year and place them into average_by_year dict
        
        for grade in students:
            if grade == year:
                grade_calculator = AverageCalculator(len(students[year]), self.subjects)
                student_list = students[grade]

                for student in student_list:
                    grades_by_class = self.class_grades(student)
                    grade_calculator.average_by_class(grades_by_class, len(students[year]), self.subjects)              
                    overall_average = grade_calculator.overall_average
                
        self.average_by_year[year] = overall_average

    def average_sorter_by_grade(self): #will pass years 1-8 to averages_by_year function 
        for year in range(1, 9):
            self.averages_by_year(self.students_by_year, year)

    def find_best_and_worst_year(self, minimum_year): #takes minimum year in order to set lowest and highest average for future comparison
        lowest_average = self.average_by_year[minimum_year]
        highest_average = self.average_by_year[minimum_year]
        best_year = None
        worst_year = None

        for year in self.average_by_year:
            grade = self.average_by_year[year]

            if grade < lowest_average:
                lowest_average = self.average_by_year[year]
                worst_year = year

            if grade > highest_average:
                highest_average = self.average_by_year[year]
                best_year = year

        return best_year, worst_year

    def find_best_and_worst_student(self):
        best_average = 0
        worst_average = 100000
        best_student = None
        worst_student = None

        for year in self.students_by_year:
            students = self.students_by_year[year]

            for student in students:

                student_id = student["id"]
                average = AverageCalculator.student_average(student, self.subjects)

                if average > best_average:
                    best_student = student_id
                    best_average = average

                if average < worst_average:
                    worst_student = student_id
                    worst_average = average

        return best_student, worst_student