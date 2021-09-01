# Communib33

I'd like to present my proposal for a Nifty Island community Discord bot - Communib33!

Simply put, Communib33 is a Discord bot intended to track community involvement and interaction on the Nifty Island server. It introduces a Kudos system, which allows users to give each other props for sharing interesting articles, incredible art or music, helpful comments, great memes, or other excellent posts that contribute to the net value of the community as a whole. Community members will also be able to earn kudos by directly growing the server - one kudos per member that joins from one of your invite links. User kudos counts could then be used for all sorts of things, like tickets in a giveaway or qualification for special roles.

Currently, the bot is just a prototype. A few of the features are implemented, though not to their fullest potential. It is also hosted on my PC, and all the instructions below demonstrate how to do the same; the final version would obviously have to be hosted in the Cloud someplace.

## Features

Here is a list of what Communib33 can do for you, now or in the future:

### Current

* DM replies to requests for important links (currently just the website).
* Kudos system - users can give each others kudos for high-quality comments, and the bot will keep track of kudos.

### Future

* Providing community assets on request (files, base images, base models).
* Check raffle eligibility based on user tags, roles, or kudos count.
* Post report of top comments of the past week/month as an automated scheduled task (based on total reactions).
* Post report of users who have achieved a particular accomplishment over a given time (most kudos earned, biggest memer, etc).
* Keeping track of who invited who to the server, and awarding kudos for it.

## Commands

* Prefix: `!`
* `communib33` - Get a DM of the command menu.
* `kudos` - Get a DM of your current kudos count.
* `kudos @<user>` - Give a member of the community a kudos. Works with message replies using just the `!kudos` command, too. You can give up to three kudos a day, which resets at midnight UTC.
* `What's the website` - Will detect this exact string of text, regardless of case or presence of the apostrophe, and send a DM to the user containing a link to the [Nifty Island website](https://www.niftyisland.com/).

## Technology Used

Below is a list of all the important technology used in the production of this app.

### Development Environment

* [Docker](https://www.docker.com/): The entire app lives in Docker containers managed using the Docker Desktop app for Windows.
* [Docker Compose](https://docs.docker.com/compose/): This is used to set up a virtual development environment to host all of the servers the application utilizes in order to function.
* [pipenv](https://pipenv.pypa.io/en/latest/): My virtual environment and package manager of choice.

### Python Modules/Libraries

* [Asyncio](https://docs.python.org/3/library/asyncio.html): Most of the app's activities have been made asynchronous.
* [Discord.py](https://discordpy.readthedocs.io/en/stable/#): This library allowed for the use of all the objects and methods in the Discord API.
* [MongoEngine](http://mongoengine.org/): I used MongoEngine to map objects to the database as documents.

### External Services

* [Discord](https://discord.com/developers/applications): You have to create a bot through the Discord developer portal. This will give you a token that you can use to connect to your bot, and a link to add your bot to servers. I would recommend following [this guide](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) to assist in setting up a bot.
* [MongoDB](https://www.mongodb.com/): The MongoDB database will hold records of all users that have received kudos (along with every kudos they have received), the top contributor and top comment histories, references to community assets, the invite history, and whatever else the bot might need to store.
* [MongoExpress](https://github.com/mongo-express/mongo-express): The admin interface to interact with the database.

## Requirements

1. [Install Python](https://www.python.org/downloads/).
2. [Install Docker](https://docs.docker.com/get-docker/).
3. [Install Docker Compose](https://docs.docker.com/compose/install/).
    * **!!**: If you are on Mac or Windows and have installed Docker Desktop, you don't need to worry about installing Docker Compose, as it comes with Docker Desktop. Only Linux users need to worry about this step.
4. Clone this repository onto your machine.

## Setting Up the Local Python Environment

Once you have everything installed, you will have to set up your Python environment.

1. Go into the repository on your machine, and `cd` into the backend directory.
2. Run the command `pipenv shell` to set up a virtual environment in the backend directory.
3. Run the command `pipenv install --dev` to install the dependencies.
4. Run the command `pip freeze > requirements.txt`. This will update your requirements document with all of the necessary dependencies to use this application.

Note that any time you install new packages not listed here, you will have to perform step 4 again in order to update your requirements.txt file with all of the necessary dependencies. Then, you must also rebuild the Docker images with the `docker compose up --build` command. See the **Building Up and Tearing Down the Docker Containers** section below for more information.

## Setting Up the Config File

I have provided a sample config file in this repository, but it will take a little work to get it ready to use. Here's the code inside the [sample_config.py](bot/src/sample_config.py) file:

```python
username = '<Your MongoDB username.>'
password = '<Your MongoDB password.>'
database = '<The name of the MongoDB database you are using.>'
token = '<Your Discord bot token.>'


task_ignore_result = False
timezone = 'UTC'
beat_schedule = {
    "reset_daily_kudos_tasks": {
        "task": "main.reset_daily_kudos_task",
        "schedule": crontab(hour=0, minute=0)
    }
}
}
```

The first thing you will have to do will be to rename the file to `config.py`. Make sure it is still in the bot/src directory.

Any of the text in `<angle brackets>` above should be replaced with whatever it says. So, your username will be your MongoDB username, your token will be your personal bot token from Discord, and so on.

If you wish, you can change the frequency with which the kudos count for all users will be reset. I would recommend keeping it to once per day, at an hour and minute denoted by the `hour` and `minute` values passed to `crontab` in the schedule. The hours are represented in a 24-hour clock format. To schedule it twice or more per day, you can instead pass a string of the numbers representing the hours. So, passing `hour="6, 18"` will cause the app to update the kudos count as 6 am and 6 pm UTC.

Apart from these values, I wouldn't recommend updating anything.

## Building Up and Tearing Down the Docker Containers

This app is using Docker Compose, so once everything is installed and set up, the `docker-compose.yml` file should have everything the application needs to dockerize itself using just three commands.

1. From the root directory of the project, run the command `docker compose up --build`. This will build the images for the first time, install all of the dependencies in your requirements.txt file, and launch the application.
2. Whenever you would like to build the application after the first time, you can use `docker compose up` instead.
3. To bring down the application, use `Ctrl+C` inside the terminal to stop the server. Once it is down, use the command `docker compose down` to dismount it from Docker.
