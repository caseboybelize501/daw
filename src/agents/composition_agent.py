import json
from typing import Dict, List
from src.theory.music21_wrapper import MusicTheoryEngine
from src.bootstrap.system_profile import AudioSystemProfile

async def generate_composition(style: str, key: str, tempo: int, length: int) -> Dict:
    """Generate MIDI composition using music theory and learned patterns"""
    
    # Get system profile
    profile = await AudioSystemProfile.load()
    if not profile:
        raise Exception("No system profile found")
    
    # Use music21 for composition
    theory_engine = MusicTheoryEngine()
    
    # Generate chord progression
    chords = theory_engine.generate_chord_progression(key, style, length)
    
    # Generate melody
    melody = theory_engine.generate_melody(chords, key, tempo)
    
    # Generate rhythm pattern
    rhythm = theory_engine.generate_rhythm_pattern(tempo, length)
    
    # Create composition structure
    composition = {
        "style": style,
        "key": key,
        "tempo": tempo,
        "length": length,
        "chord_progression": chords,
        "melody": melody,
        "rhythm": rhythm,
        "tracks": [
            {
                "instrument": "piano",
                "role": "melody",
                "midi_data": "base64_encoded_midi_data",
                "patch_suggestion": "default_piano"
            },
            {
                "instrument": "bass",
                "role": "bass",
                "midi_data": "base64_encoded_midi_data",
                "patch_suggestion": "default_bass"
            }
        ]
    }
    
    return composition