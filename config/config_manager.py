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

    yaml_tag = "!twitch"

    def __init__(self, bot_username: str, channel_name: str, oauth_token: str):
        self.bot_username = bot_username
        self.channel_name = channel_name
        self.oauth_token = oauth_token


class BotSettings(yaml.YAMLObject):
    """
    Manages the bot settings from config file
    bot_name: string
    bot_command_prefix: string
    bot_version: string
    """

    yaml_tag = "!bot"

    def __init__(self, bot_name: str, bot_command_prefix: str, bot_version: str):
        self.bot_name = bot_name
        self.bot_command_prefix = bot_command_prefix
        self.bot_version = bot_version


def load_oauth_config() -> CredentialManager:
    """
    Function to load oauth configuration information from config.yaml
    """
    credentials_object = CredentialManager
    with open(r"config/config.yaml", encoding="utf-8") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        # credentials__yaml_object = yaml.load(file, Loader=yaml.FullLoader)
        yaml.add_path_resolver("!twitch", ["twitch"], dict)
        credentials_object = yaml.load(file, Loader=yaml.FullLoader)

    return credentials_object["twitch"]


def load_bot_config() -> BotSettings:
    """
    Function to load bot configuration information from config.yaml
    """
    bot_config_object = BotSettings
    with open(r"config/config.yaml", encoding="utf-8") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        # credentials__yaml_object = yaml.load(file, Loader=yaml.FullLoader)
        yaml.add_path_resolver("!bot", ["bot"], dict)
        bot_config_object = yaml.load(file, Loader=yaml.FullLoader)

    return bot_config_object["bot"]
