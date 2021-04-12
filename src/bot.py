import os
from datetime import datetime

import discord
from discord.ext import commands
from replit import db

from cogs.api.data import getPrefix
from revive import revive

"""
Create Bot

Get prefix from replit db (Defaults to ;).
Commands are case insensitive.
Set uptime attribute for uptime command.
Remove default help command.
"""
bot = commands.AutoShardedBot(command_prefix=getPrefix, case_insensitive=True)
bot.uptime = datetime.utcnow()
bot.remove_command('help')

EXTENSIONS = [
    'cogs.core',
    'cogs.error',
    'cogs.network',
    'cogs.plugin',
    'cogs.server'
]


@bot.event
async def on_ready():
    db['prefixes'] = {} if 'prefixes' not in db else db['prefixes']
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('mh!help'))
    bot.load_extension("jishaku")
    for extension in EXTENSIONS:
        bot.load_extension(extension)
        print(f"\t- '{extension}' loaded.")
    print("Bot is ready.")


revive()
bot.run(os.getenv('TOKEN'))
