import sys
import os
from pathlib import Path


def find_config_path():
    """
    This function is used to find the path of the configuration file.

    Args:
        None

    Returns:
        The path of the configuration file as a Path object

    Raises:
        SystemExit: If the number of arguments is not correct or the configuration file does not exist
    """
    if (args_count := len(sys.argv)) > 2:
        print(f"One argument expected, got {args_count - 1}")
        raise SystemExit(2)
    elif args_count < 2:
        print("You must specify the configuration file path")
        raise SystemExit(2)

    config_file_path = Path(sys.argv[1])

    print(f"Looking for config file at: {config_file_path}")

    if not config_file_path.is_file():
        print(f"The configuration file doesn't exist {config_file_path}")
        raise SystemExit(1)

    return config_file_path
