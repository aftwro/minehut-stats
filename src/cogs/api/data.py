from discord.ext.commands import when_mentioned_or
from replit import db


def getPrefix(bot, message) -> str:
    return when_mentioned_or(db['prefixes'].get(str(message.guild.id), ';'))(bot, message)