# 2. Write a menu driven python program to perform following operations into binary file
#    student.dat
#    1) Add new student 2) Show all students 3) Search student 4) Exit
#    The binary file student.dat contains [rollno, name, marks]

def add_new_student(file_name):
    print("Enter record of student:")

    with open(file_name, "ab") as file_object:  # append binary
        rollno = int(input("Enter rollno: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        student_record = [rollno, name, marks]  # list

        # write student_record (list) into file_object (binary)
        pickle.dump(student_record, file_object)
        print("Added student record.")


def show_all_students(file_name):
    with open(file_name, "rb") as file_object:  # read binary
        while True:
            try:
                student_record = pickle.load(file_object)
                print("Rollno:", student_record[0],
                      "Name:", student_record[1],
                      "Marks:", student_record[2])
            except EOFError:
                break


def search_student(file_name):
    rollno = int(input("Enter rollno for search: "))

    student_records = []
    with open(file_name, "rb") as file_object:  # read binary
        while True:
            try:
                student_record = pickle.load(file_object)
                if student_record[0] == rollno:
                    print("Rollno:", student_record[0],
                          "Name:", student_record[1],
                          "Marks:", student_record[2])
            except EOFError:
                break


def mainmenu():
    file_name = "./student_marks_record.dat"

    while True:
        print("\nChoices available:")
        print("1. Add New Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("0: Exit")
        choice = int(input("Enter choice:"))

        if choice == 1:
            add_new_student(file_name)
        elif choice == 2:
            show_all_students(file_name)
        elif choice == 3:
            search_student(file_name)
        elif choice == 0:
            print("\nExiting...")
            break


mainmenu()
