from fastapi import APIRouter
from model.models import Student
from service.lms_service import create_student_service


router = APIRouter()

@router.post("/students", status_code=201, tags=["lms"])
async def create_student(student: Student):
    
    return await create_student_service(student)