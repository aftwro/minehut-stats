from datetime import datetime

import minehut
from discord import Embed
from discord.ext import commands
from discord.ext.commands import BucketType

from .api.color import color
from .api.time import formatTime

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='server')
    @commands.cooldown(1, 2, BucketType.user)
    async def _server(self, ctx, query):
        async with ctx.typing():
            try:
                server = minehut.getServer(query)
                created = await formatTime(server.getCreationDatetime())
                lastonline = await formatTime(server.getLastOnlineDatetime())
                embed = Embed(title=server.getName(), timestamp=datetime.now(),
                              color=color.minehut).set_footer(
                    text="Requested by " + ctx.author.name)
                embed.add_field(name="ID", value=server.getId())
                embed.add_field(name="Online?", value=str(server.isOnline()))
                embed.add_field(name="Visible?", value=str(server.isVisible()))
                embed.add_field(name="Player Count", value=server.getPlayerCount())
                embed.add_field(name="Max Players", value=server.getMaxPlayers())
                embed.add_field(name="Plan", value=server.getServerPlan())
                embed.add_field(name="Credits Per Day", value=server.getCreditsPerDay())
                embed.add_field(name="Icon", value=server.getIcon())
                embed.add_field(name="Platform", value=server.getPlatform())
                embed.add_field(name="Created", value=created)
                embed.add_field(name="Last Online", value=lastonline)
                embed.add_field(name="MOTD", value=server.getMOTD(), inline=False)
                embed.add_field(name="Plugins", value="".join([f"\t- {plugin.getName()}\n" for plugin in server.getPlugins()]))
                print(server.getServerProperties())
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(embed=Embed(description=e, timestamp=datetime.now(),
                                           color=color.error).set_footer(
                    text="Requested by " + ctx.author.name))


def setup(client):
    client.add_cog(Server(client))
