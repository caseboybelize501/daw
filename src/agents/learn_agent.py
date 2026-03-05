import json
from typing import Dict, List
from src.memory.mix_decision_store import MixDecisionStore
from src.memory.signal_chain_graph import SignalChainGraph
from src.memory.sonic_signatures import SonicSignatureLibrary
from src.memory.meta_learner import MetaLearner

async def learn_from_mix(mix_result: Dict) -> None:
    """Learn from mix results and update memory systems"""
    
    # Store mix decision in ChromaDB
    await MixDecisionStore.store_decision(mix_result)
    
    # Update signal chain graph in Neo4j
    await SignalChainGraph.update_from_mix(mix_result)
    
    # Update sonic signature library
    await SonicSignatureLibrary.update_from_mix(mix_result)
    
    # Update meta-learner
    await MetaLearner.update_from_mix(mix_result)