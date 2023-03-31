from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import admin_page, teacher_page, student_page
from db.models import Base, Students, Teachers, Grades
import sys

engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

BLUE = "\033[34m"


def blue_print(*args, **kwargs):
    print(BLUE, end="")
    print(*args, **kwargs)
    sys.stdout.flush()


print = blue_print

page = 1

while True:

    if page == 1:
        select = int(input(f'''{BLUE}
        Please select who you are:
        
        1 - Admin
        2 - Teachers
        3 - Students
        4 - Log Out{BLUE}
        ENTER: '''))
        if select == 1:
            admin_page()
        elif select == 2:
            teacher_page()
        elif select == 3:
            student_page()
        elif select == 4:
            Session().close()
            break
        else:
            print(BLUE + "Error, invalid selecton.")
