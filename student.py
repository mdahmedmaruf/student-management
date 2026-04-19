class StudentDatabse:
    student_list = []

    def add_student(self, student):
        self.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled) -> None:
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"Student {self.__student_id} has been enrolled.")
        else:
            print("Trying to enroll a student who is already enrolled.")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"Student {self.__student_id} has been dropped.")
        else:
            print("Trying to drop a student who is not enrolled.")

    def view_student_info(self):
        print(
            f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, {self.__is_enrolled}"
        )


s_db = StudentDatabse()
s_db.add_student(Student("S101", "Ahmed", "CSE", True))
s_db.add_student(Student("S102", "Karim", "EEE", True))
s_db.add_student(Student("S103", "Rahim", "Math", False))


def menu():
    while True:
        print(
            """
            ------------ Student Management System ------------

            1. View All Students
            2. Enrolled Student
            3. Drop Student
            4. Exit    
            """
        )

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print()
            for student in s_db.student_list:
                student.view_student_info()

        elif choice == 2:
            enroll_id = input("Enter Student ID to enroll: ").strip()
            flag = 0
            for student in s_db.student_list:
                if student.get_student_id() == enroll_id:
                    student.enroll_student()
                    flag = 1
                    break
            if not flag:
                print("Invalid Student ID.")

        elif choice == 3:
            drop_id = input("Enter Student ID to drop: ").strip()
            flag = 0
            for student in s_db.student_list:
                if student.get_student_id() == drop_id:
                    student.drop_student()
                    flag = 1
                    break
            if not flag:
                print("Invalid Student ID.")

        elif choice == 4:
            print("Thanks for using our Student Management!")
            break

        else:
            print("Invalid query. Try a number between 1 and 4.")


menu()
