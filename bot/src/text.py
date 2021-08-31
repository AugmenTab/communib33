#! python3


about = {
    "kudos": {
        "desc": "Gives a user kudos, or checks your own kudos.",
        "noref": "Whoopsie! You've gotta @ someone to give them kudos!",
        "bot": "Whoopsie! Bots like us have no use for kudos!"
    }
}


emojis = {
    "eyes": "👀",
    "star": "⭐"
}


links = {
    "website": "Here you go! https://www.niftyisland.com/"
}


def formatKudos(name, num, server):
    return f"Hi, {name}! You have {num} kudos in the {server} server! ⭐"
