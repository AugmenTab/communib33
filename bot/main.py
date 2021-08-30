#! python3

# SL Imports
import logging
from typing_extensions import ParamSpecArgs

# 3p Imports
import discord
from   discord.ext import commands

# Internal Imports
try:
    from src.config import token
except Exception as e:
    print (e)


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
    giver = ctx.author.id
    if len(ctx.message.mentions) > 0:
        receiver = ctx.message.mentions[0]
    else:
        receiver = None
    if not receiver:
        await ctx.reply("Whoopsie! You've gotta @mention someone to give them kudos!")
    elif receiver.bot:
        await ctx.reply("Whoopsie! Bots like us have no use for kudos!")
    elif giver == receiver.id:
        ## TODO DM user with their own kudos count.
        await ctx.send("Here are your kudos!")
    else:
        ## TODO Add a kudos to receiver.
        logging.warning(receiver.id)
        await ctx.message.add_reaction("⭐")


if __name__ == "__main__":
    b33.run(token)
