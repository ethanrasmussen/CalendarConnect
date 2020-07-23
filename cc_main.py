import requests, json, schedule, ast, datetime, time
from typing import List
# import discord_status_update as dsu
from pypresence import Presence
import discord_rich_presence as drpc


# NOTICE: The 'schedule' module uses the machine's local time. Therefore, you should ensure that this matches the timezone of your calendar.
client_id = "735164013658374277"


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


# get new calendar events, refreshing the queued statuses/RPC
def queue_events(calendar:TeamupCalendar, rpc:Presence):
    new_events = calendar.get_events()
    for event in new_events:
        # get the timestamp for 1 minute before event ends
        today = datetime.datetime.today()
        event_end = (datetime.datetime(today.year, today.month, today.day, hour=int(event.end.split(':')[0]), minute=int(event.end.split(':')[1])) + datetime.timedelta(minutes=-1)).time().strftime('%H:%M')
        # schedule a discord status update to begin
        schedule.every().day.at(event.start).do(drpc.set_rpc, rpc=rpc, status=event)
        # schedule the discord status to clear 1 minute before event end
        schedule.every().day.at(event_end).do(drpc.clear_rpc, rpc=rpc)


# link teamup calendar to status updates on Discord
def link_teamup_calendar(teamup_link:str):
    # init calendar & get initial events
    cal = TeamupCalendar(teamup_link)
    events = cal.get_events()

    # init RPC & connect to Discord client
    RPC = Presence(client_id)
    RPC.connect()

    # add today's events to status update queue
    for event in events:
        # get the timestamp for 1 minute before event ends
        today = datetime.datetime.today()
        event_end = (datetime.datetime(today.year, today.month, today.day, hour=int(event.end.split(':')[0]), minute=int(event.end.split(':')[1])) + datetime.timedelta(minutes=-1)).time().strftime('%H:%M')
        # schedule a discord status update to begin
        schedule.every().day.at(event.start).do(drpc.set_rpc, rpc=RPC, status=event)
        # schedule the discord status to clear 1 minute before event end
        schedule.every().day.at(event_end).do(drpc.clear_rpc, rpc=RPC)

    # update status queue daily based on calendar (will start next day)
    schedule.every().day.at('00:00').do(queue_events, calendar=cal, rpc=RPC)
    while True:
        schedule.run_pending()
        time.sleep(1)

