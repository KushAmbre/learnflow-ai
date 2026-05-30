# Inside your utility file (let's say it's named llm_config.py)
from langchain_community.llms import Ollama

# Add the format and temperature settings here
llm = Ollama(
    model="llama3",
    format="json",          # Forces the local model to output valid JSON
    temperature=0.0         # Strips creativity to keep format highly rigid
)

def get_llm():
    return llm