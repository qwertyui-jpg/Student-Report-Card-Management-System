import json
class Student:
    def __init__(self):
        print("\n\t=== Welcome to Student Report Card Management System ===\n")
        print("\n\t\tEnter the details of the student: \n")
        print("===================================================================================\n")
        self.name =  str(input("Enter the name of the student: "))
        self.roll_number =  int(input("Enter the roll number of the student: "))
        self.standard = int(input("Enter the standard of the student: "))
        
        print("\nMarks obtained are : ")
        self.marks = {
            
            'Mathematics & Statistics': int(input("Enter the marks for Mathematics & Statistics:  ")),
            'English': int(input("Enter the marks for English: ")),
            'Science': int(input("Enter the marks for Science: ")),
            'Social Science': int(input("Enter the marks for Social Science: ")),
            'Hindi': int(input("Enter the marks for Hindi: "))
        }
        self.marks 
        self.total_marks = 0
        self.total_average = 0.0
        self.grade = ''
        self.attendance = 0.0

    def calculate_total_marks_average(self):
        self.total_marks = sum(self.marks.values())
        self.total_average = self.total_marks / len(self.marks)
        return self.total_marks, self.total_average
    
    def calculate_grade(self):
        if self.total_average >= 90:
            self.grade = 'A+'
        elif self.total_average>= 80:
            self.grade = 'A'
        elif self.total_average >= 70:
            self.grade = 'B+'
        elif self.total_average >= 60:
            self.grade = 'B'
        elif self.total_average >= 50:
            self.grade = 'C'
        elif self.total_average >= 40:
            self.grade = 'D'
        else:
            self.grade = 'F'
        return self.grade
    
    def get_attendance(self):
        print("\nAttendance should be in percentage (0-100)")
        self.attendance = float(input("Enter the attendance of the student: "))
        if self.attendance >= 75:
            print("Attendance is satisfactory")
        else:
            print("Attendance is not satisfactory")
        return self.attendance
    
    
    
    def get_Student_detail(self):
        print("\n=====================================================================\n")
        print("Student Details are :")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Total Marks are : {self.total_marks}"),
        print(f"Total Average is : {self.total_average}"),
        print(f"Grade is : {self.grade}")
        print(f"Attendance is : {self.attendance} %")
        if (self.attendance >= 75) & (self.total_average >= 40):
            print(f"you are passed and promoted to {self.standard + 1} standard")
        else:
            print(f"you are failed and not promoted to {self.standard + 1} standard")
           

    
students = []

while True:
    obj = Student()
    obj.calculate_total_marks_average()
    obj.calculate_grade()
    obj.get_attendance()
    obj.get_Student_detail()
    students.append(obj)

    choice = input("\nDo you want to add another student details ? (yes/no): ").strip().lower()
    if choice == 'yes':
        break
    elif choice == 'no':
        print("\n\tThank you for using the Student Report Card Management System")
        break
    

