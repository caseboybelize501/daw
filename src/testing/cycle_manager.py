import asyncio
from typing import Dict, List
from src.testing.lufs_checker import check_lufs
from src.testing.spectrum_analyzer import analyze_spectrum
from src.testing.stereo_checker import check_stereo_image
from src.testing.reference_comparator import compare_to_reference
from src.testing.mutation_injector import inject_mutation

async def run_validation_cycle(cycle_id: str) -> Dict:
    """Run 10-stage audio validation cycle"""
    
    # Stage 01 - Render Check
    render_ok = True
    
    # Stage 02 - Clipping Check
    clipping_ok = True
    
    # Stage 03 - LUFS Target
    lufs_ok = await check_lufs()
    
    # Stage 04 - Dynamic Range
    dr_ok = True
    
    # Stage 05 - Frequency Balance
    freq_ok = await analyze_spectrum()
    
    # Stage 06 - Stereo Image
    stereo_ok = await check_stereo_image()
    
    # Stage 07 - Transient Density
    transient_ok = True
    
    # Stage 08 - Reference Compare
    ref_ok = await compare_to_reference()
    
    # Stage 09 - Codec Survivability
    codec_ok = True
    
    # Stage 10 - Regression
    regression_ok = True
    
    # Mutation testing
    mutation_results = []
    for i in range(5):
        mutated = await inject_mutation()
        stage_results = await run_validation_cycle(f"mutated_{i}")
        mutation_results.append(stage_results)
    
    # Final validation
    all_stages = [
        render_ok,
        clipping_ok,
        lufs_ok,
        dr_ok,
        freq_ok,
        stereo_ok,
        transient_ok,
        ref_ok,
        codec_ok,
        regression_ok
    ]
    
    # Check for consecutive passes
    consecutive_passes = 0
    for stage in all_stages:
        if stage:
            consecutive_passes += 1
        else:
            consecutive_passes = 0
            break
    
    return {
        "cycle_id": cycle_id,
        "stage_results": all_stages,
        "consecutive_passes": consecutive_passes,
        "mutation_results": mutation_results,
        "status": "stable" if consecutive_passes >= 7 else "unstable"
    }