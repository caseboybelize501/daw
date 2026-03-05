from music21 import *
from typing import List, Dict

async def voice_chord(chord_notes: List[str], key: str) -> List[Dict]:
    """Voice a chord with proper voice leading"""
    # Simplified voicing logic
    return [
        {"note": note, "octave": 4} for note in chord_notes
    ]

async def generate_chord_progression(key: str, style: str, length: int) -> List[Dict]:
    """Generate a chord progression with voice leading"""
    # Simplified progression generation
    progressions = {
        "pop": ["I", "V", "vi", "IV"],
        "jazz": ["Imaj7", "V7", "vi", "IV"]
    }
    
    chords = progressions.get(style, ["I", "V", "iv", "v"])
    return [
        {"chord": chord, "notes": ["C4", "E4", "G4"]} for chord in chords
    ]