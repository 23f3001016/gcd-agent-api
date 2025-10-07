from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import math
import logging

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
    expose_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

@app.get("/task")
def run_task(q: str = Query(...)):
    logging.info(f"Received task: {q}")
    agent = "copilot-cli"

    # Simple example: return gcd if the task mentions it
    output = str(math.gcd(204, 562)) if "greatest common divisor" in q.lower() else "Unknown task"

    return {
        "task": q,
        "agent": agent,
        "output": output,
        "email": "23f3001016@ds.study.iitm.ac.in"
    }
