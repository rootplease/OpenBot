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


def load_oauth_config(yaml_object) -> CredentialManager:
    """
    Function to load oauth configuration information from config.yaml
    """
    yaml.add_path_resolver("!oauth", ["OAUTH"], dict)
    data = yaml.load(yaml_object, Loader=yaml.FullLoader)
    return data["OAUTH"]
