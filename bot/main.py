#! python3

# SL Imports
import logging

# 3p Imports
import discord
from   discord.ext import commands

# Internal Imports
try:
    from src.config import token
except Exception as e:
    print (e)


# Python Bot Commands and Message Triggers
b33 = commands.Bot(command_prefix="!")


@b33.event
async def on_message(msg):
    if msg.author == b33.user:
        await b33.process_commands(msg)
        return
    text = str(msg.content)
    if "whats the website" in text.lower().replace("'", ""):
        await msg.reply("Here you go! https://www.niftyisland.com/")
    await b33.process_commands(msg)


@b33.command(name="kudos", help="Gives a user kudos, or checks your own kudos.")
async def kudos(ctx):
    msg = ctx.message
    giver = ctx.author
    receiver = msg.mentions[0] if len(msg.mentions) > 0 else msg.author
    if not receiver:
        await ctx.reply("Whoopsie! You've gotta @ someone to give them kudos!")
    elif receiver.bot:
        await ctx.reply("Whoopsie! Bots like us have no use for kudos!")
    elif giver.id == receiver.id:
        ## Acquire kudos count for the giver
        n = giver.nick or giver.name
        s = giver.guild.name
        logging.warning(msg)
        await giver.send(f"Hi, {n}! You have {0} kudos in the {s} server! ⭐")
    else:
        ## TODO Add a kudos to receiver.
        logging.warning(receiver.id)
        await ctx.message.add_reaction("⭐")


# Helper Functions

async def get_message(ctx):
    logging.warning(str(ctx))


if __name__ == "__main__":
    b33.run(token)
