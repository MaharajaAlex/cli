import os
import shutil
from typing import Union

def list_directory(path: Union[str, bytes]) -> list[str]:
    """List contents of a directory.
    
    Parameters:
    path (str | bytes): The path to list the directory of.
    
    Raises:
    FileNotFoundError: If the specified path does not exist.
    PermissionError: If the permission to change the directory is denied.
    """
    try:
        return os.listdir(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory '{path}' not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied: '{path}'")
    except Exception as e:
        raise RuntimeError(f"Failed to list directory '{path}': {e}")

def cd(path: Union[str, bytes]) -> None:
    """
    Change the current working directory to the given path.
    
    Parameters:
    path (str | bytes): The path to change the current working directory to.
                        It can be an absolute path or a relative path.
    
    Raises:
    FileNotFoundError: If the specified path does not exist.
    NotADirectoryError: If the specified path is not a directory.
    PermissionError: If the permission to change the directory is denied.
    OSError: For other OS-related errors.
    """
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Error: The specified path '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: The specified path '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to change directory to '{path}'.")
    except OSError as e:
        print(f"Error: {e}")
