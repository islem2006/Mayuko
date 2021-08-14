import os
import logging
import discord

from dotenv import load_dotenv
from dotenv.main import find_dotenv
from discord.ext import commands

from utils import error_handler
from modules import waifu, anilist, hentai_commands, neko_commands, system


client = commands.Bot(command_prefix="$")
client.remove_command("help")
load_dotenv(find_dotenv())


if __name__ == "__main__":
    print("Mayuko is starting...")
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)



@client.event
async def on_ready():
    load_modules()
    await client.change_presence(activity=discord.Game("$help >///<"))
    print("Bot is ready!\n")


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


client.run(os.environ.get("TOKEN"))
