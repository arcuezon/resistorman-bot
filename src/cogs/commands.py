from discord.ext import commands
import discord

class bot_commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "status")
    async def check_status(self, ctx):
        await ctx.send(self.bot.message2)

def setup(bot):
    bot.add_cog(bot_commands(bot))