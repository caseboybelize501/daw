import os
import hashlib
from typing import List, Dict
from pathlib import Path

async def build_plugin_catalog() -> List[Dict]:
    plugin_catalog = []
    
    # macOS plugin paths
    mac_paths = [
        "/Library/Audio/Plug-Ins/VST3/",
        "/Library/Audio/Plug-Ins/Components/",
        "~/Library/Audio/Plug-Ins/VST3/",
        "~/Library/Audio/Plug-Ins/Components/"
    ]
    
    # Linux plugin paths
    linux_paths = [
        "~/.vst/",
        "~/.vst3/",
        "/usr/lib/vst/",
        "/usr/lib/vst3/"
    ]
    
    # Windows plugin paths (via Wine)
    win_paths = [
        "C:\\Program Files\\Common Files\\VST3\\"
    ]
    
    all_paths = mac_paths + linux_paths + win_paths
    
    for path in all_paths:
        try:
            expanded_path = os.path.expanduser(path)
            if not os.path.exists(expanded_path):
                continue
            
            for root, dirs, files in os.walk(expanded_path):
                for file in files:
                    if file.endswith(('.vst3', '.component', '.dll')):
                        plugin_path = os.path.join(root, file)
                        try:
                            with open(plugin_path, 'rb') as f:
                                binary_data = f.read()
                                hash_value = hashlib.sha256(binary_data).hexdigest()
                            
                            # Extract basic info (simplified)
                            plugin_info = {
                                "name": file.replace('.vst3', '').replace('.component', ''),
                                "path": plugin_path,
                                "hash": hash_value,
                                "format": "VST3" if file.endswith('.vst3') else "AU" if file.endswith('.component') else "VST",
                                "category": "effect",  # Simplified
                                "version": "1.0"
                            }
                            plugin_catalog.append(plugin_info)
                        except Exception as e:
                            print(f"Error processing plugin {plugin_path}: {e}")
        except Exception as e:
            print(f"Error scanning path {path}: {e}")
    
    return plugin_catalog