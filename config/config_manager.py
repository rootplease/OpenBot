"""
centralized configuration manager module
"""
import yaml


class CredentialManager(yaml.YAMLObject):
    """
    Manages the crendentials from config file
    bot_username: string
    channel_name: string
    oauth_token:  string
    """

    yaml_tag = "!oauth"

    def __init__(self, bot_username: str, channel_name: str, oauth_token: str):
        self.bot_username = bot_username
        self.channel_name = channel_name
        self.oauth_token = oauth_token


def load_oauth_config() -> CredentialManager:
    """
    Function to load oauth configuration information from config.yaml
    """
    credentials_object = CredentialManager
    with open(r"config/config.yaml", encoding="utf-8") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        # credentials__yaml_object = yaml.load(file, Loader=yaml.FullLoader)
        yaml.add_path_resolver("!oauth", ["oauth"], dict)
        credentials_object = yaml.load(file, Loader=yaml.FullLoader)

    return credentials_object["oauth"]
