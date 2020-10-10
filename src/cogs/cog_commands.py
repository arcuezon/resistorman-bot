from discord.ext import commands

class cog_commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = "load_cog")
    @commands.check(commands.has_role("Admin"))
    async def load_cog(self, ctx, arg1):
        self.bot.load_extension(f"cogs.{arg1}")
        await ctx.send(f"Loaded {arg1}.")

    @commands.command(name = "unload_cog")
    @commands.check(commands.has_role("Admin"))
    async def unload_cog(self, ctx, arg1):
        self.bot.unload_extension(f"cogs.{arg1}")
        await ctx.send(f"Unloaded {arg1}.")

    @commands.command(name = "reload_cog")
    @commands.check(commands.has_role("Admin"))
    async def reload_cog(self, ctx, arg1):
        self.bot.unload_extension(f"cogs.{arg1}")
        self.bot.load_extension(f"cogs.{arg1}")
        await ctx.send(f"Reloaded {arg1}.")

def setup(bot):
    bot.add_cog(cog_commands(bot))