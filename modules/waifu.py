import requests
import discord
from discord.ext import commands
from utils import fumo_mode

from bs4 import BeautifulSoup


class WaifuCommands(commands.Cog):
    @commands.command(name="waifu")
    async def waifu(self, ctx):
        response = requests.get("https://mywaifulist.moe/random")
        soup = BeautifulSoup(response.content, "html.parser")

        # Building the waifu
        waifu_name = soup.find("meta", property="og:title")
        waifu_short_desc = soup.find("meta", property="og:description")
        waifu_image = soup.find("meta", property="og:image")
        waifu_url = soup.find("meta", property="og:url")

        # Build the embed using the above waifu
        waifu_embed = discord.Embed(
            title=waifu_name["content"],
            description=waifu_short_desc["content"],
            url=waifu_url["content"],
            color=0xFFFFFF,
        )

        waifu_embed.set_image(url=waifu_image["content"])
        waifu_embed.set_footer(
            text="Data provided by MyWaifuList.moe",
            icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
        )

        # Debug logging, just in case
        print("Waifu generated!")
        print(waifu_name['content'] + '\n' + waifu_url['content'])
        print("=========================================================")

        # Send the waifu in the channel the command was executed in.
        await ctx.send(embed=waifu_embed)
