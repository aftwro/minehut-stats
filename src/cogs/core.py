from datetime import datetime

from discord import Embed
from discord.ext import commands
from discord.ext.commands import BucketType

from .api.color import color
from .api.commands import commandEmbed


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.BOT_COMMANDS = ['help', 'source', 'invite']
        self.MINEHUT_COMMANDS = ['server', 'plugin', 'network']

    @commands.command(name='help')
    @commands.cooldown(1, 1, BucketType.user)
    async def _help(self, ctx, query=None):
        if query is None:
            embed = Embed(title="Minehut Stats Bot",
                          description="An open source discord.py bot for minehut stats using the minehut-api python library.",
                          timestamp=datetime.now(), color=color.info).set_footer(
                text="Requested by " + ctx.author.name)
            embed.add_field(name="Bot", value="".join([f"- `{command}`\n" for command in self.BOT_COMMANDS]),
                            inline=False)
            embed.add_field(name="Minehut", value="".join([f"- `{command}`\n" for command in self.MINEHUT_COMMANDS]),
                            inline=False)
        else:
            embed = commandEmbed("_" + query)
        await ctx.send(embed=embed)

    @commands.command(name='source', aliases=['contribute'])
    @commands.cooldown(1, 1, BucketType.user)
    async def _source(self, ctx):
        embed = Embed(
            description="You can view my source [here](https://github.com/SuperOrca/Minehut-Stats).",
            timestamp=datetime.now(), color=color.info).set_footer(
            text="Requested by " + ctx.author.name)
        await ctx.send(embed=embed)

    @commands.command(name='invite')
    @commands.cooldown(1, 1, BucketType.user)
    async def _invite(self, ctx):
        embed = Embed(
            description="You can invite me [here](https://discord.com/api/oauth2/authorize?client_id=830206810644021309&permissions=8&scope=bot).",
            timestamp=datetime.now(), color=color.info).set_footer(
            text="Requested by " + ctx.author.name)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Core(client))
