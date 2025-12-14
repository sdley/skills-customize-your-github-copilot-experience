from fastapi import FastAPI

app = FastAPI(title="Task Management API")

# In-memory storage for tasks
tasks = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API"}

# TODO: Implement the following endpoints:
# GET /tasks - Return all tasks
# GET /tasks/{id} - Return a single task by ID
# POST /tasks - Create a new task
# PUT /tasks/{id} - Update an existing task
# DELETE /tasks/{id} - Delete a task

# TODO: Create Pydantic models for Task validation
# Example:
# class Task(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     completed: bool = False
