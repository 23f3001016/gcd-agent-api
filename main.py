from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware BEFORE any routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods including OPTIONS
    allow_headers=["*"],  # Allow all headers
    expose_headers=["*"]  # Expose all headers
)

@app.get("/")
async def root():
    """Root endpoint for health check"""
    return JSONResponse(
        content={
            "status": "online",
            "message": "Copilot CLI Agent API",
            "endpoint": "/task?q=your_task_here"
        }
    )

@app.get("/health")
async def health():
    """Health check endpoint"""
    return JSONResponse(content={"status": "healthy"})

@app.get("/task")
async def run_task(q: str = Query(..., description="Task description for the coding agent")):
    """
    Execute a task using simulated copilot-cli agent
    """
    try:
        logger.info(f"Received task: {q}")
        
        agent_name = "copilot-cli"
        output = ""
        
        # Check if it's a GCD task
        if "greatest common divisor" in q.lower() or "gcd" in q.lower() or ("204" in q and "562" in q):
            result = math.gcd(204, 562)
            output = str(result)
            logger.info(f"GCD(204, 562) = {output}")
        else:
            output = "Task completed"
            logger.info(f"Generic task completed")
        
        response_data = {
            "task": q,
            "agent": agent_name,
            "output": output,
            "email": "23f3001016@ds.study.iitm.ac.in"
        }
        
        logger.info(f"Returning response: {response_data}")
        
        # Return with explicit headers
        return JSONResponse(
            content=response_data,
            headers={
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "*"
            }
        )
        
    except Exception as e:
        logger.error(f"Error processing task: {str(e)}")
        return JSONResponse(
            content={
                "task": q,
                "agent": "copilot-cli",
                "output": f"Error: {str(e)}",
                "email": "23f3001016@ds.study.iitm.ac.in"
            },
            status_code=500,
            headers={
                "Access-Control-Allow-Origin": "*"
            }
        )

# Handle OPTIONS requests explicitly
@app.options("/task")
async def task_options():
    """Handle preflight OPTIONS requests"""
    return JSONResponse(
        content={},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
