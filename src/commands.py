import os
import shutil

def list_directory(path: str) -> list[str]:
    """List contents of a directory."""
    try:
        return os.listdir(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory '{path}' not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied: '{path}'")
    except Exception as e:
        raise RuntimeError(f"Failed to list directory '{path}': {e}")
