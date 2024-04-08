from fastapi import HTTPException
from bson import ObjectId
from model.models import Student
from config.db import collection


async def create_student_service(student: Student):

	result = collection.insert_one(student.dict())
	return {"id": str(result.inserted_id)}

async def get_students_service(country: str, age: int):

	filters = {}
	if country:
		filters["address.country"] = country
	if age:
		filters["age"] = {"$gte": age}

	students = list(collection.find(filters, {"_id": 0, "name": 1, "age": 1}))
	return {"data": [dict(student) for student in students]}

async def fetch_student_service(id: str):

	student = collection.find_one({"_id": ObjectId(id)})
	if not student:
		raise HTTPException(status_code=404, detail="Student not found")

	student["_id"] = str(student["_id"])
	return student

async def update_student_service(id: str, student: Student):

	result = collection.update_one({"_id": ObjectId(id)}, {"$set": student.dict()})
	if result.modified_count == 0:
		raise HTTPException(status_code=404, detail="Student not found")

	return {"message": "Student updated successfully"}

async def delete_student_service(id: str):

	result = collection.delete_one({"_id": ObjectId(id)})
	if result.deleted_count == 0:
		raise HTTPException(status_code=404, detail="Student not found")
    
	return {"message": "Student deleted successfully"}