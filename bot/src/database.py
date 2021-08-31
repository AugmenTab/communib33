#! python3

# PSL Imports
import logging
from datetime import datetime

# 3p Imports
import mongoengine as db


# Internal Imports
try:
    from src.config import username, password, database
except Exception as e:
    print(e)


class Kudos(db.EmbeddedDocument):
    message_id = db.IntField(primary_key=True)
    channel_id = db.IntField(required=True)
    giver_id = db.IntField(required=True)
    receiver_id = db.IntField(required=True)
    timestamp = db.DateTimeField(required=True)

    def to_json(self):
        return {
            "message_id": self.message_id,
            "channel_id": self.channel_id,
            "giver_id": self.giver_id,
            "receiver_id": self.receiver_id,
            "timestamp": self.timestamp
        }


class User(db.Document):
    user_id = db.IntField(primary_key=True)
    name = db.StringField(required=True)
    kudos_today = db.IntField(required=True)
    kudos_given = db.EmbeddedDocumentListField(Kudos)
    kudos_received = db.EmbeddedDocumentListField(Kudos)

    def to_json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "kudos_today": self.kudos_today,
            "kudos_given": self.kudos_given,
            "kudos_received": self.kudos_received
        }


def connect_to_db():
    db.connect(
        db=database,
        host="mongodb://mongodb",
        port=27017,
        username=username,
        password=password
    )


async def get_kudos_count(_id):
    user = User.objects(user_id=_id).first()
    return user.kudos_received.count() if user else 0


async def give_kudos(g, r, msg):
    receiver = User.objects(user_id=r.id).first() or await __create_new_user(r)
    giver = User.objects(user_id=g.id).first() or await __create_new_user(g)
    if giver.kudos_today < 3:
        new_kudos = __create_kudos(g, r, msg)
        giver.kudos_today += 1
        giver.kudos_given.append(new_kudos)
        receiver.kudos_received.append(new_kudos)
        await __update_user(giver)
        await __update_user(receiver)
        return "ok"
    return "not_enough"


def __create_kudos(giver, receiver, msg):
    new_kudos = Kudos(
            message_id = msg.id,
            channel_id = msg.channel.id,
            giver_id = giver.id,
            receiver_id = receiver.id,
            timestamp = datetime.utcnow(),
        )
    return new_kudos

async def __create_new_user(user):
    new_user = User(
        user_id = user.id,
        name = user.name,
        kudos_today = 0,
        kudos_given = [],
        kudos_received = []
    )
    return new_user.save()


async def __update_user(user):
    return user.save()