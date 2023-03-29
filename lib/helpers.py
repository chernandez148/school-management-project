from db.models import Students, Teachers, Grades
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)


def add_student(first_name, last_name):
    session = Session()
    new_student = Students(first_name=first_name, last_name=last_name)
    session.add(new_student)
    session.commit()
    student_id = new_student.id
    student_name = f"{new_student.first_name} {new_student.last_name}"
    session.close()
    print(f"Added new student: {student_name} (ID: {student_id})")
    return student_id, student_name


def add_teacher(first_name, last_name, subject):
    session = Session()
    new_teacher = Teachers(first_name=first_name,
                           last_name=last_name, subject=subject)
    session.add(new_teacher)
    session.commit()
    teacher_id = new_teacher.id
    teacher_name = f"{new_teacher.first_name} {new_teacher.last_name}"
    session.close()
    print(f"Added new teacher: {teacher_name} (ID: {teacher_id})")
    return teacher_id, teacher_name


def add_grade(teacher_id, student_id, grade):
    session = Session()  # create a new session object
    new_grade = Grades(teachers_id=teacher_id,
                       students_id=student_id, grade=grade)
    session.add(new_grade)
    session.flush()  # flush to generate IDs before committing
    session.commit()
    grade_id = new_grade.id
    teacher_name = session.query(Teachers).filter_by(id=teacher_id).first()
    student_name = session.query(Students).filter_by(id=student_id).first()
    session.close()
    print(f"Added new grade: {grade} (ID: {grade_id}, {teacher_name.first_name} {teacher_name.last_name}, {student_name.first_name} {student_name.last_name})")
    return grade_id, teacher_id, student_id, grade


def get_student_classes(first_name):
    session = Session()
    student = session.query(Students).filter_by(first_name=first_name).first()
    if not student:
        print(f"No student found with first name '{first_name}'.")
        session.close()
        return []

    grades = student.grades
    class_info = []
    for grade in grades:
        teacher = grade.teachers
        class_info.append((teacher.subject, grade.grade))
    session.close()
    return class_info
