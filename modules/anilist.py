import discord

from datetime import datetime
from AnilistPython import Anilist
from AnilistPython.botSupport import botSupportClass
from discord.ext import commands


anilist = Anilist()
anilist_bot = botSupportClass()


class AnilistCommands(commands.Cog):
    @commands.command(name="anisearch")
    async def anisearch(self, ctx, arg):
        result_anime = anilist_bot.getAnimeInfo(arg)
        anilist_id = anilist.extractID.anime(result_anime["name_english"])
        ani_id = anilist_id["data"]["Page"]["media"][0]["id"]

        short_desc = result_anime["desc"][0:200]
        final_desc = short_desc + "..."

        genres = str(result_anime["genres"])
        no_bracket_list = str(genres[1:-1])
        translation = {39: None, 91: None, 93: None}
        final_list = str(no_bracket_list.translate(translation))

        # UNCOMMENT THESE IF I NEED INFO BECAUSE DOCS ARE FOR CHUMPS
        # print(result_anime)
        # print("==================")
        # print(anilist_id)

        final_score = str(result_anime["average_score"]) + "/100"

        print("Anime result: " + result_anime["name_english"])
        print("https://anilist.co/anime/" + str(ani_id))
        print("=========================================================")

        anilist_embed = discord.Embed(
            title=result_anime["name_english"],
            description=final_desc,
            color=0x02A9FF,
            url="https://anilist.co/anime/" + str(ani_id))
        anilist_embed.set_thumbnail(
            url=result_anime["cover_image"]
        )
        anilist_embed.add_field(
            name="Romaji name",
            value=result_anime["name_romaji"],
            inline=False
        )
        anilist_embed.add_field(
            name="Genres",
            value=final_list,
            inline=False
        )
        anilist_embed.add_field(
            name="Status",
            value=result_anime["airing_status"],
            inline=False
        )
        anilist_embed.add_field(
            name="Episodes",
            value=result_anime["airing_episodes"],
            inline=False
        )
        if result_anime['next_airing_ep'] is not None:
            anilist_embed.add_field(
                name="Next episode",
                value=str(datetime.utcfromtimestamp(
                    result_anime['next_airing_ep']['airingAt']).strftime('%d/%m/%Y')),
                inline=False
            )
        anilist_embed.add_field(
            name="Average score",
            value=final_score,
            inline=False
        )
        anilist_embed.set_footer(
            text="Data provided by anilist.net",
            icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
        )
        await ctx.send(embed=anilist_embed)

    @ commands.command(name='charsearch')
    async def charsearch(self, ctx, arg):
        result_char = anilist_bot.getCharacterInfo(arg)
        anilist_id = anilist.extractID.character(result_char["first_name"])
        ani_id = anilist_id["data"]["Page"]["characters"][0]["id"]

        short_desc = result_char["desc"][0:200] + "..."

        last_name = str(result_char["last_name"])
        if last_name == "None":
            last_name = " "

        print("Character result: " +
              str(result_char["first_name"] + " " + last_name))
        print("https://anilist.co/character/" + str(ani_id))
        print("=========================================================")

        anilist_embed = discord.Embed(title=str(result_char["first_name"] + " " + last_name),
                                      description=short_desc,
                                      color=0x02A9FF,
                                      url="https://anilist.co/character/" + str(ani_id))
        anilist_embed.set_image(url=result_char["image"])
        anilist_embed.add_field(
            name="Native name", value=result_char["native_name"])
        anilist_embed.set_footer(
            text="Data provided by anilist.net",
            icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg"
        )
        await ctx.send(embed=anilist_embed)
