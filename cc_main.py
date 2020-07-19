import requests, json, schedule, ast, datetime, time
from typing import List
import discord_status_update as dsu


# NOTICE: The 'schedule' module uses the machine's local time. Therefore, you should ensure that this matches the timezone of your calendar.



class StatusEvent:

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end