students = {}
courses = {}
marks = {}


def input_students():
    num_student = int(input("Enter the student's number:"))
    for i in range(num_student):
        student_ID = (input("Enter student ID:"))
        student_name = (input("Enter student name:"))
        student_DoB = (input("Enter student DoB:"))
        students[student_ID] = {"Name": student_name, "DoB": student_DoB}


def input_courses():
    number_of_course = int(input("Enter the course's number:"))
    for i in range(number_of_course):
        course_ID = input("Enter course ID:")
        course_name = input("Enter course name:")
        courses[course_ID] = {"Name": course_name}


def input_marks():
    course_ID = input("Enter course id:")
    for student_ID in students:
        mark = float(
            input(f"Enter the mark for {students[student_ID]['Name']}:"))
        if student_ID not in marks:
            marks[student_ID] = {}
        marks[student_ID][course_ID] = mark


def show_mark():
    course_ID = input("Enter course id:")
    for student_ID in students:
        if student_ID in marks and course_ID in marks[student_ID]:
            print(
                f"{students[student_ID]['Name']}: {marks[student_ID][course_ID]}")
        else:
            return


def list_students():
    for student_ID in students:
        print(f"{student_ID} : {students[student_ID]['Name']}")


def list_courses():
    for course_ID in courses:
        print(f"{course_ID} : {courses[course_ID]['Name']}")


input_students()
input_courses()
input_marks()
list_students()
list_courses()
show_mark()
