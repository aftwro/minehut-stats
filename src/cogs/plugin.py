from datetime import datetime

import minehut
from discord import Embed
from discord.ext import commands
from discord.ext.commands import BucketType
from minehut import IllegalArgumentError

from .api.color import color


class Plugin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='plugin')
    @commands.cooldown(1, 2, BucketType.user)
    async def _plugin(self, ctx, query: str):
        try:
            try:
                plugin = minehut.getPlugin(query)
                embed = embed = Embed(title=plugin.getName(), timestamp=datetime.now(),
                                           color=color.minehut).set_footer(
                    text="Requested by " + ctx.author.name)
            except IllegalArgumentError:
                embed = Embed(description="Server was not found.", timestamp=datetime.now(),
                                           color=color.error).set_footer(
                    text="Requested by " + ctx.author.name)
            finally:
                await ctx.send(embed=embed)
        except Exception as e:
            print(e)


def setup(client):
    client.add_cog(Plugin(client))
