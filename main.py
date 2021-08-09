import os
import discord

from commands import waifu, anilist, hentai_commands, system

from dotenv import load_dotenv
from dotenv.main import find_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix='$')
client.remove_command('help')


if __name__ == '__main__':
    print("Saucebot V2 starting...")


@client.event
async def on_ready():
    print("Saucebot V2 is ready!\n")
    await client.change_presence(activity=discord.Game('$help for info :3'))
    client.add_cog(waifu.WaifuCommands(client))
    client.add_cog(anilist.AnilistCommands(client))
    client.add_cog(hentai_commands.HentaiCommands(client))
    client.add_cog(system.SystemCommands(client))
    pass


load_dotenv(find_dotenv())
client.run(os.environ.get("TOKEN"))
