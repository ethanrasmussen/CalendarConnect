import requests, json, schedule, ast, datetime, time
from typing import List
import discord_status_update as dsu


# NOTICE: The 'schedule' module uses the machine's local time. Therefore, you should ensure that this matches the timezone of your calendar.



class StatusEvent:

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end


class TeamupCalendar:

    def __init__(self, url:str):
        self.calendar_id = url.split("teamup.com/")[1]

    def get_event_json(self):
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        r = requests.get(url=f"https://teamup.com/{self.calendar_id}/events?startDate={today}&endDate={today}")
        events = r.content.decode("UTF-8")
        return json.loads(events)

    def get_events(self):
        events = self.get_event_json()
        events = events['events']
        # convert JSON to StatusEvent objects
        status_events = []
        for event in events:
            status_event = StatusEvent(event['title'], event['start_dt'].split("T")[1].split("-")[0][:-3], event['end_dt'].split("T")[1].split("-")[0][:-3])
            status_events.append(status_event)
        return status_events

# TODO: MS Calendar
# TODO: Google Calendar