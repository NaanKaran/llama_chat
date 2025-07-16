# Llama Chat

Llama Chat is a planned chat application designed to demonstrate how a lightweight frontend can communicate with a backend that serves as a bridge to a large language model. The project aims to provide a template for rapid prototyping of LLM-based web apps.

## Project Goals

- Simple conversational interface backed by an LLM service
- Clearly separated frontend and backend components for easy customization
- Containerized setup to make development and deployment straightforward

## Planned Architecture

```
[Client (React)] <-> [Backend API] <-> [LLM Provider]
```

- **Frontend**: A React application that handles user interaction and displays chat history
- **Backend**: A lightweight API that accepts messages, forwards them to an LLM service (e.g., OpenAI or a self-hosted model), and streams responses back to the frontend
- **LLM Provider**: This can be any service exposing a chat completion API

## Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose
- Node.js (for local frontend development)
- Python 3.10+ (for local backend development)

## Environment Variables

The backend relies on the following variables:

- `LLM_PROVIDER_API_KEY` – API key for your language model provider
- `LLM_PROVIDER_URL` – Endpoint for the provider's API
- `PORT` – Port for the backend server (defaults to `8000`)

Frontend variables:

- `VITE_API_URL` – URL of the backend API

Create a `.env` file in each component to set these values when running locally.

## Setup and Running Locally

1. Clone this repository
2. Install dependencies for the frontend and backend
3. Set the environment variables
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

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Docker Usage

The repository includes a `docker-compose.yml` that builds both components and runs them together.

```bash
docker compose up --build
```

This will start the backend and frontend services so you can access the application at `http://localhost:3000`.

## Frontend Overview

- Built with Vite + React
- Communicates with the backend over a REST/streaming API
- Stores minimal state (chat history) in memory or browser storage

## Backend Overview

- Implemented with FastAPI (or similar framework)
- Provides endpoints to submit user messages and stream responses
- Handles authentication and relay to the LLM provider

## Contributing

This project is in its early stages. Feel free to fork it and experiment with alternative architectures or providers.

## License

MIT License
