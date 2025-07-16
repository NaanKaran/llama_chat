import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import replicate

app = FastAPI(title="Llama Chat Backend")

# Default model reference for Replicate
LLAMA_MODEL = os.getenv("LLAMA_MODEL", "llama4:maverick")
client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

class Message(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Welcome to Llama Chat"}

@app.post("/chat")
async def chat(msg: Message):
    if client._api_token is None:
        raise HTTPException(status_code=500, detail="REPLICATE_API_TOKEN not configured")

    try:
        output = client.run(LLAMA_MODEL, input={"prompt": msg.text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if isinstance(output, (list, tuple)):
        response = "".join(map(str, output))
    else:
        response = str(output)

    return {"response": response}
