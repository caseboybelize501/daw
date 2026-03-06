import sounddevice
import rtmidi
from typing import List, Dict

async def scan_audio_hardware() -> Dict:
    # Query audio devices
    devices = sounddevice.query_devices()
    
    audio_interfaces = []
    midi_controllers = []
    
    # Identify audio interfaces by vendor IDs (simplified)
    for device in devices:
        if device["max_input_channels"] > 0 or device["max_output_channels"] > 0:
            # Simplified vendor ID detection
            vendor_id = "unknown"
            if "Focusrite" in device["name"]:
                vendor_id = "0x1235"
            elif "Universal Audio" in device["name"]:
                vendor_id = "0x0D8C"
            elif "MOTU" in device["name"]:
                vendor_id = "0x07FD"
            
            audio_interfaces.append({
                "name": device["name"],
                "host_api": device["hostapi"],
                "vendor_id": vendor_id,
                "max_input_channels": device["max_input_channels"],
                "max_output_channels": device["max_output_channels"]
            })
    
    # MIDI controllers
    midi_controllers = []
    try:
        midi_in = rtmidi.MidiIn()
        port_count = midi_in.get_port_count()
        for i in range(port_count):
            try:
                port_name = midi_in.get_port_name(i)
                if port_name:
                    midi_controllers.append({
                        "name": port_name,
                        "port_number": i
                    })
            except Exception as e:
                print(f"Error reading MIDI port {i}: {e}")
        midi_in.close_port()
    except Exception as e:
        print(f"MIDI scan error (non-critical): {e}")
    
    return {
        "audio_interfaces": audio_interfaces,
        "midi_controllers": midi_controllers,
        "sample_rate_supported": [44100, 48000, 96000],
        "bit_depth_supported": [24, 32]
    }