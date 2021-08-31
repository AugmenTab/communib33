#! python3

# PSL Imports
from datetime import datetime

# 3p Imports
import mongoengine as db


# Internal Imports
try:
    from src.config import username, password, database
except Exception as e:
    print(e)


class Kudos(db.EmbeddedDocument):
    user_id: db.IntField(primary_key=True)
    channel_id: db.IntField(required=True)
    message_id: db.IntField(required=True)
    timestamp: db.DateTimeField(required=True)

    def to_json(self):
        return {
            "user_id": self.user_id,
            "channel_id": self.channel_id,
            "message_id": self.message_id,
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
