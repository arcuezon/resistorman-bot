import os

import discord
import random
import re

#To-Do
# 1. Bot commands (?)

#Text channel ids in the AECES Discord
text_channels = {
    "intros" : 760703291892957215,
    "welcome" : 760697489711693880,
    "announce" : 760702549643755530,
    "rules" : 760698388001325067,
    "roles" : 760698326386999296
}

#Mappings for roles
mapping = {
    763466119990083595:{
        "🌱" : 763462230540812298,
        "🍦" : 763462194473074718,
        "🥲" : 763462159534653451,
        "🧟‍♂️" : 763462130317131846,
        "👨‍🎓" : 763461855578161192,
        "👴" : 763462275277127682
    },
    763598798776827904:{
        '⚽': 763595482429653043, 
        '🎮': 763595543602921512, 
        '📱': 763595591531102218,
        '🔨' : 763598078258315275
    }
}

#Batch roles message
batch_roles_id = 763466119990083595

#Set Discord intents
intents = discord.Intents.default()
intents.members = True
intents.reactions = True

#Get environment variables
def get_tokens():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    return TOKEN

#Run bot and verify if connected to AECES server
def run_bot():
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

        channel = client.get_channel(text_channels["roles"])
        #RULES Message
        #groovy = client.get_user(234395307759108106)
        # await channel.send(f"**1. First of all, kindly change your nickname!**\n To do this right click on your profile at the right side and click on 'Change Nickname' OR click the arrow beside the server name on the top left of your screen and click on 'Change Nickname'. Follow the format [Nickname || Yr. and Course]\n\n **2. This is a safe space. Be nice and respectful.**\n Discrimination, racism, homophobia, or any other derogatory behavior will not be tolerated on this server.\n\n **3. There are different topics for each respective channel. Please post content in the correct channels.**\n {groovy.mention} is bound to #📻music , use that channel for any music requests\n\n **4. Avoid spamming the chatrooms, leave announcements and recruitments in their respective channels. Do not ping other roles for unnecessary reasons.**\n\n **5. Don't forget to constantly check out the announcements tab for upcoming AECES events or changes in the server.**")
        
        #ROLES Message
        # message = await channel.send("Please react to this message with the following according to your batch\n🌱 : Batch 2025\n🍦 : Batch 2024\n🥲 : Batch 2023\n🧟‍♂️ : Batch 2022\n👨‍🎓 : Batch 2021\n👴 : Alumni")
        # for emoji in mapping:
        #     await message.add_reaction(emoji)
        
        #INTEREST ROLES Message
        # content = "Please react to this message with your interests to be able to access the relevant channels!\n⚽ : Sports\n🎮 : Video Games\n📱 : Technology\n🔨 : Opportunities"
        # message = await send_message(channel, content)
        # emojis = ['⚽', '🎮', '📱', '🔨']
        # for emoji in emojis:
        #     await message.add_reaction(emoji)

    #Message utility function
    async def send_message(channel, content):
        message = await channel.send(content)
        return message

    #Reply to messages
    @client.event
    async def on_message(message): 
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
            #mika = client.get_user(751054032679993435)
            #await channel.send(f"{mika.mention} pls help {message.author.mention}")

        if "ohms" in user_message or "ohm" in user_message:
            channel = message.channel
            await channel.send("V = IR")

        if "papasa" in user_message:
            channel = message.channel
            await channel.send("Syempre papasa!!")
            return

        if "shift" in user_message:
            channel = message.channel
            await channel.send("ECCE :heart:")
            return
        
        if "inom" in user_message:
            channel = message.channel
            await channel.send("Tara Pop up!")
            return

    #Welcome new members
    @client.event
    async def on_member_join(member):
        greetings = [
            "Hello {}! Welcome to the AECES Discord server!!",
            "Welcome to the AECES Discord server, {}!",
            "Hi there {}!! Welcome to the AECES Discord server!",
            "{} joined the party! Welcome to the AECES Discord server!"
        ]
        channel = client.get_channel(text_channels["welcome"])
        await channel.send(random.choice(greetings).format(member.mention))

    #Role assignment
    @client.event
    async def on_raw_reaction_add(payload):
        await manage_roles(payload, True)
    
    @client.event
    async def on_raw_reaction_remove(payload):
        await manage_roles(payload, False)

    async def manage_roles(payload, add_role: bool):
        
        if not payload.message_id in mapping:
            print("returned on message id")
            return

        if not str(payload.emoji) in mapping[payload.message_id]:
            print("returned on mapping")
            return

        role_emoji = mapping[payload.message_id][str(payload.emoji)]
        role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=role_emoji)
        member = discord.utils.get(client.get_guild(payload.guild_id).members, id=payload.user_id)

        if add_role:
            await payload.member.add_roles(role)
            msg = f"You have given yourself the **{role.name}** role on the **{role.guild} discord server**!"
            await payload.member.send(content = msg)

        else:
            await member.remove_roles(role)
        
        

    client.run(TOKEN)

run_bot()