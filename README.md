# Llama Chat

Llama Chat is a chat application that illustrates how a lightweight web frontend can talk to a backend which in turn forwards requests to a large language model provider. The repository serves as a simple template for prototyping your own LLM-powered apps.

## Project Goals

- Provide a minimal conversational interface backed by an LLM service
- Keep frontend and backend code clearly separated
- Offer containerized development and deployment

## Planned Architecture

```
[React Client] <-> [Backend API] <-> [LLM Provider]
```

- **Frontend** – Handles user input and renders chat history
- **Backend** – Receives messages, passes them to the LLM service and streams results
- **LLM Provider** – Any service that exposes a chat completion API

## Directory Structure

- `frontend/` – React client built with Vite
- `backend/` – FastAPI server acting as a proxy to the LLM provider
- `docker-compose.yml` – Compose file to run both services together
- `docker-stack.yml` – Swarm stack definition
- `deploy.sh` – Helper script for one-click deployment

## Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose
- Node.js for frontend development
- Python 3.10+ for backend development

## Environment Variables

Backend variables:

- `REPLICATE_API_TOKEN` – API token for Replicate (used when `LLAMA_MODEL_PATH` is not set)
- `LLAMA_MODEL` – Model reference to use with Replicate (defaults to `llama4:maverick`)
- `LLAMA_MODEL_PATH` – Path to a local GGUF model file; if provided the backend runs locally using `llama-cpp`
- `PORT` – Port for the backend server (defaults to `8000`)

Frontend variables:

- `VITE_API_URL` – URL of the backend API

Create a `.env` file in each component with values similar to the example below:

```
# Example using Replicate
REPLICATE_API_TOKEN=your-token
LLAMA_MODEL=llama4:maverick
PORT=8000
VITE_API_URL=http://localhost:8000

# Example using a local model
# LLAMA_MODEL_PATH=/path/to/model.gguf
```

## Setup and Running Locally

1. Clone this repository
2. Install dependencies for the frontend and backend
3. Add the required environment variables
4. Start the backend server
5. Start the frontend development server

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port $PORT
```
If `LLAMA_MODEL_PATH` is set to a local GGUF file, the backend will load it
using `llama-cpp` instead of contacting Replicate.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Docker Usage

If you prefer running everything in containers, use the helper script:

```bash
./deploy.sh
```

To deploy on a Docker Swarm cluster:

```bash
./deploy.sh swarm
```

Both methods start the services and expose the web UI at `http://localhost:3000`.

## Frontend Overview

- Built with Vite + React
- Communicates with the backend over REST or streaming endpoints
- Stores only minimal state such as chat history in memory or browser storage

## Backend Overview

- Implemented with FastAPI (or a similar framework)
- Provides endpoints to submit user messages and stream responses
- Relays authentication and requests to the LLM provider or runs a local model when `LLAMA_MODEL_PATH` is set

## Contributing

This project is in the early stages. Feel free to fork it and try alternative architectures or providers.

## License

MIT License