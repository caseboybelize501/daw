import librosa
import pyloudnorm
import numpy as np
from typing import Dict, List

async def analyze_audio(file_path: str) -> Dict:
    """Perform perceptual audio measurements"""
    
    # Load audio file
    y, sr = librosa.load(file_path)
    
    # LUFS measurement
    meter = pyloudnorm.Meter(sr)
    lufs = meter.integrated_loudness(y)
    
    # Dynamic range
    dr = np.max(y) - np.min(y)
    
    # Frequency spectrum balance
    spectrum = np.abs(librosa.stft(y))
    freq_balance = np.mean(spectrum, axis=1)
    
    # Stereo correlation
    if len(y.shape) > 1:
        stereo_corr = np.corrcoef(y[0], y[1])[0, 1]
    else:
        stereo_corr = 1.0
    
    return {
        "lufs": lufs,
        "dynamic_range": dr,
        "frequency_spectrum": freq_balance.tolist(),
        "stereo_correlation": stereo_corr,
        "transient_density": np.std(np.diff(y)).tolist()
    }