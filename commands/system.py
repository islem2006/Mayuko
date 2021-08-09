import discord
from discord.ext import commands


class SystemCommands(commands.Cog):
    @commands.command(pass_context=True)
    async def help(self, ctx):
        help_embed = discord.Embed(title="Help", description="Learn commands how to use them here!", color=0xFFF8A2)
        help_embed.add_field(name="$waifu", value="Pull a random Waifu or Husbando from MyWaifuList.moe", inline=False)
        help_embed.add_field(name="$anisearch <\"Anime name\">", value="Search for an anime by name on Anilist.co", inline=False)
        help_embed.add_field(name="$charsearch <\"Character name\">",  value="Search for a character by name on Anilist.co", inline=False)
        help_embed.add_field(name="$sauce <code>", value="Display information and a thumbnail about the provided saucecode.", inline=False)
        help_embed.add_field(name="$randsauce", value="Generate a random valid saucecode and display information about it.", inline=False)
        help_embed.set_footer(text="Saucebot v2.0", icon_url="https://avatarfiles.alphacoders.com/577/57772.png")
        await ctx.send(embed=help_embed)
