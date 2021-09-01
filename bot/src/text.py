#! python3


about = {
    "b33": {
        "desc": "DMs the requester the communib33 command list."
    },
    "kudos": {
        "desc": "Gives a user kudos, or checks your own kudos.",
        "noref": "Whoopsie! You've gotta @ someone to give them kudos!",
        "bot": "Whoopsie! Bots like us have no use for kudos!",
        "not_enough": "Whoopsie! You've used up your kudos for the day!",
        "reset": "Daily kudos numbers have been reset."
    }
}


command_list = """
Communib33 Command List

Prefix - `!`

`communib33` - Display this command list.

`kudos` - Get your current kudos count. Alternatively, grant kudos to another user if used in a message reply.

`kudos @<user>` - Grant kudos to the mentioned user.

`What's the website` - Get a DM of the Nifty Island website. Will detect this exact string of text, regardless of case or presence of the apostrophe.
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
