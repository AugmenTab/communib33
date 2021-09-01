#! python3


about = {
    "b33": {
        "desc": "DMs the requester the communib33 command list."
    },
    "kudos": {
        "desc": "Gives a user kudos, or checks your own kudos.",
        "noref": "Whoopsie! You've gotta @ someone to give them kudos!",
        "bot": "Whoopsie! Bots like us have no use for kudos!",
        "not_enough": "Whoopsie! You've used up your kudos for the day!"
    }
}


command_list = """
Communib33 Command List

Prefix - `!`

`kudos` - Get your current kudos count. Alternatively, grant kudos to another user if used in a message reply.

`kudos @<user>` - Grant kudos to the mentioned user.

In addition to these commands, Communib33 will also listen to message content asking for the following important links, and send them to you in a DM!
- website
"""


emojis = {
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "eyes": "👀",
    "no_entry": "⛔",
    "star": "⭐"
}


links = {
    "website": "Here you go! https://www.niftyisland.com/"
}


def formatKudos(name, num, server):
    return f"Hi, {name}! You have {num} kudos in the {server} server! ⭐"
