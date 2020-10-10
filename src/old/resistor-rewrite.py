import os
from discord.ext import commands
from dotenv import load_dotenv

from main_cog import resistor_man

def main():
    load_dotenv()
    bot = resistor_man()

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[0:-3]}')

    bot.run(os.getenv('DISCORD_TOKEN'))

main()

    