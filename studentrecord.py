
#intializing dictionary
student_grades = { }

#add a new element
def add_student(name, grade):
    student_grades[name]= grade
    #[joy] = 100
    print(f"Added {name} with a {grade}")
    #added joy with 100

#update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        #joy = 200
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")   

#delete a student   
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted")
    else:
        print(f"{name} is not found!")     

#view all students 
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print(f"No students found/added")


def main():
    while True:
        print('/n Student Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice="))
        if choice ==1:
            name = input("enter student name=")
            grade = input("enter student grade=")
            add_student(name, grade)

        elif choice == 2:
            name = input("enter student name=")
            grade = input("enter student grade=")
            update_student(name, grade)

        elif choice == 3:
            name = input("enter student name=")
            delete_student(name)

        
        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("closing the program....")
            break
        else:
            print("Invalid choice")
            
main()
