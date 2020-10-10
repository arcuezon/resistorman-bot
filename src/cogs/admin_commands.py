from discord.ext import commands
import discord
import os

class admin_cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "msgc")
    @commands.check(commands.has_role("Admin"))
    async def message_channel(self, ctx, arg1, arg2):

        channel_id = await self.get_channel(self, arg1)
        channel = discord.utils.get(ctx.guild.channels, id=channel_id)

        await channel.send(arg2)

    @commands.command(name = "react")
    @commands.check(commands.has_role("Admin"))
    async def react_message(self, ctx, arg1, arg2, arg3):
        #arg1 = channel_id arg2 = msg_id arg3 = reaction

        channel_id = await self.get_channel(self, arg1)
        channel = discord.utils.get(ctx.guild.channels, id=channel_id)
        message = await channel.fetch_message(int(arg2))
        await message.add_reaction(arg3)

    async def get_channel(self, ctx, channel_id):
        channel = 0
        if channel_id in self.bot.text_channels:
            channel = self.bot.text_channels[channel_id]
        elif int(channel_id) in self.bot.text_channels.values():
            channel = int(channel_id)

        return channel





def setup(bot):
    bot.add_cog(admin_cmds(bot))

