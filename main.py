from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
STUDENTS = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

class Student(StudentCreateSchema):
    id: int


app = FastAPI()

@app.post("/student/")
async def create_item(student: StudentCreateSchema):
    s = Student(first_name=student.first_name, last_name=student.last_name, id=len(STUDENTS)+1)
    STUDENTS[s.id] = s
    return s

class StudentUpdateSchema():
    @app.get("/student/<id>")
    async def read_item(student: StudentCreateSchema):
     return {"student_id": student_id}
@app.get("/students")
async def read_item():
    return STUDENTS