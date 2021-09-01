#! python3

# SL Imports
import asyncio

# 3p Imports
from celery import Celery
from discord.ext import commands
import discord

# Internal Imports
from src.config import token
import src.database as db
import src.text as txt


def make_celery():
    celery = Celery(
        "celery",
        broker="amqp://rabbit:password@rabbitmq"
    )
    celery.config_from_object("src.config")
    return celery


db.connect_to_db()
celery_app = make_celery()


@celery_app.task
def reset_daily_kudos_task():
    asyncio.run(db.update_daily_kudos(0))
    print(txt.about["kudos"]["reset"])


# Python Bot Commands and Message Triggers
b33 = commands.Bot(command_prefix="!")


@b33.event
async def on_message(msg):
    if msg.author != b33.user:
        await get_requested_links(msg)
        await b33.process_commands(msg)


@b33.command(name="communib33", help=txt.about["b33"]["desc"])
async def communib33(ctx):
    await ctx.author.send(txt.command_list)


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
        num = await db.get_kudos_count(receiver.id)
        name = giver.nick or giver.name
        server = giver.guild.name
        await giver.send(txt.formatKudos(name, num, server))
    else:
        result = await db.give_kudos(giver, receiver, msg)
        if result["msg"] == "ok":
            number_emoji = str(result["kudos_today"])
            await ctx.message.add_reaction(txt.emojis["star"])
            await ctx.message.add_reaction(txt.emojis[number_emoji])
        else:
            await ctx.message.add_reaction(txt.emojis["no_entry"])
            await giver.send(txt.about["kudos"][result["msg"]])


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
