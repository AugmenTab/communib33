#! python3

# SL Imports
import logging

# 3p Imports
import discord
from   discord.ext import commands

# Internal Imports
import src.text as txt
try:
    from src.config import token
except Exception as e:
    print (e)


# Python Bot Commands and Message Triggers
b33 = commands.Bot(command_prefix="!")


@b33.event
async def on_message(msg):
    if msg.author != b33.user:
        await get_requested_links(msg)
        await b33.process_commands(msg)


@b33.command(name="kudos", help=txt.about["kudos"]["desc"])
async def kudos(ctx):
    msg = ctx.message
    giver = ctx.author
    receiver = msg.mentions[0] if len(msg.mentions) > 0 else msg.author
    if not receiver:
        await giver.send(txt.about["kudos"]["noref"])
    elif receiver.bot:
        await giver.send(txt.about["kudos"]["bot"])
    elif giver.id == receiver.id:
        num = 0 ## Acquire kudos count for the giver
        name = giver.nick or giver.name
        server = giver.guild.name
        logging.warning(msg)
        await giver.send(txt.formatKudos(name, num, server))
    else:
        ## TODO Add a kudos to receiver.
        logging.warning(receiver.id)
        await ctx.message.add_reaction(txt.emojis["star"])


# Helper Functions

async def get_requested_links(msg):
    msg_content = str(msg.content).lower().replace("'", "")
    text = []
    if "whats the website" in msg_content:
        text.append(txt.links["website"])
    if len(text) > 0:
        await msg.add_reaction(txt.emojis["eyes"])
        await msg.author.send('\n'.join(text))


if __name__ == "__main__":
    b33.run(token)
