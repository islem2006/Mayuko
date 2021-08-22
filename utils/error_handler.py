import traceback
import discord
import sys
from discord.ext import commands


class NonDiscordErrors():
    async def AnimeNotFoundError(self, ctx, error):
        error_embed = discord.Embed(
            title="Error",
            color=0xE94D4E
        )
        await ctx.send(embed=error_embed)


class CommandErrorHandler(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error_embed = discord.Embed(
            title="Error",
            color=0xE94D4E
        )
        if hasattr(ctx.command, 'on_error'):
            return
        if isinstance(error, commands.MissingRequiredArgument):
            error_embed.add_field(
                name="Syntax error",
                value=f"{ctx.command} is missing a required argument."
            )
            error_embed.set_thumbnail(
                url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/syntaxt_error.png"
            )
            error_embed.set_footer(
                text="Mayuko",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
            )
            await ctx.send(embed=error_embed)
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("Detected a missing permission.")
        if isinstance(error, commands.NSFWChannelRequired):
            error_embed.add_field(
                name="NSFW content",
                value=f"{ctx.command} is disabled in non-NSFW channels."
            )
            error_embed.set_thumbnail(
                url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/nsfw_error.png"
            )
            error_embed.set_footer(
                text="Mayuko",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
            )
            await ctx.send(embed=error_embed)
        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(
                ctx.command), file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)
