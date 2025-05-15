from .extraction import extract_events_and_reflect
from generative_agents.reverie.backend_server.persona.persona import Persona

def main():
    eren_jaeger = Persona("Eren Jaeger", "memory_generation/src/eren_jaeger", eren_jaeger=True)
    path = "memory_generation/docs/biography.txt"
    extract_events_and_reflect(path, eren_jaeger)

if __name__ == '__main__':
    main()