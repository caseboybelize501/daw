import chromadb
from typing import Dict, List

async def store_decision(mix_result: Dict) -> None:
    """Store mix decision in ChromaDB"""
    
    # Simplified storage logic
    client = chromadb.Client()
    collection = client.get_or_create_collection("mix_decisions")
    
    # Store mix result
    collection.add(
        documents=[str(mix_result)],
        metadatas=[{
            "genre": mix_result.get("genre", "unknown"),
            "tempo": mix_result.get("tempo", 0),
            "key": mix_result.get("key", "C")
        }],
        ids=[f"decision_{len(collection.get())}"]
    )