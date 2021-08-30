#! python3

# SL Imports
import logging

# 3p Imports
import discord

# Internal Imports
try:
    from src.config import token
except Exception as e:
    print (e)


client = discord.Client()


@client.event
async def on_message(msg):
    text = str(msg.content)
    logging.warning(text)
    if "whats the website" in text.lower().replace("'", ""):
        return await msg.channel.send("Here you go! https://www.niftyisland.com/")

if __name__ == "__main__":
    client.run(token)
