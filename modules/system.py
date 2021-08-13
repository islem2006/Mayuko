import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from dotenv.main import find_dotenv
from utils import fumo_mode

load_dotenv(find_dotenv())


class SystemCommands(commands.Cog):
    @commands.command(pass_context=True)
    async def help(self, ctx):
        help_embed = discord.Embed(
            title="Help",
            description="Learn modules how to use them here!",
            color=0xFFF8A2,
        )
        help_embed.add_field(
            name="$waifu",
            value="Pull a random Waifu or Husbando from MyWaifuList.moe",
            inline=False,
        )
        help_embed.add_field(
            name="$changelog",
            value="View historical changes about Saucebot.",
            inline=False,
        )
        help_embed.add_field(
            name='$anisearch <"Anime name">',
            value="Search for an anime by name on Anilist.co",
            inline=False,
        )
        help_embed.add_field(
            name='$charsearch <"Character name">',
            value="Search for a character by name on Anilist.co",
            inline=False,
        )
        if os.environ.get("NSFW") == "1":
            help_embed.add_field(
                name="$sauce <code> - NSFW COMMAND",
                value="Display information and a thumbnail about the provided saucecode.",
                inline=False,
            )
            help_embed.add_field(
                name="$randsauce - NSFW COMMAND",
                value="Generate a random valid saucecode and display information about it.",
                inline=False,
            )
        if fumo_mode.friday_check():
            help_embed.set_footer(
                text="Saucebot v2.0 | Happy Fumo Friday!",
                icon_url="https://media.spelunky.fyi/mods/logo/01ESRVJJKV6TRQKP8WAM27365T/1608225737342242.jpg",
            )
        else:
            help_embed.set_footer(
                text="Saucebot v2.0",
                icon_url="https://avatarfiles.alphacoders.com/577/57772.png",
            )
        await ctx.send(embed=help_embed)

    @commands.command(pass_context=True)
    async def changelog(self, ctx):
        await ctx.send("Changelog is available at https://github.com/DynamicDonkey/Saucebot-V2/CHANGELOG.md")
        await ctx.send("Happy hacking!")
