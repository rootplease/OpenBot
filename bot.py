"""
Bot Class
"""
import datetime
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

    @commands.command()
    async def uptime(self, ctx: commands.Context):
        """
        Command to print stream uptime
        """
        stream_info = await self.fetch_streams(None, None, ["accountsbroke"])
        stream_time = stream_info[0].started_at
        start_time = stream_time.replace(tzinfo=None)
        current_time = datetime.datetime.now()
        time_difference = (current_time - start_time).seconds
        days = divmod(time_difference, 86400)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)
        time_string = f"""
            {days[0]} days, 
            {hours[0]} hours, 
            {minutes[0]} minutes, 
            {minutes[1]} seconds
        """
        await ctx.send(f"Uptime: {time_string}!")
