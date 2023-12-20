import json


def read_config_file(config_file_path):
    """
    Reads a JSON configuration file and returns its contents as a Python object.

    Args:
        config_file_path (str): Path to the configuration file.

    Returns:
        dict: The contents of the configuration file as a Python object.

    Raises:
        FileNotFoundError: If the configuration file cannot be found.
        ValueError: If the configuration file cannot be parsed as JSON.
    """
    with open(config_file_path, 'r') as f:
        data = f.read()
        return json.loads(data)
