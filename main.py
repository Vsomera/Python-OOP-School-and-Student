# ACIT 2515 - W4 School Lab
# Vilmor Somera
# 01/27/23

import csv

class Student:
    all = [] # a class attribute list containing all the students
    def __init__(self, name: str, id: str, grades: list):
        self.name = name
        self.id = id
        self.grades = grades
        Student.all.append(self)

    def calculate_avg_grade(self):
        """ Method takes no parameters and calculates the average grade for student """
        avg_grade = 0
        for grade in self.grades:
            avg_grade += int(grade)
        return f"The calculated average grade for {self.name} is {avg_grade / len(self.grades)}%"

    def __repr__(self): 
        """ Formats the data to be more readable """
        return f"{self.__class__.__name__}('{self.name}', '{self.id}'. '{self.grades}')"

class School(Student):
    @classmethod
    def instantiate_student_info(cls):
        """ Gets student info from studetns.csv and grades.csv """

        with open("students.csv", "r") as file: # reads student csv
            reader = csv.DictReader(file)
            stu_info = list(reader)

        with open("grades.csv", "r") as file: # reads grades csv
            lines = file.readlines()

            for x in stu_info:  # loop for stu_info
                for y in lines: # loop for stu_grades
                    stu_grades = y.rstrip("\n").split(",")
                    stu_grade_id = stu_grades[0]
                    
                    
                    if (stu_grade_id == x["student_id"]): # matches id in grades to id in students csv: then initiates the student class
                        Student(
                            name = x["name"],
                            id = x["student_id"],   
                            grades = stu_grades[1:len(stu_grades)], #  a list of the student's grade
                        )

    def find_students_by_name(stu_name: str):
        """ Method Takes a string and returns a list containing all instances regardless of case """
        for student in Student.all:
            if stu_name.capitalize() in student.name:
                return student

    def find_students_by_id(stu_id: str):
        """ Method takes a string and returns a list containing all student instances whose student id is equal to the argument provided """
        for student in Student.all:
            if stu_id == student.id:
                return student
        
    def print_student_list():
        """ Method takes no params, when called prints out a list of all the student """
        for student in Student.all:
            print(student)

        
                

def main():
    School.instantiate_student_info() # reads both grade and student

    print(School.find_students_by_name("william")) # finds student by name
    print(School.find_students_by_id("A6900396")) # finds student id
    School.print_student_list()                   # prints all students when called
    print(School.find_students_by_id("A6667751").calculate_avg_grade()) # calculates the average grade of a student given a name or id
    print(School.find_students_by_name("brian").calculate_avg_grade()) 

if __name__ == "__main__":
    main()