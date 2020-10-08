import os
from discord.ext import commands
from dotenv import load_dotenv

from main_cog import resistor_man

def main():
    load_dotenv()
    bot = resistor_man()

    cogs = ["greetings", "roles_assignment", "chat_responses"]
    for cog in cogs:
        bot.load_extension(cog)

    bot.run(os.getenv('DISCORD_TOKEN'))

main()

    