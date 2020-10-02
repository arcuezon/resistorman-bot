import os

import discord
from dotenv import load_dotenv
import random
import re

#Text channel ids in the AECES Discord
text_channels = {
    "intros" : 760703291892957215,
    "welcome" : 760697489711693880,
    "announce" : 760702549643755530
}

#Set intents to enable greeting members on server join
intents = discord.Intents.default()
intents.members = True

def get_tokens(): #Get environment variables
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    return TOKEN

def run_bot(): #Run bot and verify if connected to AECES server
    client = discord.Client(intents = intents)
    TOKEN = get_tokens()
    GUILD = "AECES"

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=GUILD)

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    @client.event
    async def on_message(message): #Reply to messages
        if message.author == client.user:
            return
        
        user_message = re.findall(r'\w+', message.content.lower()) 
        if message.channel == client.get_channel(text_channels["intros"]): #Reply to intro channel
            greetings = ["hello", "hi"]

            for greeting in greetings:
                if greeting in user_message:
                    channel = client.get_channel(text_channels["intros"])
                    await channel.send(f"Hello, {message.author.mention}!")
                    return

        if "bong" in user_message:
            channel = message.channel
            await channel.send("Sir Bong ❤️")
            return

    @client.event
    async def on_member_join(member): #Welcome new members
        greetings = [
            "Hello {}! Welcome to the AECES Discord server!!",
            "Welcome to the AECES Discord server, {}!",
            "Hi there {}!! Welcome to the AECES Discord server!",
            "{} joined the party! Welcome to the AECES Discord server!"
        ]
        channel = client.get_channel(text_channels["welcome"])
        await channel.send(random.choice(greetings).format(member.mention))

    client.run(TOKEN)

run_bot()