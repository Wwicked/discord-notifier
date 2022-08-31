import time
import config
import random
from discord import Embed, Color


def game_on():
    current_time = time.strftime("%X")

    title = random.choice(config.EMBEDS["on"]["titles"])
    desc = random.choice(config.EMBEDS["on"]["description"])
    img = random.choice(config.EMBEDS["on"]["images"])

    embed = Embed(title=title, description=desc, color=Color.blue(),)
    embed.set_thumbnail(url=img)
    embed.add_field(name="Czas rozpoczecia", value=current_time)

    return embed


def game_off(started_at):
    current_time = time.strftime("%X")
    elapsed = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - started_at))

    title = random.choice(config.EMBEDS["off"]["titles"])
    desc = random.choice(config.EMBEDS["off"]["description"])
    img = random.choice(config.EMBEDS["off"]["images"])

    embed = Embed(title=title, description=desc, color=Color.blue(),)
    embed.set_thumbnail(url=img)
    embed.add_field(name="Czas zakonczenia", value=current_time)
    embed.add_field(name="Stracony czas", value=f"~ {elapsed}")

    return embed
