from discord.ext import commands


class Plugin(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Plugin(client))
