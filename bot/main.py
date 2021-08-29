#! python3

# 3p Imports
import discord

# Internal Imports
try:
    from src.config import token
except Exception as e:
    print (e)


client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}.")


@client.event
async def on_message(msg):
    trigger = "beep"
    response = "boop"
    if trigger in str(msg.content):
        await msg.channel.send(response)
        return


client.run(token)
