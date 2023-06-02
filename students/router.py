
from fastapi import APIRouter, HTTPException
from .storage import STUDENTS
from .schema import StudentCreateSchema, Student

router = APIRouter()
@router.get("/")
async def get_students():
    return STUDENTS


@router.post("/")
async def create_student(student: StudentCreateSchema):
    id = len(STUDENTS) + 1
    new_student = Student(**student.dict(), id=id)
    STUDENTS[id] = new_student
    return new_student

@router.get("/")
async def read_item():
    return STUDENTS

@router.put("/")
async def update_item(student_id: int, first_name: str, last_name: str):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        student = STUDENTS[student_id]
        student.first_name = first_name
        student.last_name = last_name
    return student

@router.post("/{student_id}/marks/{ocena}")
async def add_mark(student_id: int):
    student = STUDENTS[student_id]
