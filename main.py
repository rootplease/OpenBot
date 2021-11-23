#!/usr/bin/python3
"""
OpenBot v0.1 Author RootPlease
https://github.com/rootplease/OpenBot
"""

from config_manager import load_oauth_config, CredentialManager


def main():
    """Main Entrypoint"""

    credentials_object = CredentialManager
    with open(r"config/config.yaml", encoding="utf-8") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        # credentials__yaml_object = yaml.load(file, Loader=yaml.FullLoader)
        credentials_object = load_oauth_config(file)

    print(credentials_object)


if __name__ == "__main__":
    main()
