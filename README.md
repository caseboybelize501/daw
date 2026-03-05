# LLM.DAW - Autonomous Audio Production Jarvis

A self-learning, autonomous audio production system that composes, arranges, mixes, and masters music using AI.

## Overview

LLM.DAW is a revolutionary audio production system that scans your entire audio stack (DAWs, plugins, hardware, sample libraries) and learns from every mix that didn't.

### Key Features

- **System Scan**: Detects installed DAWs, plugins, audio interfaces, and sample libraries
- **Self-Learning Memory**: Builds a knowledge base of what signal chain decisions produced what sonic outcomes
- **Autonomous Production**: Generates complete musical productions from concept to master
- **Perceptual Quality Control**: Validates audio quality through 10-stage validation cycles

### Architecture


┌─────────────┐
│   Voice     │
└──────┬──────┘
       │
┌──────▼──────┐
│ Planner LLM │
└──────┬──────┘
       │
┌──────▼──────┐
│ Agent       │
│ Controller  │
└──────┬──────┘
       │
┌──────▼──────┐
│ SystemScan  │
│ Composition │
│ Arrangement │
│ Mix         │
│ Master      │
│ Analysis    │
│ Learn       │
└─────────────┘


### System Requirements

- Python 3.10+
- Docker (for full functionality)
- Audio hardware with PortAudio support
- MIDI controllers (optional)

### Installation

bash
# Clone the repository
git clone https://github.com/llm-daw/llm.daw.git

cd llm.daw

# Install dependencies
pip install -r requirements.txt

# Run the system
python src/main.py


### Usage

1. Start the system: `python src/main.py`
2. The system will automatically scan your audio environment
3. Use the API endpoints to generate compositions and mixes

### API Endpoints

- `GET /api/system/profile` - Get current system profile
- `POST /api/composition/generate` - Generate MIDI composition
- `POST /api/mix/generate` - Generate mixing chain
- `GET /api/test/cycle/{id}` - Get validation cycle results
- `GET /health` - Health check endpoint

### Memory Systems

1. **Mix Decision Memory**: Stores what worked for different genres and styles
2. **Signal Chain Graph**: Tracks processor → parameter → sonic outcome relationships
3. **Sonic Signature Library**: Genre-specific sonic profiles
4. **Meta-Learning Index**: Production approach optimization

### Validation Cycle

The system runs a 10-stage validation cycle with 7 consecutive passes required for stability:

1. Render Check
2. Clipping Check
3. LUFS Target
4. Dynamic Range
5. Frequency Balance
6. Stereo Image
7. Transient Density
8. Reference Compare
9. Codec Survivability
10. Regression

### Contributing

Contributions are welcome! Please submit a pull request with your improvements.

### License

MIT License