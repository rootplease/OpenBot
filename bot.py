"""
Bot Class
"""
from twitchio.ext import commands
from config.config_manager import (
    load_oauth_config,
    load_bot_config,
    CredentialManager,
    BotSettings,
)


class Bot(commands.Bot):
    """
    Initializes twitch bot object with available commands
    """

    def __init__(self):
        # Initialise our Bot with our access token
        credentials_object: CredentialManager = load_oauth_config()
        bot_settings_object: BotSettings = load_bot_config()
        self.bot_name = bot_settings_object.bot_name
        self.bot_version = bot_settings_object.bot_version
        super().__init__(
            token=credentials_object.oauth_token,
            prefix=bot_settings_object.bot_command_prefix,
            initial_channels=[credentials_object.channel_name],
        )

    async def event_ready(self):
        """
        Logged in and ready
        """
        print(f"Logged in as | {self.nick}")

    @commands.command()
    async def hello(self, ctx: commands.Context):
        """
        Command to respond hi to user
        """
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command()
    async def version(self, ctx: commands.Context):
        """
        Command to respond hi to user
        """
        await ctx.send(f"{self.bot_name} {self.bot_version}!")
