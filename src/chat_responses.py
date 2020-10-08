from discord.ext import commands
import re

class chat_responses(commands.Cog):

    responses = {
        "bong" : "Sir Bong ❤️",
        "ohms" : "V = IR",
        "ohm" : "V = IR",
        "papasa" : "Syempre papasa!",
        "shift" : "ECCE :heart:",
        "inom" : "Tara Pop Up!!"
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        user_message = re.findall(r'\w+', message.content.lower()) 
        if message.channel == self.bot.get_channel(self.bot.text_channels["intros"]): #Reply to intro channel
            greetings = ["hello", "hi"]

            for greeting in greetings:
                if greeting in user_message:
                    channel = self.bot.get_channel(self.bot.text_channels["intros"])
                    await channel.send(f"Hello, {message.author.mention}!")
                    return

        for prompt in self.responses:
            if prompt in user_message:
                channel = message.channel
                await channel.send(self.responses[prompt])

def setup(bot):
    bot.add_cog(chat_responses(bot))