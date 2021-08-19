import os
import discord
import nekos

from dotenv import load_dotenv
from dotenv.main import find_dotenv
from discord.ext import commands
from utils import fumo_mode

load_dotenv(find_dotenv())


class NekoCommands(commands.Cog):
    @commands.command(name="nekoavatar")
    async def avatar(self, ctx):
        neko_avatar = nekos.img('avatar')
        neko_embed = discord.Embed(
            title="Have a new profile picture, on the house!",
            url=neko_avatar,
            color=0x512DA8
        )
        neko_embed.set_image(url=neko_avatar)
        neko_embed.set_footer(
            text="Data provided by nekos.life",
            icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
        )
        await ctx.send(embed=neko_embed)

    if os.environ.get("NSFW") == "1":
        @commands.command(name="nekohavatar")
        @commands.is_nsfw()
        async def havatar(self, ctx):
            neko_avatar = nekos.img('nsfw_avatar')
            neko_embed = discord.Embed(
                title="Have a new profile picture, on the house!",
                url=neko_avatar,
                color=0x512DA8
            )
            neko_embed.set_image(url=neko_avatar)
            neko_embed.set_footer(
                text="Data provided by nekos.life",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
            )
            await ctx.send(embed=neko_embed)

        @commands.command(name="nekolewd")
        @commands.is_nsfw()
        async def nekolewd(self, ctx):
            neko_avatar = nekos.img('lewd')
            neko_embed = discord.Embed(
                title="Lewd nekos, on the way!",
                url=neko_avatar,
                color=0x512DA8
            )
            neko_embed.set_image(url=neko_avatar)
            neko_embed.set_footer(
                text="Data provided by nekos.life",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
            )
            await ctx.send(embed=neko_embed)
