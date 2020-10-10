from discord.ext import commands
import re
import random


class welcome_greetings(commands.Cog):

    greetings = [
        "Hello {}! Welcome to the AECES Discord server!!",
        "Welcome to the AECES Discord server, {}!",
        "Hi there {}!! Welcome to the AECES Discord server!",
        "{} joined the party! Welcome to the AECES Discord server!"
    ]

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        channel = self.bot.get_channel(self.bot.text_channels["welcome"])
        await channel.send(random.choice(self.greetings).format(member.mention))


def setup(bot):
    bot.add_cog(welcome_greetings(bot))
