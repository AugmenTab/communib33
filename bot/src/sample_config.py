#! python3

from celery.schedules import crontab


username = '<Your MongoDB username.>'
password = '<Your MongoDB password.>'
database = '<The name of the MongoDB database you are using.>'
token = '<Your Discord bot token.>'


task_ignore_result = False
timezone = "UTC"
beat_schedule = {
    "reset_daily_kudos_tasks": {
        "task": "main.reset_daily_kudos_task",
        "schedule": crontab(hour=0, minute=0)
    }
}
