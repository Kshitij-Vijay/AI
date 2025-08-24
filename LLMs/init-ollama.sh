#!/bin/sh
ollama pull nomic-embed-text:latest
ollama pull llama2:latest
ollama serve
