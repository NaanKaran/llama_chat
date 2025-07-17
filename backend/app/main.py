import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import replicate

try:
    from llama_cpp import Llama
except ImportError:  # pragma: no cover - optional dependency
    Llama = None

app = FastAPI(title="Llama Chat Backend")

# Local model path enables llama.cpp backend
LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH")

# Default model reference for Replicate
LLAMA_MODEL = os.getenv("LLAMA_MODEL", "llama4:maverick")

if LLAMA_MODEL_PATH:
    if Llama is None:
        raise RuntimeError("llama-cpp-python must be installed for local mode")
    llm = Llama(model_path=LLAMA_MODEL_PATH)
    client = None
else:
    client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))

class Message(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Welcome to Llama Chat"}

@app.post("/chat")
async def chat(msg: Message):
    if LLAMA_MODEL_PATH:
        try:
            result = llm(msg.text, max_tokens=128)
            output = result["choices"][0]["text"]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        return {"response": output.strip()}

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
