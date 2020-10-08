import discord

client = discord.Client()
token = ""

@client.event
async def on_member_join(member):
    print("member joined")
    server = member.guild

    #await member.send(welcome_msg.format(member, server))
    await client.get_channel(760697489711693880).send("{0.mention} has joined".format(member))



@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run(token)