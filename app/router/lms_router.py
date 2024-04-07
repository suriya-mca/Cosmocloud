from fastapi import APIRouter
from model.models import Student
from service.lms_service import create_student_service, get_students_service


router = APIRouter()

@router.post("/students", status_code=201, tags=["lms"])
async def create_student(student: Student):
    
    return await create_student_service(student)

@router.get("/students", status_code=200, tags=["lms"])
async def get_students(country: str = None, age: int = None):

    return await get_students_service(country, age)
    