import discord
from discord.ext import commands
from hentai import Hentai, Format, Utils
from utils import fumo_mode


class HentaiCommands(commands.Cog):
    @commands.command(name="sauce")
    @commands.is_nsfw()
    async def sauce(self, ctx, arg=0):
        if arg == 0:
            await ctx.send("Error: argument not provided.")
        if arg != 0:

            doujin = Hentai(arg)

            tag_list = [tag.name for tag in doujin.tag]
            no_bracket_list = str(tag_list[1:-1])
            translation = {39: None, 91: None, 93: None}
            final_list = str(no_bracket_list.translate(translation))

            print("Doujin generated.")
            print(doujin.title(Format.Pretty))
            print("https://nhentai.net/g/" + str(arg))
            print("=========================================================")

            hentai_embed = discord.Embed(
                title=doujin.title(Format.Pretty),
                description=str(arg),
                color=0xF15478,
                url="https://nhentai.net/g/" + str(arg)
            )
            hentai_embed.set_thumbnail(url=doujin.image_urls[0])
            hentai_embed.add_field(
                name="Tags",
                value=final_list,
                inline=False
            )
            hentai_embed.add_field(
                name="Pages", value=str(doujin.num_pages), inline=False
            )
            hentai_embed.add_field(
                name="Favorites", value=str(doujin.num_favorites), inline=False
            )
            if fumo_mode.friday_check():
                hentai_embed.set_footer(
                    text="Data provided by nhentai.net | Happy Fumo Friday!",
                    icon_url="https://media.spelunky.fyi/mods/logo/01ESRVJJKV6TRQKP8WAM27365T/1608225737342242.jpg",
                )
            else:
                hentai_embed.set_footer(
                    text="Data provided by nhentai.net",
                    icon_url="https://avatarfiles.alphacoders.com/577/57772.png",
                )
            await ctx.send(embed=hentai_embed)

    @commands.command(name="randsauce")
    @commands.is_nsfw()
    async def randsauce(self, ctx):
        await self.sauce(ctx, Utils.get_random_id())