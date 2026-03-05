import random
from typing import Dict, List

async def inject_mutation() -> Dict:
    """Inject small parameter mutations to test robustness"""
    
    # Perturb mix parameters
    mutations = {
        "bus_compression_ratio": random.uniform(0.5, 2.0),
        "master_limiter_threshold": random.uniform(-1.0, 1.0),
        "eq_shelf": random.uniform(-3.0, 3.0),
        "reverb_decay": random.uniform(0.6, 1.4)
    }
    
    return mutations