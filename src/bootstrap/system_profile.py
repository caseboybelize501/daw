import json
from typing import List, Dict
from pathlib import Path
from pydantic import BaseModel

class AudioSystemProfile(BaseModel):
    daw_info: List[Dict]
    plugin_catalog: List[Dict]
    hardware_info: Dict
    sample_catalog: List[Dict]
    model_files: List[Dict]
        
    @classmethod
    async def load(cls):
        try:
            with open("system_profile.json", "r") as f:
                data = json.load(f)
                return cls.model_validate(data)
        except Exception as e:
            print(f"Error loading profile: {e}")
            return None

    async def save(self):
        data = self.model_dump()
        with open("system_profile.json", "w") as f:
            json.dump(data, f, indent=2)
        
    def get_available_plugins(self, category: str = None):
        if not category:
            return self.plugin_catalog
        return [p for p in self.plugin_catalog if p["category"] == category]
    
    def get_available_samples(self, format_type: str = None):
        if not format_type:
            return self.sample_catalog
        return [s for s in self.sample_catalog if s["format"] == format_type]