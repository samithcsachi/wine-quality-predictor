from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Data Ingestion Configuration"""
    root_dir: Path
    source_URL: str 
    local_data_file: Path