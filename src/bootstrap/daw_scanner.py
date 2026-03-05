import os
import subprocess
import plistlib
from typing import List, Dict

async def scan_daws() -> List[Dict]:
    daws = []
    
    # Logic Pro (macOS)
    logic_path = "/Applications/Logic Pro.app"
    if os.path.exists(logic_path):
        try:
            with open(os.path.join(logic_path, "Contents", "Info.plist"), 'rb') as f:
                info = plistlib.load(f)
                version = info.get("CFBundleShortVersionString", "Unknown")
                daws.append({
                    "name": "Logic Pro",
                    "version": version,
                    "project_format": "logic",
                    "cli_available": True
                })
        except Exception as e:
            print(f"Error reading Logic Pro info: {e}")
    
    # Ableton Live (macOS)
    ableton_path = "/Applications/Ableton Live.app"
    if os.path.exists(ableton_path):
        try:
            with open(os.path.join(ableton_path, "Contents", "Info.plist"), 'rb') as f:
                info = plistlib.load(f)
                version = info.get("CFBundleShortVersionString", "Unknown")
                daws.append({
                    "name": "Ableton Live",
                    "version": version,
                    "project_format": "live",
                    "cli_available": True
                })
        except Exception as e:
            print(f"Error reading Ableton info: {e}")
    
    # Reaper (macOS)
    reaper_path = "/Applications/REAPER.app"
    if os.path.exists(reaper_path):
        daws.append({
            "name": "Reaper",
            "version": "Unknown",
            "project_format": "reaper",
            "cli_available": True
        })
    
    # FL Studio (Windows via Wine)
    fl_studio_path = "/Applications/FL Studio.app"
    if os.path.exists(fl_studio_path):
        daws.append({
            "name": "FL Studio",
            "version": "Unknown",
            "project_format": "flstudio",
            "cli_available": True
        })
    
    return daws