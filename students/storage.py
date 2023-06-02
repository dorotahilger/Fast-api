from functools import lru_cache
from .schema import Student, Mark


STUDENTS: dict[int, Student] = {}
MARKS = {}

@lru_cache(maxsize=1)
def get_students_storage() -> dict[int, Student]:
    return STUDENTS

def get_marks():
    return MARKS