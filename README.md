# Backend Intern Hiring Task

This project implements a backend API for managing student records using FastAPI and MongoDB.

## Features

- **Create Student**: Allows the creation of a new student record.
- **List Students**: Retrieves a list of student records with optional filtering by country and age.
- **Fetch Student**: Retrieves a specific student record by ID.
- **Update Student**: Updates the properties of a specific student record.
- **Delete Student**: Deletes a specific student record by ID.

## Technologies Used

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- MongoDB: A NoSQL database for storing student records.

## Usage

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

3. The API will be available at `http://localhost:8000/api/v1`.

## API Documentation

Swagger UI documentation for the API is available at `http://localhost:8000/docs`.

## Endpoints

- `POST /students`: Create a new student record.
- `GET /students`: List student records with optional filtering.
- `GET /students/{id}`: Fetch a specific student record by ID.
- `PATCH /students/{id}`: Update a specific student record by ID.
- `DELETE /students/{id}`: Delete a specific student record by ID.

## Deployment

This project is deployed on Render. You can access the deployed API [here](https://lms-latest.onrender.com/).

## Accessing API Documentation

Swagger UI documentation for the API is available at [https://lms-latest.onrender.com/docs](https://lms-latest.onrender.com/docs).
