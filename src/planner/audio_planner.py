from src.bootstrap.system_profile import AudioSystemProfile
from src.agents.composition_agent import generate_composition
from src.agents.arrangement_agent import arrange_track
from src.agents.mix_agent import generate_mix
from src.agents.master_agent import apply_mastering

async def plan_audio_tasks(profile: AudioSystemProfile):
    """Plan audio production tasks based on system profile"""
    
    # Generate composition
    composition = await generate_composition(
        style="pop",
        key="C",
        tempo=120,
        length=32
    )
    
    # Arrange track
    arrangement = await arrange_track(
        composition=composition,
        available_plugins=profile.get_available_plugins(),
        available_samples=profile.get_available_samples()
    )
    
    # Generate mix
    mix = await generate_mix(arrangement)
    
    # Apply mastering
    mastered = await apply_mastering(mix)
    
    return {
        "composition": composition,
        "arrangement": arrangement,
        "mix": mix,
        "mastered": mastered
    }