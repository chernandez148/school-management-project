from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Teachers, Students, Grades


if __name__ == '__main__':
    engine = create_engine('sqlite:///school.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # DELETE TEACHERS,STUDENTS, and GRADES; CLEAR DATA ON INITIATION
    session.query(Teachers).delete()
    session.query(Students).delete()
    session.query(Grades).delete()

    teacher1 = Teachers(first_name="Regina",
                        last_name="Tran", subject="Science")
    teacher2 = Teachers(first_name="Juan", last_name="Chacon", subject="Math")
    teacher3 = Teachers(first_name="Lisa",
                        last_name="Cardoso", subject="History")

    session.add(teacher1)
    session.add(teacher2)
    session.add(teacher3)
    session.commit()

    student1 = Students(first_name='Billy', last_name="Bob")
    student2 = Students(first_name='Hannah', last_name='Smith')
    student3 = Students(first_name='George', last_name='Richards')
    student4 = Students(first_name='Sarah', last_name='Connor')

    session.add(student1)
    session.add(student2)
    session.add(student3)
    session.add(student4)
    session.commit()

    billys_grade_science = Grades(teachers_id=1, students_id=1, grade="B")
    billys_grade_math = Grades(teachers_id=2, students_id=1, grade="B")

    hannahs_grade_science = Grades(teachers_id=1, students_id=2, grade='A')
    hannahs_grade_math = Grades(teachers_id=2, students_id=2, grade="B")
    hannahs_grade_history = Grades(teachers_id=3, students_id=2, grade='C')

    george_grade_science = Grades(teachers_id=1, students_id=3, grade='C')
    george_grade_math = Grades(teachers_id=2, students_id=3, grade="B")
    george_grade_history = Grades(teachers_id=3, students_id=3, grade='B')

    sarah_grade_math = Grades(teachers_id=2, students_id=4, grade="B")

    session.add(billys_grade_science)
    session.add(billys_grade_math)

    session.add(hannahs_grade_science)
    session.add(hannahs_grade_math)
    session.add(hannahs_grade_history)

    session.add(george_grade_science)
    session.add(george_grade_math)
    session.add(george_grade_history)

    session.add(sarah_grade_math)
    session.commit()
