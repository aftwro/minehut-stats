from datetime import datetime

from discord import Embed
from discord.ext import commands

from .api.color import color
from .api.commands import commandEmbed


class ErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        if isinstance(error, commands.CommandOnCooldown):
            embed = Embed(
                description=f"This command is on cooldown for another **{round(ctx.command.get_cooldown_retry_after(ctx), 1)} seconds**.",
                color=color.error, timestamp=datetime.now()).set_footer(
                text="Requested by " + ctx.author.name)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions) or \
                isinstance(error, commands.MissingRequiredArgument) or \
                isinstance(error, commands.BadArgument):
            await ctx.send(embed=commandEmbed(ctx.command))


def setup(client):
    client.add_cog(ErrorHandler(client))
