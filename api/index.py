from fastapi import FastAPI, Query
from mangum import Mangum
import math
import logging

app = FastAPI()

# Logging
logging.basicConfig(level=logging.INFO)

@app.get("/task")
def run_task(q: str = Query(..., description="Natural-language coding task")):
    logging.info(f"Received task: {q}")

    agent_name = "copilot-cli"  # Simulated agent
    output = ""

    # Simple “AI agent simulation”
    if "greatest common divisor" in q.lower():
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

# Adapter for Vercel serverless
handler = Mangum(app)
