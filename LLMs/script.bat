echo "Hello, this is my script running!"

# List directory contents (Windows command). If on Linux/macOS use `ls`.
dir

# Build your Docker images (make sure your Dockerfile is named properly)
docker build -t ollama .

# Pull models inside Ollama container (ensure Ollama container is running)
docker-compose exec ollama ollama pull nomic-embed-text:latest
docker-compose exec ollama ollama pull llama:latest
docker-compose exec ollama ollama pull smollm2:latest

# List the downloaded models inside Ollama container
docker-compose exec ollama ollama ls

# Run the Python app container interactively
docker-compose run --rm -it app

docker build -t app

