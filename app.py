from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

#frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    with open("index.html") as f:
        return HTMLResponse(content=f.read())

class InputData(BaseModel):
    data: str  
    #the platform is expecting a string input

@app.post("/transform")
def transform(input_data: InputData):
    chars = sorted(input_data.data)
    return {"word": chars}



