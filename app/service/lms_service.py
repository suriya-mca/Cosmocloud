from model.models import Student
from config.db import collection


async def create_student_service(student: Student):

	result = collection.insert_one(student.dict())
	return {"id": str(result.inserted_id)}