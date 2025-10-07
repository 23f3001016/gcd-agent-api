from fastapi import FastAPI, Query
import math
import logging
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

logging.basicConfig(level=logging.INFO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow all origins (for testing)
    allow_methods=["GET"],     # Allow GET requests
    allow_headers=["*"],
    expose_headers=["*"]       # Allow all headers
)


@app.get("/task")
def run_task(q: str = Query(...)):
    logging.info(f"Received task: {q}")

    agent_name = "copilot-cli"  # simulated agent
    output = ""

    # Only simulate GCD task
    if "greatest common divisor" in q.lower() or "gcd" in q.lower() or "204 and 562" in q:
        output = str(math.gcd(204, 562))
    else:
        output = "Unknown task"

    logging.info(f"Agent: {agent_name} | Output: {output}")

    return {
        "task": q,
        "agent": agent_name,
        "output": output,
        "email": "23f3001016@ds.study.iitm.ac.in"
    }
