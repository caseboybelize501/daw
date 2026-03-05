import hashlib
from typing import Dict, List

# In-memory deduplication registry (simplified)
plugin_registry = {}
model_registry = {}
sample_registry = {}

async def register_plugin(plugin_info: Dict):
    """Register plugin with hash-based deduplication"""
    plugin_hash = plugin_info["hash"]
    if plugin_hash not in plugin_registry:
        plugin_registry[plugin_hash] = plugin_info
        return True
    return False

async def register_model(model_info: Dict):
    """Register model with hash-based deduplication"""
    model_hash = model_info["hash"]
    if model_hash not in model_registry:
        model_registry[model_hash] = model_info
        return True
    return False

async def register_sample(sample_info: Dict):
    """Register sample with hash-based deduplication"""
    sample_hash = sample_info["hash"]
    if sample_hash not in sample_registry:
        sample_registry[sample_hash] = sample_info
        return True
    return False