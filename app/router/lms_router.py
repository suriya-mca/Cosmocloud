from fastapi import APIRouter
from model.models import Student
from service.lms_service import create_student_service, get_students_service, fetch_student_service, update_student_service, delete_student_service


router = APIRouter()

@router.post("/students", status_code=201, tags=["lms"])
async def create_student(student: Student):
    
    return await create_student_service(student)

@router.get("/students", status_code=200, tags=["lms"])
async def get_students(country: str, age: int):

    return await get_students_service(country, age)

@router.get("/students/{id}", status_code=200, tags=["lms"])
async def fetch_student(id: str):

    return await fetch_student_service(id)

@router.patch("/students/{id}", status_code=200, tags=["lms"])
async def update_student(id: str, student: Student):

    return await update_student_service(id, student)

@router.delete("/students/{id}", status_code=200, tags=["lms"])
async def delete_student(id: str):

    return await delete_student_service(id)