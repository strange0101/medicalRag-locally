# Medical Hybrid RAG (Retrieval-Augmented Generation) System

🩺 **Medical Hybrid RAG** is an educational demo that combines vector-based document retrieval with a knowledge graph for answering medical questions using a local LLM (no external API required).

## Features
- Vector search over medical data using sentence embeddings
- Knowledge graph representing disease-symptom-treatment relationships
- Hybrid context combining text chunks and graph nodes
- Local LLM integration via Ollama for generating answers
- Interactive visualization of the medical knowledge graph with PyVis
- Built with Streamlit for an easy web UI

## Getting Started

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com/) installed and configured (optional, for LLM)
- Required Python packages installed (`pip install -r requirements.txt`)

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/medical-hybrid-rag.git
   cd medical-hybrid-rag
