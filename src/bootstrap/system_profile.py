import json
from typing import List, Dict
from pathlib import Path

class AudioSystemProfile:
    def __init__(self, daw_info: List[Dict], plugin_catalog: List[Dict], hardware_info: Dict, sample_catalog: List[Dict], model_files: List[Dict]):
        self.daw_info = daw_info
        self.plugin_catalog = plugin_catalog
        self.hardware_info = hardware_info
        self.sample_catalog = sample_catalog
        self.model_files = model_files
        
    @classmethod
    async def load(cls):
        try:
            with open("system_profile.json", "r") as f:
                data = json.load(f)
                return cls(**data)
        except Exception as e:
            print(f"Error loading profile: {e}")
            return None
    
    async def save(self):
        data = {
            "daw_info": self.daw_info,
            "plugin_catalog": self.plugin_catalog,
            "hardware_info": self.hardware_info,
            "sample_catalog": self.sample_catalog,
            "model_files": self.model_files
        }
        
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