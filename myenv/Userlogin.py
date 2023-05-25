from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.security import OAuth2PasswordBearer, HTTPBasicCredentials

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["school"]

# Create OAuth2PasswordBearer authentication scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Create HTTPBasicCredentials authentication scheme
basic_scheme = HTTPBasicCredentials(username="johndoe", password="password")

# Create User and login endpoint
@app.post("/user")
def create_user(user: dict):
    db.users.insert_one(user)

@app.post("/login")
def login(credentials: HTTPBasicCredentials):
    user = db.users.find_one({"username": credentials.username})
    if user and user["password"] == credentials.password:
        access_token = oauth2_scheme.create_access_token(user)
        return {"access_token": access_token}
    else:
        return {"error": "Invalid username or password"}

# Create login user with authentication and session timeout endpoint
@app.post("/login_with_authentication_and_session_timeout")
def login_with_authentication_and_session_timeout(credentials: HTTPBasicCredentials):
    user = db.users.find_one({"username": credentials.username})
    if user and user["password"] == credentials.password:
        access_token = oauth2_scheme.create_access_token(user)
        refresh_token = oauth2_scheme.create_refresh_token(user)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "session_timeout": 3600,
        }
    else:
        return {"error": "Invalid username or password"}

if __name__ == "__main__":
    app.run()
