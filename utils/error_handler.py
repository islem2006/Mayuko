from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send(f"{ctx.command} is disabled in non-NSFW channels.")
