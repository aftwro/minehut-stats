import json
from datetime import datetime

from discord import Embed

from color import color


def commandEmbed(author, command: str) -> Embed:
    with open("../../assets/data/commands.json", 'r') as file:
        data = json.load(file)
    if command in data:
        data = data[command]
        embed = Embed(title=command.strip('_'), description=data['description'], color=color.info).set_footer(
            text="Requested by " + author)
        if data['aliases'] is not None:
            embed.add_field(name="Aliases", value=data['aliases'])
        if data['permissions'] is not None:
            embed.add_field(name="Permissions", value=data['permissions'])
    return embed or Embed(description="The command not found.", timestamp=datetime.now(), color=color.error).set_footer(
        text="Requested by " + author)
