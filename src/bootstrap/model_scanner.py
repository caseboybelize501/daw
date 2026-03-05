import os
import hashlib
from typing import List, Dict

async def scan_models() -> List[Dict]:
    model_files = []
    
    # Standard GGUF paths
    gguf_paths = [
        "~/models/",
        "./models/",
        "/opt/models/"
    ]
    
    for path in gguf_paths:
        try:
            expanded_path = os.path.expanduser(path)
            if not os.path.exists(expanded_path):
                continue
            
            for root, dirs, files in os.walk(expanded_path):
                for file in files:
                    if file.endswith('.gguf'):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'rb') as f:
                                binary_data = f.read()
                                hash_value = hashlib.sha256(binary_data).hexdigest()
                            
                            model_info = {
                                "name": file,
                                "path": file_path,
                                "hash": hash_value,
                                "size": os.path.getsize(file_path)
                            }
                            model_files.append(model_info)
                        except Exception as e:
                            print(f"Error processing model {file_path}: {e}")
        except Exception as e:
            print(f"Error scanning path {path}: {e}")
    
    # Probe inference servers
    server_ports = [11434, 8000, 1234, 8080]
    
    return model_files