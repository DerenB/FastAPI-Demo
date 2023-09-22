# FastAPI-Demo

- [Tutorial Source Video](https://www.youtube.com/watch?v=cbASjoZZGIw)
- Learning &amp; Notes on FastAPI
- basic python
- async out the box
- Data validation is built in with Pydantic
- Typed

# Step 0: Run FastAPI Server

- Run Server
  - CLI: `uvicorn main:app --reload`
    - "main" is the name of the app we picked

# Step 1: Setup

- Create virtual environment
- Install Packages:
  - pip install fastapi
  - pip install "uvicorn[standard]" 
    - (runs the server)
- Create `main.py`
- Code Block:
```
from fastapi import FastAPI

# starts an API class
app = FastAPI()

@app.get("/")
async def root():
  return {
    "message": "Hello FastAPI World"
  }
```

# Step 2: Create CRUD actions

### Create

```
@app.post("/todos")
async def create_todos(todo_item: Todo):
  todo_list.append(todo_item)
  return {"Message": "Todo Item Added"}
```

### Read

```
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
```

### Update

```
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_object: Todo):
  for todo_item in todo_list:
    if todo_item.id == todo_id:
      todo_item.id = todo_id
      todo_item.item = todo_object.item
      return {"todo": todo_item}
  return {"Message": "No todos found"}
```

### Delete

```
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
  for todo_item in todo_list:
    if todo_item.id == todo_id:
      todo_list.remove(todo_item)
      return {"Message": "Todo item has been deleted"}
  return {"Message": "No todos found"}
```
