#!/bin/bash
set -e

MODE=${1:-compose}

if [ "$MODE" = "swarm" ]; then
    echo "Building images for swarm..."
    docker compose build
    echo "Deploying stack to swarm..."
    docker stack deploy -c docker-stack.yml llama_chat
else
    echo "Starting services with Docker Compose..."
    docker compose up --build
fi
