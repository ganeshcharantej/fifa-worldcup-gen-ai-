# main.py
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask_concierge

app = FastAPI()

class FanRequest(BaseModel):
    query: str

@app.post("/api/chat")
async def chat_endpoint(request: FanRequest):
    # Pass the fan's query to the Antigravity agent
    answer = await ask_concierge(request.query)
    return {"response": answer}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)