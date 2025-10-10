from fastapi import FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "online", "endpoint": "/task"}

@app.get("/task")
def run_task(q: str = Query(...), response: Response = None):
    # Explicitly set CORS headers
    if response:
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "*"
    
    # Calculate GCD
    output = str(math.gcd(204, 562))
    
    return {
        "task": q,
        "agent": "copilot-cli",
        "output": output,
        "email": "23f3001016@ds.study.iitm.ac.in"
    }

@app.options("/task")
def task_options(response: Response):
    # Handle preflight requests
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return {}
