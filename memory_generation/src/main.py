from .extraction import extract_events_and_reflect
from generative_agents.reverie.backend_server.persona.persona import Persona

def main():
    mikasa_ackerman = Persona("Mikasa Ackerman", "memory_generation/src/mikasa_ackerman")
    path = "memory_generation/docs/mikasa-bio.txt"
    extract_events_and_reflect(path, mikasa_ackerman)

if __name__ == '__main__':
    main()