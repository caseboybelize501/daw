import json
from typing import Dict, List
from src.bootstrap.system_profile import AudioSystemProfile

async def arrange_track(composition: Dict, available_plugins: List[Dict], available_samples: List[Dict]) -> Dict:
    """Arrange composition for available instruments and sample libraries"""
    
    # Get system profile
    profile = await AudioSystemProfile.load()
    if not profile:
        raise Exception("No system profile found")
    
    # Route tracks to available plugins/samples
    arranged_tracks = []
    
    for track in composition["tracks"]:
        # Find suitable plugin or sample library
        instrument = track["instrument"]
        role = track["role"]
        
        # Simplified routing logic
        if role == "melody":
            plugin = next((p for p in available_plugins if p["category"] == "synth"), None)
            sample = next((s for s in available_samples if s["format"] in ["wav", "aif"]), None)
        elif role == "bass":
            plugin = next((p for p in available_plugins if p["category"] == "instrument"), None)
            sample = next((s for s in available_samples if s["format"] in ["wav", "aif"]), None)
        else:
            plugin = next((p for p in available_plugins if p["category"] == "effect"), None)
            sample = None
        
        arranged_tracks.append({
            "instrument": instrument,
            "role": role,
            "plugin": plugin["name"] if plugin else None,
            "sample": sample["name"] if sample else None,
            "midi_data": track["midi_data"]
        })
    
    return {
        "composition": composition,
        "arranged_tracks": arranged_tracks,
        "routing_info": "auto-routed based on available plugins and samples"
    }