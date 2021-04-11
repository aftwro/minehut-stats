from datetime import datetime

import minehut
from discord import Embed
from discord.ext import commands

from .api.color import color

class Network(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='network')
    async def _network(self, ctx):
        try:
            async with ctx.typing():
                embed = Embed(title='Network', timestamp=datetime.now(), color=color.minehut).set_footer(
                    text="Requested by " + ctx.author.name)
                embed.add_field(name='Players Online', value=f"{minehut.getPlayerCount():,d}")
                embed.add_field(name='Severs Online', value=f"{minehut.getServerCount():,d}")
                embed.add_field(name='Server Max', value=f"{minehut.getServerCap():,d}")
                embed.add_field(name='Top Servers', value="".join(
                    [f"{index}. {server.getName()} ({server.getPlayerCount():,d} players)\n" for index, server in
                     enumerate(minehut.getTop5(), start=1)]), inline=False)
                await ctx.send(embed=embed)
        except Exception as e:
            print(e)


def setup(client):
    client.add_cog(Network(client))
