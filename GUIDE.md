# LLM.DAW - Setup and Usage Guide

## Overview

LLM.DAW is an autonomous audio production system that uses AI to compose, arrange, mix, and master music. It scans your audio environment and learns from every production to improve future results.

---

## System Requirements

### Minimum Requirements
- **Python**: 3.10 or higher
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 2GB for dependencies + space for audio files
- **Audio**: PortAudio-compatible audio hardware

### Optional (for full functionality)
- **Docker**: For running Redis, Neo4j, and ChromaDB services
- **DAW Software**: Logic Pro, Ableton Live, Reaper, or FL Studio
- **VST/AU Plugins**: For sound generation and processing
- **Sample Libraries**: WAV, AIFF, NKI, or SFZ format samples
- **MIDI Controllers**: For input and control

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/llm-daw/llm.daw.git
cd llm.daw
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Core dependencies include:**
- `fastapi` - Web framework
- `librosa` - Audio analysis
- `music21` - Music theory engine
- `sounddevice` - Audio I/O
- `python-rtmidi` - MIDI support
- `chromadb` - Vector memory storage
- `neo4j` - Knowledge graph
- `redis` - Task queue backend
- `celery` - Distributed task processing

### Step 3: (Optional) Set Up Docker Services

For full memory and learning capabilities:

```bash
docker-compose up -d
```

This starts:
- **Redis** (port 6379) - Task queue
- **Neo4j** (ports 7474, 7687) - Signal chain graph
- **ChromaDB** (port 8000) - Vector embeddings

---

## Running the System

### Start the API Server

```bash
python src/main.py
```

The server will:
1. Run a system scan on startup
2. Detect available DAWs, plugins, and audio hardware
3. Start the FastAPI server on `http://localhost:8000`

### Access the API

- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **System Profile**: http://localhost:8000/api/system/profile

---

## API Endpoints

### System Information

#### `GET /api/system/profile`
Returns the current system profile with detected hardware and plugins.

**Response:**
```json
{
  "daw_info": [],
  "plugin_catalog": [],
  "hardware_info": {
    "audio_interfaces": [...],
    "midi_controllers": [],
    "sample_rate_supported": [44100, 48000, 96000],
    "bit_depth_supported": [24, 32]
  },
  "sample_catalog": [],
  "model_files": []
}
```

#### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "daw_detected": true,
  "plugins_indexed": true,
  "consecutive_passes": 7,
  "memory_hit_rate": 0.95
}
```

### Music Generation

#### `POST /api/composition/generate`
Generate a MIDI composition.

**Parameters:**
- `style` (string): Genre (e.g., "electronic", "jazz", "classical")
- `key` (string): Musical key (e.g., "C", "Am", "F#m")
- `tempo` (integer): BPM (e.g., 120)
- `length` (integer): Bars (e.g., 16)

**Example:**
```bash
curl -X POST "http://localhost:8000/api/composition/generate?style=electronic&key=Am&tempo=128&length=16"
```

#### `POST /api/mix/generate`
Generate a mixing chain for a track.

**Parameters:**
- `track_id` (string): Identifier for the track

**Example:**
```bash
curl -X POST "http://localhost:8000/api/mix/generate?track_id=track_001"
```

### Testing & Validation

#### `GET /api/test/cycle/{cycle_id}`
Get validation cycle results.

**Example:**
```bash
curl http://localhost:8000/api/test/cycle/cycle_001
```

---

## System Scan Details

On startup, LLM.DAW performs a 5-phase system scan:

| Phase | Component | Description |
|-------|-----------|-------------|
| 1 | DAW Detection | Scans for installed DAWs (Logic, Ableton, Reaper, FL Studio) |
| 2 | Plugin Registry | Indexes VST, VST3, and AU plugins |
| 3 | Audio Hardware | Detects audio interfaces and MIDI controllers |
| 4 | Sample Libraries | Scans for WAV, AIFF, NKI, SFZ samples |
| 5 | Model Files | Finds GGUF models for inference |

### Scan Output Locations

- **Profile**: `system_profile.json` (in project root)
- **Logs**: Console output during startup

---

## Music Theory Engine

The system uses `music21` for composition:

- **Chord Progressions**: Genre-aware harmonic structures
- **Melody Generation**: Scale-constrained melodic lines
- **Rhythm Patterns**: Tempo-appropriate rhythmic motifs

### Supported Styles
- Electronic
- Jazz
- Classical
- Rock
- Pop
- Hip-Hop

### Supported Keys
- All major keys (C, D, E, F, G, A, B, and accidentals)
- All minor keys (Am, Em, Dm, etc.)

---

## Validation Cycle

The system runs a 10-stage validation cycle:

1. **Render Check** - Audio renders without errors
2. **Clipping Check** - No digital clipping detected
3. **LUFS Target** - Meets loudness standards
4. **Dynamic Range** - Appropriate dynamics preserved
5. **Frequency Balance** - Full spectrum representation
6. **Stereo Image** - Proper stereo field
7. **Transient Density** - Rhythmic clarity
8. **Reference Compare** - Matches reference tracks
9. **Codec Survivability** - Survives MP3/AAC encoding
10. **Regression** - No quality degradation

**7 consecutive passes** are required for stability confirmation.

---

## Memory Systems

### 1. Mix Decision Memory
Stores successful mixing decisions by genre and style.

### 2. Signal Chain Graph (Neo4j)
Tracks: `Processor → Parameter → Sonic Outcome` relationships.

### 3. Sonic Signature Library (ChromaDB)
Vector embeddings of genre-specific sonic profiles.

### 4. Meta-Learning Index
Optimizes production approach selection based on past success.

---

## Troubleshooting

### "No module named 'rtmidi'"
```bash
pip install python-rtmidi
```

### "PortAudio not found"
- **Windows**: Install [Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- **macOS**: `brew install portaudio`
- **Linux**: `sudo apt-get install portaudio19-dev`

### "System scan failed"
Check that all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Docker services not starting
```bash
docker-compose down
docker-compose up -d
```

---

## File Structure

```
llm.daw/
├── src/
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # Data models
│   ├── bootstrap/           # System scanning
│   │   ├── system_scanner.py
│   │   ├── daw_scanner.py
│   │   ├── plugin_registry.py
│   │   ├── audio_hardware_scanner.py
│   │   └── sample_library_scanner.py
│   ├── agents/              # AI agents
│   │   ├── composition_agent.py
│   │   ├── arrangement_agent.py
│   │   ├── analysis_agent.py
│   │   └── mix_agent.py
│   ├── theory/              # Music theory
│   │   └── music21_wrapper.py
│   ├── testing/             # Validation
│   │   └── cycle_manager.py
│   └── memory/              # Learning systems
│       ├── mix_decision_store.py
│       └── signal_chain_graph.py
├── models/                  # ML models (GGUF)
├── docker-compose.yml       # Docker services
├── requirements.txt         # Python dependencies
└── GUIDE.md                 # This file
```

---

## Next Steps

1. **Run the system**: `python src/main.py`
2. **Check the API docs**: http://localhost:8000/docs
3. **Generate a composition**: Use the `/api/composition/generate` endpoint
4. **Review system profile**: Check detected hardware at `/api/system/profile`

For development updates and progress tracking, see [PROJECT.md](./PROJECT.md).
