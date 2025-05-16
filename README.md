# Eren Jaeger Agent

## Overview
The goal of this project was to insert an Eren Jaeger persona into the generative agents playground produced by Park et al.

## Project Structure
- `generative_agents/` - This is the original code used in the paper, but it is slightly modified
- `memory_generation/` - This is where I generated Eren Jaeger's persona

## Prerequisites
Set up a virtual environment and install everything from requirements.txt. Read the generative_agents README for more information.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/enteigss/eren-jaeger-generative-agent.git
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\Activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Generate Eren's persona
```bash
python -m memory_generation.src.main
```

2. Run simulation according to steps in the generative_agents README

## License
Apache 2.0

## Acknowledgments
- This project uses code from the paper "Generative Agents: Interactive Simulcra of Human Behavior" by Park et al. (2023). The original implementation can be found at https://github.com/joonspk-research/generative_agents/tree/main and the paper can be found at https://arxiv.org/abs/2304.03442. 
