🧱 Features:

Frontend: Chat UI (React + Tailwind)

Backend: FastAPI server with OpenAI-compatible API format (/v1/chat/completions)

LLM: Load llama4-maverick model using HuggingFace transformers + vllm or llama-cpp-python

Session & history tracking via PostgreSQL or DuckDB

Authentication: optional JWT-based

🚢 Deployment Requirements:

Complete Docker Swarm setup with:

frontend service (React app)

backend service (FastAPI)

model service (LLM with GPU or CPU fallback)

optional db service (PostgreSQL or DuckDB file volume)

One-click deploy via docker stack deploy

Configurable with .env file

📦 Output:

Docker Swarm-compatible docker-compose.yml

Backend FastAPI app with chat endpoint

React frontend with nice chat UI

Script to download model (llama4-maverick)

Swarm deployment script with labels, health checks, restart policies

🧠 Additional Considerations:

Include token streaming support in backend (yield via FastAPI SSE or WebSocket)

Add system prompt/personality injection support

Optional rate limiting and logging

📁 Directory Structure:

bash
Copy
Edit
/llama-chat
  /frontend
  /backend
  /model
  /scripts
  docker-compose.yml
  .env
  deploy.sh
You can paste this directly in Codex or Claude and ask it to:

"Generate the full project based on the above specification step by step. Start with the folder structure and then implement each component (backend, frontend, Docker config)."

Bonus: One-liner Prompt for Codex
If you want a condensed version:

🚀 Build a ChatGPT-like full-stack project using llama4-maverick model with:

FastAPI backend (/v1/chat/completions)

React + Tailwind frontend

Docker Swarm support (frontend, backend, model, optional DB)

One-click deployment with docker stack deploy
Include streaming support, persona injection, model loading via HuggingFace or llama.cpp, and .env support. Output: full folder structure, source code, and deploy script.
