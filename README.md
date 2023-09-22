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

- use pydantic for data validation
- Create a class item as a model/item