from fastapi import FastAPI
from models import Todo

# starts an API class
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI World"}

# Fake database for demo purposes
todo_list = []

# Get All Todos
@app.get("/todos")
async def get_todos():
    return {"todo_list": todo_list}

# Get Single Todo item
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo_item in todo_list:
        if todo_item.id == todo_id:
            return {"todo": todo_item}
    return {"Message": "No todos found"}

# Create Todo
@app.post("/todos")
async def create_todos(todo_item: Todo):
    todo_list.append(todo_item)
    return {"Message": "Todo Item Added"}

# Update a Todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_object: Todo):
    for todo_item in todo_list:
        if todo_item.id == todo_id:
            todo_item.id = todo_id
            todo_item.item = todo_object.item
            return {"todo": todo_item}
    return {"Message": "No todos found"}

# Delete a Todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo_item in todo_list:
        if todo_item.id == todo_id:
            todo_list.remove(todo_item)
            return {"Message": "Todo item has been deleted"}
    return {"Message": "No todos found"}