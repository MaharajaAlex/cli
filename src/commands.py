import os
import shutil
import subprocess
from typing import Union, List
from gui import *


def list_directory(path: Union[str, bytes]) -> List[str]:
    """List contents of a directory.
    
    Parameters:
    path (str | bytes): The path to list the directory of.
    
    Raises:
    FileNotFoundError: If the specified path does not exist.
    PermissionError: If the permission to change the directory is denied.
    
    Returns:
    List[str]: List of directory contents.
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


def shutdown() -> None:
    """
    Shutdown the system.
    
    Parameters:
    None 

    Raises:
    OSError: For other OS-related errors.
    """
    try:
        os.system("shutdown /s /t 1")
    except OSError as e:
        print(f"Error: {e}")


def signout() -> None:
    """
    Signout the user.
    
    Parameters:
    None 

    Raises:
    OSError: For other OS-related errors.
    """
    try:
        os.system("shutdown /l")
    except OSError as e:
        print(f"Error: {e}")


def mkdir(path: Union[str, bytes]) -> None:
    """
    Make a new directory.
    
    Parameters:
    path (str | bytes): The path of the directory to be made.

    Raises:
    OSError: For other OS-related errors.
    """
    try:
        os.mkdir(path, mode=0o777)
    except OSError as e:
        print(f"Error: {e}")


def rmdir(path: Union[str, bytes]) -> None:
    """
    Remove a directory.
    
    Parameters:
    path (str | bytes): The path of the directory to be removed.

    Raises:
    OSError: For other OS-related errors.
    """
    try:
        os.rmdir(path)
    except OSError as e:
        print(f"Error: {e}")


def echo(text: Union[str, bytes]) -> None:
    """
    Display user input text.
    
    Parameters:
    text (str | bytes): The text to be displayed.

    Raises:
    OSError: For other OS-related errors.
    """
    try:
        print(text)
    except OSError as e:
        print(f"Error: {e}")


def cls() -> None:
    """
    Clear the screen.
    
    Parameters:
    None

    Raises:
    OSError: For other OS-related errors.
    """
    try:
        print("Cleared")
    except OSError as e:
        print(f"Error: {e}")


def ipconfig() -> List[str]:
    """
    Get the IP configuration details.

    Parameters:
    None
    
    Returns:
    List[str]: The IP configuration details.

    Raises:
    PermissionError: If the permission to access the details is denied.
    OSError: For other OS-related errors.
    """
    try:
        data = subprocess.check_output(['ipconfig', '/all']).decode('utf-8').split('\n')
        output = []
        for item in data:
            output.extend(item.split('\r')[:-1])
        return output
    except PermissionError:
        print("Permission Denied")
    except OSError as e:
        print(f"Error: {e}")


def ping_func(host: str) -> Union[str, Exception]:
    """
    Ping a host.

    Parameters:
    host (str): The host to be pinged.

    Returns:
    Union[str, Exception]: The result of the ping or an exception if it fails.
    """
    try:
        ping_res = ping(host, verbose=True)
        return ping_res
    except Exception as e:
        return e
