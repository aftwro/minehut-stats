from discord import Embed
from discord.ext import commands
from discord.ext.commands import BucketType

from .api.commands import commandEmbed


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    @commands.cooldown(1, 1, BucketType.user)
    async def _help(self, ctx, query=None):
        if query is None:
            embed = Embed(title="Help").set_footer(
                text="Requested by " + ctx.author.name)
        else:
            await ctx.send(commandEmbed("_" + query))


def setup(client):
    client.add_cog(Core(client))
