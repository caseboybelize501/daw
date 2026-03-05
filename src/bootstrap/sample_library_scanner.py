import os
import hashlib
from typing import List, Dict

async def scan_sample_libraries() -> List[Dict]:
    sample_catalog = []
    
    # Common paths for sample libraries
    sample_paths = [
        "~/Documents/Native Instruments/",
        "~/Samples/",
        "/Library/Application Support/",
        "~/Music/Samples/"
    ]
    
    for path in sample_paths:
        try:
            expanded_path = os.path.expanduser(path)
            if not os.path.exists(expanded_path):
                continue
            
            for root, dirs, files in os.walk(expanded_path):
                for file in files:
                    # Scan for common sample formats
                    if file.endswith(('.nki', '.sfz', '.wav', '.aif', '.aiff')):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'rb') as f:
                                binary_data = f.read()
                                hash_value = hashlib.sha256(binary_data).hexdigest()
                            
                            sample_info = {
                                "name": file,
                                "path": file_path,
                                "hash": hash_value,
                                "format": file.split('.')[-1].lower(),
                                "size": os.path.getsize(file_path)
                            }
                            sample_catalog.append(sample_info)
                        except Exception as e:
                            print(f"Error processing sample {file_path}: {e}")
        except Exception as e:
            print(f"Error scanning path {path}: {e}")
    
    return sample_catalog