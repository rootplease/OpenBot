"""
Bot Class
"""
from twitchio.ext import commands
from config.config_manager import load_oauth_config, CredentialManager


class Bot(commands.Bot):
    """
    Initializes twitch bot object with available commands
    """

    def __init__(self):
        # Initialise our Bot with our access token
        credentials_object: CredentialManager = load_oauth_config()
        super().__init__(
            token=credentials_object.oauth_token,
            prefix="?",
            initial_channels=["rootplease"],
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
