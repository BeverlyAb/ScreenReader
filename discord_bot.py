# This example requires the 'message_content' intent.

import discord

def read_token():
    with open("token.txt") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi") # If the user says !hello we will send back hi


client.run(token)

# intents = discord.Intents.default()
# intents.messages = True

# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# client.run('your token here')
