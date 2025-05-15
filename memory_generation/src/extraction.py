import spacy
from generative_agents.reverie.backend_server.persona.cognitive_modules.reflect import reflect
from generative_agents.reverie.backend_server.persona.cognitive_modules.reflect import generate_poig_score
from generative_agents.reverie.backend_server.persona.prompt_template.run_gpt_prompt import get_embedding

def extract_events_and_reflect(file_path, persona):
    """Given a path to a txt file generate a list of concept nodes"""

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    nlp = spacy.load("en_core_web_sm")

    # Process text
    doc = nlp(text)

    # Extract sentences
    sentences = [sent.text.strip() for sent in doc.sents]

    date = persona.scratch.curr_time
    for sentence in sentences:
        # Get poignancy
        event_poignancy = generate_poig_score(persona, "event", sentence)

        # Get embedding
        desc_embedding_in = sentence
        if "(" in sentence:
            desc_embedding_in = (desc_embedding_in.split("(")[1]
                                                .split(")")[0]
                                                .strip())
        if desc_embedding_in in persona.a_mem.embeddings:
            event_embedding = persona.a_mem.embeddings[desc_embedding_in]
        else:
            event_embedding = get_embedding(desc_embedding_in)
        event_embedding_pair = (desc_embedding_in, event_embedding)

        persona.a_mem.add_event(created=date, 
                                    expiration=None,
                                    s="someone", p="is", o="idle", # may need to fix later
                                    description=sentence,
                                    keywords=set(),
                                    poignancy=event_poignancy,
                                    embedding_pair=event_embedding_pair,
                                    filling=[])
        persona.scratch.importance_trigger_curr -= event_poignancy
        persona.scratch.importance_ele_n += 1
        reflect(persona)
        persona.a_mem.save("memory_generation/src/eren_jaeger/bootstrap_memory/associative_memory")