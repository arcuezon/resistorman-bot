from discord.ext import commands
import os

class admin_cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "restart")
    @commands.check(commands.has_role("Admin"))
    async def restart_bot(self, ctx):

        await ctx.message.channel.send("Restarting...")
        await self.bot.logout()

def setup(bot):
    bot.add_cog(admin_cmds(bot))

