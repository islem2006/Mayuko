import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error_embed = discord.Embed(
            title="Error",
            color=0xE94D4E
        )
        if isinstance(error, commands.ConversionError):
            return # Return because we don't want to send a message every single time
        if isinstance(error, commands.CommandNotFound):
            return # Return because we don't want to send a message every single time
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Detected a missing parameter.")
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
