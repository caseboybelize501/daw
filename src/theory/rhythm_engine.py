import random
from typing import List, Dict

async def generate_rhythm_pattern(tempo: int, length: int) -> Dict:
    """Generate rhythmic pattern"""
    # Simplified rhythm generation
    patterns = [
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 0]
    ]
    
    pattern = random.choice(patterns)
    
    return {
        "pattern": pattern,
        "tempo": tempo,
        "length": length,
        "beat": "quarter"
    }

async def generate_groove(style: str, tempo: int) -> List[Dict]:
    """Generate groove for different styles"""
    grooves = {
        "pop": [1, 0, 1, 0],
        "hiphop": [1, 1, 0, 0],
        "jazz": [1, 0, 1, 1]
    }
    
    return [
        {"step": i, "active": bool(grooves.get(style, [1, 0, 1, 0])[i])} for i in range(4)
    ]