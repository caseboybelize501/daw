import asyncio
from src.bootstrap.daw_scanner import scan_daws
from src.bootstrap.plugin_registry import build_plugin_catalog
from src.bootstrap.audio_hardware_scanner import scan_audio_hardware
from src.bootstrap.sample_library_scanner import scan_sample_libraries
from src.bootstrap.model_scanner import scan_models
from src.bootstrap.system_profile import AudioSystemProfile

async def scan_system():
    print("Starting system scan...")
    
    # Phase 1: DAW Detection
    daw_info = await scan_daws()
    
    # Phase 2: Plugin Registry
    plugin_catalog = await build_plugin_catalog()
    
    # Phase 3: Audio Hardware
    hardware_info = await scan_audio_hardware()
    
    # Phase 4: Sample Library Scan
    sample_catalog = await scan_sample_libraries()
    
    # Phase 5: Model Files + Inference
    model_files = await scan_models()
    
    # Create AudioSystemProfile
    profile = AudioSystemProfile(
        daw_info=daw_info,
        plugin_catalog=plugin_catalog,
        hardware_info=hardware_info,
        sample_catalog=sample_catalog,
        model_files=model_files
    )
    
    await profile.save()
    print("System scan complete.")
    return profile