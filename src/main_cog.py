import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

class resistor_man(commands.Bot):

    text_channels = {
    "intros" : 760703291892957215,
    "welcome" : 760697489711693880,
    "announce" : 760702549643755530,
    "rules" : 760698388001325067,
    "roles" : 760698326386999296,
    "resistor" : 763422998442016789,
    "jobs" : 761064541051944990,
    "acads" : 760702201630556160
    }

    resistorman_id = 760711591355744307

    cogpath = os.path.join(os.path.dirname(__file__), "./cogs")

    def __init__(self, command_prefix = '!'):
        #Set Discord intents
        intents = discord.Intents.default()
        intents.members = True
        intents.reactions = True

        commands.Bot.__init__(self, command_prefix = command_prefix, intents = intents)
        self.message1 = f"[INFO] Resistor Man is now online."
        self.message2 = "Resistor man is online!"

        
    
    async def on_ready(self):
        guild = discord.utils.get(self.guilds, name = "AECES")
        print(self.message1)
        print(f"Connected to {guild.name} with ID: {guild.id}")
    
    
def main():
    load_dotenv()
    bot = resistor_man()

    for filename in os.listdir(bot.cogpath):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[0:-3]}')

    bot.run(os.getenv('DISCORD_TOKEN'))

main()