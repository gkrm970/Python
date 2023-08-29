"""
Finally, let's update the main.py file to import and use these separate files:
"""
# main.py
from fastapi import FastAPI, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base, get_db
from models import User
from schemas import UserCreateRequest, UserResponse, UserUpdateRequest

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users", response_model=list[UserResponse])
def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdateRequest, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user = User(name=user.name, age=user.age)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User deleted successfully"}


"""
In this updated code, we have added the following endpoints:

PUT /users/{user_id}: This endpoint updates an existing user by their user_id. It expects a UserUpdateRequest model 
as the request body, which contains the updated name and age fields. If the user is not found, it returns a 404 
response with an appropriate error message. 

DELETE /users/{user_id}: This endpoint deletes an existing user by their user_id. If the user is not found, 
it returns a 404 response with an appropriate error message. Otherwise, it deletes the user from the database and 
returns a success message. 

Please note that in the above code, UserUpdateRequest is assumed to be a Pydantic model representing the request body 
for updating a user. You can define it in the schemas.py file similar to UserCreateRequest and UserResponse models. 

With these additional endpoints, you now have a complete set of CRUD operations for managing users in your FastAPI 
application. Feel free to customize and extend these endpoints as needed based on your application's requirements. 

In this updated main.py file, we import the necessary modules from the separate files: engine, SessionLocal, 
Base from database.py; User from models.py; and UserCreateRequest and UserResponse from schemas.py. 

We also include a get_db function that uses Depends to provide a database session to the API endpoints. This ensures 
that each request operates within its own database session and is properly closed afterward. 

The example now includes database integration with SQLAlchemy, a clear separation of concerns with separate files for 
the database module, database structure, and Pydantic models. This organization improves the maintainability and 
modularity of the codebase. 

Remember to install the necessary dependencies (sqlalchemy and pydantic) if you haven't done so already. Run the 
application using the same command as before: 

uvicorn main:app --reload   execute in terminal.

"""