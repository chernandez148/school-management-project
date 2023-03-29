from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import add_student, add_teacher, add_grade, get_student_classes
from db.models import Base, Students, Teachers, Grades

engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()


while True:
    command = input("Insert command: ")
    if command == "Add new Student":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        add_student(first_name, last_name)

    elif command == "Add new Teacher":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        subject = input("Enter subject: ")
        add_teacher(first_name, last_name, subject)

    elif command == "Add new Grade":
        teacher_id = input("Enter teacher ID: ")
        student_id = input("Enter student ID: ")
        grade = input("Enter grade: ")
        add_grade(teacher_id, student_id, grade)

    elif command == "search student":
        first_name = input("Enter student first name: ")
        class_info = get_student_classes(first_name)
        if class_info:
            print(f"Classes for {first_name}:")
            for subject, grade in class_info:
                print(f"{subject}: {grade}")
        else:
            print("No classes found.")

    elif command == "Quit":
        session.close()
        break

    else:
        print("Invalid command. Please try again.")
