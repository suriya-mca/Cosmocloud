from model.models import Student
from config.db import collection


async def create_student_service(student: Student):

	result = collection.insert_one(student.dict())
	return {"id": str(result.inserted_id)}

async def get_students_service(country, age):

	filters = {}
	if country:
		filters["address.country"] = country
	if age:
		filters["age"] = {"$gte": age}

	students = list(collection.find(filters, {"_id": 0, "name": 1, "age": 1}))
	return {"data": [dict(student) for student in students]}