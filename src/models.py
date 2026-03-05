from pydantic import BaseModel
from typing import List, Dict, Optional

class DAWInfo(BaseModel):
    name: str
    version: str
    project_format: str
    cli_available: bool

class PluginInfo(BaseModel):
    name: str
    path: str
    hash: str
    format: str
    category: str
    version: str


class AudioInterface(BaseModel):
    name: str
    host_api: str
    vendor_id: str
    max_input_channels: int
    max_output_channels: int


class MIDIController(BaseModel):
    name: str
    port_number: int


class SampleInfo(BaseModel):
    name: str
    path: str
    hash: str
    format: str
    size: int


class ModelFile(BaseModel):
    name: str
    path: str
    hash: str
    size: int


class AudioSystemProfile(BaseModel):
    daw_info: List[DAWInfo]
    plugin_catalog: List[PluginInfo]
    hardware_info: Dict[str, List]
    sample_catalog: List[SampleInfo]
    model_files: List[ModelFile]