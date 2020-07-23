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

class DiscordStatusUpdater:

    def __init__(self, events:List[StatusEvent], discord_email:str, discord_password:str):

        # init variables
        self.events = events
        self.dis_email = discord_email
        self.dis_password = discord_password

        # touch base with Discord servers and obtain 'fingerprint'
        self.fingerprint = fingerprint = ast.literal_eval(requests.post(url="https://discord.com/api/v6/auth/fingerprint").content.decode("UTF-8"))['fingerprint']

        # begin session
        self.s = requests.Session()
        r = self.s.get(url="https://discord.com/channels/@me", headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        })

        # login
        r_login = self.s.post(url="https://discord.com/api/v6/auth/login", headers={
            "content-type": "application/json",
            "origin": "https://discord.com",
            "referer": "https://discord.com/login?redirect_to=%2Fchannels%2F%40me",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "x-fingerprint": fingerprint,
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzgzLjAuNDEwMy4xMTYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjgzLjAuNDEwMy4xMTYiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vY2hhbm5lbHMvQG1lIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjYzNjAxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }, data=json.dumps({
            "captcha_key": None,
            "email": self.dis_email,
            "gift_code_sku_id": None,
            "login_source": None,
            "password": self.dis_password,
            "undelete": False
        }))
        # get token
        self.token = ast.literal_eval(r_login.content.decode("UTF-8"))['token']


    def daily_schedule_update(self):
        for event in self.events:
            # get the timestamp for 1 minute before event ends
            today = datetime.datetime.today()
            event_end = (datetime.datetime(today.year, today.month, today.day, hour=int(event.end.split(':')[0]), minute=int(event.end.split(':')[1])) + datetime.timedelta(minutes=-1)).time().strftime('%H:%M')
            # schedule a discord status update to begin
            schedule.every().day.at(event.start).do(dsu.update_status, status=event.name, session=self.s, fingerprint=self.fingerprint, token=self.token)
            # schedule the discord status to clear 1 minute before event end
            schedule.every().day.at(event_end).do(dsu.clear_status, session=self.s, fingerprint=self.fingerprint, token=self.token)



# get calendar and create status updater
def status_updates(calendar:str, email:str, password:str):
    cal = TeamupCalendar(calendar)
    events = cal.get_events()
    update = DiscordStatusUpdater(events, email, password)


# link teamup calendar to status updates on Discord
def link_teamup_calendar(email:str, password:str, teamup_link:str):
    # add today's events to status update queue
    cal = TeamupCalendar(teamup_link)
    events = cal.get_events()
    update = DiscordStatusUpdater(events, email, password)
    update.daily_schedule_update()
    # update status based on calendar (will start next day)
    schedule.every().day.at('00:00').do(status_updates, calendar=teamup_link, email=email, password=password)
    while True:
        schedule.run_pending()
        time.sleep(1)