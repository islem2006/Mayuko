import discord
from discord.ext import commands

from utils import fumo_mode


class SystemCommands(commands.Cog):
    @commands.command(pass_context=True)
    async def help(self, ctx, arg=None):
        help_embed = discord.Embed(
            title="Help",
            description="Learn commands and how to use them here!",
            color=0xFFF8A2,
        )
        if arg == "nsfw":
            help_embed.add_field(
                name="$sauce <code>",
                value="Display information and a thumbnail about the provided saucecode.",
                inline=False,
            )
            help_embed.add_field(
                name="$randsauce",
                value="Generate a random valid saucecode and display information about it.",
                inline=False,
            )
            help_embed.add_field(
                name="$nekohavatar",
                value="Sends a NSFW profile picture.",
                inline=False,
            )
            help_embed.add_field(
                name='$nekolewd',
                value="Sends a lewd neko picture.",
                inline=False,
            )
            help_embed.set_footer(
                text="Mayuko",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/pfp.jpg",
            )
            await ctx.send(embed=help_embed)
        else:
            help_embed.add_field(
                name="$waifu",
                value="Pull a random Waifu or Husbando from MyWaifuList.moe",
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
            help_embed.add_field(
                name='$nekoavatar',
                value="Sends a new profile picture.",
                inline=False,
            )
            help_embed.add_field(
                name="$changelog",
                value="View historical changes about Mayuko.",
                inline=False,
            )
            help_embed.add_field(
                name="$help nsfw",
                value="View NSFW commands.",
                inline=False,
            )
            help_embed.set_footer(
                text="Mayuko",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/pfp.jpg",
            )
            await ctx.send(embed=help_embed)


    @commands.command(pass_context=True)
    async def changelog(self, ctx):
        await ctx.send("Changelog is available at https://github.com/DynamicDonkey/Mayuko/blob/master/assets/CHANGELOG.md")
        await ctx.send("Happy hacking!")