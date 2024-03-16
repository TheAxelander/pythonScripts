def get_env_file_content():
    env_file_path = '.env'
    env_dict = {}

    with open(env_file_path, 'r') as file:
        for line in file:
            # Ignore comments and empty lines
            if line.startswith('#') or not line.strip():
                continue
            # Strip leading and trailing whitespace, then split the line into key and value
            key, value = line.strip().split('=', 1)
            # Store the key-value pair in the dictionary
            env_dict[key] = value

    return env_dict
