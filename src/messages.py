import time
from discord import Embed, Color


def game_on():
    current_time = time.strftime("%X")

    embed = Embed(
        title="Czarek znowu odpalil CSka",
        description="Pewnie i tak 16:0 dostanie",
        color=Color.blue(),
    )
    embed.set_thumbnail(url="https://cdn.frankerfacez.com/emoticon/113912/4")
    embed.add_field(name="Czas rozpoczecia", value=current_time)

    return embed


def game_off(started_at):
    current_time = time.strftime("%X")
    elapsed = time.strftime("%Hh %Mm %Ss", time.gmtime(time.time() - started_at))

    embed = Embed(
        title="Czarek skonczyl grac w CSka",
        description="Z rozwalonym biurkiem i nizsza ranga uda sie w objecia snu",
        color=Color.blue(),
    )
    embed.set_thumbnail(url="https://cdn.frankerfacez.com/emoticon/299177/4")
    embed.add_field(name="Czas zakonczenia", value=current_time)
    embed.add_field(name="Stracony czas", value=f"~ {elapsed}")

    return embed
