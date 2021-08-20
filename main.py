import os
import logging
import discord
import random
import asyncio


from dotenv import load_dotenv
from dotenv.main import find_dotenv
from discord.ext import commands, tasks

from utils import error_handler
from modules import waifu, anilist, hentai_commands, neko_commands, system


client = commands.Bot(command_prefix="$")
client.remove_command("help")
load_dotenv(find_dotenv())


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


async def update_status():
    while True:
        print("[SYS] Setting status")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random_line('assets/anime.txt')))
        await asyncio.sleep(1440)


@client.event
async def on_ready():
    load_modules()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random_line('assets/anime.txt')))

    print("Bot is ready!\n")
    client.loop.create_task(update_status())


def load_modules():
    client.add_cog(error_handler.CommandErrorHandler(client))
    print("[SYS] Error handling loaded. (utils/error_handler.py)")

    client.add_cog(waifu.WaifuCommands(client))
    print("[MOD] Waifu module loaded. (modules/waifu.py)")

    client.add_cog(anilist.AnilistCommands(client))
    print("[MOD] Anilist module loaded. (modules/anilist.py)")

    client.add_cog(neko_commands.NekoCommands(client))
    print("[MOD] Nekos.life module loaded. (modules/neko_commands.py)")

    client.add_cog(system.SystemCommands(client))
    print("[MOD] System module loaded. (modules/system.py)")

    print("[SYS] Checking .env for NSFW...")
    if os.environ.get("NSFW") == "1":
        client.add_cog(hentai_commands.HentaiCommands(client))
        print("[MOD] Hentai module loaded. (modules/hentai.py)")
    else:
        print("[MOD] NSFW modules not loaded.")


if __name__ == "__main__":
    print("Mayuko is starting...")

    client.run(os.environ.get("TOKEN"))
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
