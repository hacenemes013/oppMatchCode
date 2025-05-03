"""
Configuration settings for the project.
Contains API keys, model settings and other configuration parameters.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys - Make sure to add these to your .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Optional if using OpenAI as fallback
LAMA_API_KEY = os.getenv("LAMA_API_KEY")  # Optional if using Llama as fallback


os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY   
os.environ["GEMINI_API_KEY"] = GOOGLE_API_KEY  # Assuming Gemini uses the same API key

# Model Configuration
GEMINI_MODEL = "gemini-pro"  # or other Gemini model variants as needed

# Agent Configuration
MAX_ITERATIONS = 3
TEMPERATURE = 0.5
VERBOSE = True

# PDF Processing Configuration
PDF_CHUNK_SIZE = 1000
PDF_CHUNK_OVERLAP = 200