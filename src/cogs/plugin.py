from datetime import datetime

import minehut
from discord import Embed
from discord.ext import commands
from discord.ext.commands import BucketType

from .api.color import color


class Plugin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='plugin')
    @commands.cooldown(1, 2, BucketType.user)
    async def _plugin(self, ctx, query: str):
        async with ctx.typing():
            try:
                plugin = minehut.getPlugin(query)
                embed = Embed(title=plugin.getName(), description=plugin.getLongDescription(), timestamp=datetime.now(),
                              color=color.minehut).set_footer(
                    text="Requested by " + ctx.author.name)
                embed.add_field(name="Name", value=plugin.getName())
                embed.add_field(name="ID", value=plugin.getId())
                embed.add_field(name="Version", value=plugin.getVersion())
                embed.add_field(name="Creation", value=plugin.getCreatedDatetime(), inline=False)
                embed.add_field(name="Last Updated", value=plugin.getLastUpdatedDatetime(), inline=False)
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(embed=Embed(description=e, timestamp=datetime.now(),
                                           color=color.error).set_footer(
                    text="Requested by " + ctx.author.name))


def setup(client):
    client.add_cog(Plugin(client))
