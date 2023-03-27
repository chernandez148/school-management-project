from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///pet_stores.db')

Base = declarative_base()

# TEACHERS, STUDENTS, GRADES CLASSES


class Teachers(Base):
    __tablename__ = "teachers"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    subject = Column(String())

    grades = relationship('Grades', backref=backref('teachers'))

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'first_name: {self.first_name}, ' + \
            f'last_name: {self.last_name}, ' + \
            f'subject: {self.subject}'


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    grades = relationship('Grades', backref=backref('students'))

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'first_name: {self.first_name}, ' + \
            f'last_name: {self.last_name}'


class Grades(Base):
    __tablename__ = "grades"

    id = Column(Integer(), primary_key=True)
    teacher_id = Column(Integer(), ForeignKey('teacher.id'))
    student_id = Column(Integer(), ForeignKey('student.id'))
    grades = Column(String())

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'teacher_id: {self.teacher_id}, ' + \
            f'student_id: {self.student_id}, ' + \
            f'grades: {self.grades}'
