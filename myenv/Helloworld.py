from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["school"]

# Create API to print "Hello World"
@app.get("/")
def hello_world():
    return "Hello World!"

# Create API for a School to perform CRUD operations for teachers or students or both.
@app.get("/teachers")
def get_teachers():
    return db.teachers.find()

@app.post("/teachers")
def create_teacher(teacher: dict):
    db.teachers.insert_one(teacher)

@app.put("/teachers/{teacher_id}")
def update_teacher(teacher_id: str, teacher: dict):
    db.teachers.update_one({"_id": teacher_id}, {"$set": teacher})

@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: str):
    db.teachers.delete_one({"_id": teacher_id})

@app.get("/students")
def get_students():
    return db.students.find()

@app.post("/students")
def create_student(student: dict):
    db.students.insert_one(student)

@app.put("/students/{student_id}")
def update_student(student_id: str, student: dict):
    db.students.update_one({"_id": student_id}, {"$set": student})

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    db.students.delete_one({"_id": student_id})

# Create API to assign students to a particular teacher
@app.post("/assign_student_to_teacher")
def assign_student_to_teacher(student_id: str, teacher_id: str):
    db.students.update_one({"_id": student_id}, {"$set": {"teacher_id": teacher_id}})

if __name__ == "__main__":
    app.run()