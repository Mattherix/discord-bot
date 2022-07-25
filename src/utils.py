from nextcord import slash_command
from nextcord.ext import commands


class Utils(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @slash_command(description="Return the sum of 2 numbers")
    async def add(self, ctx, left: int, right: int):
        await ctx.send(left + right)
