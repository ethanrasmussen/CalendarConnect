# ![](https://github.com/ethanrasmussen/CalendarConnect/blob/master/art/cc_icon_small.png) CalendarConnect
This program links your Discord status to your calendar! After seeing a [post on Reddit](https://www.reddit.com/r/discordapp/comments/hs0d6l/its_always_bugged_me_that_you_cant_schedule/), I was inspired to find a way to utilize Discord's custom status feature in conjunction with one's schedule. So... I made this! It ended up being a fun project, and a great way to start learning PyQT5! CalendarConnect currently only supports [Teamup](https://www.teamup.com/) calendars (an underrated favorite of mine), but I'm hoping to add support for other popular calendars like Google Calendar & Outlook Calendar in the future.

## Usage:
Currently, you'll need to clone this repo to use the program. I'm working on creating an executable, but unfortunately Pyinstaller has been giving me a bit of trouble due to the included image files. So, for now, here's what you'll need to do to run the program:
#### Step 1:
Make sure you have a Teamup calendar set with events! It could look something like this:

![](https://github.com/ethanrasmussen/CalendarConnect/blob/master/art/cc_demo_4.PNG)
#### Step 2:
Clone this repo, and install the required [dependencies](https://github.com/ethanrasmussen/CalendarConnect/blob/master/README.md#dependencies) via pip.
#### Step 3:
Run [run.pyw](https://github.com/ethanrasmussen/CalendarConnect/blob/master/run.pyw) (for no terminal/cmd line) or [cc_gui.py](https://github.com/ethanrasmussen/CalendarConnect/blob/master/cc_gui.py).
#### Step 4:
Enter your login details for Discord and the link to your Teamup calendar (don't worry, this data isn't stored anywhere! feel free to take a look in the code for yourself!).

![](https://github.com/ethanrasmussen/CalendarConnect/blob/master/art/cc_demo_1.PNG)
#### Step 5:
Boom! You're linked! You'll now see this dialogue:

![](https://github.com/ethanrasmussen/CalendarConnect/blob/master/art/cc_demo_2.PNG)

And your Discord status should update according to your calendar!

![](https://github.com/ethanrasmussen/CalendarConnect/blob/master/art/cc_demo_3.PNG)
#### Hope you enjoy!!



### Main Limitations (With the current Teamup version):
- Cannot use "All-Day" events within Teamup
- Cannot detect different Teamup sub-calendars
- Local time (on PC) must match timezone of Teamup calendar
- Cannot handle concurrent events

### TODO List (Not in any particular order):
- Create an executable version of the program
- Error/exception handling, for when a user mis-enters their information, or Discord and/or Teamup are offline
- Ability to minimize window to tray
- Support for Google Calendar & Outlook Calendar
- Support for changing Discord status between 'online', 'idle', 'do not disturb' and 'invisible' based on calendar events
- Support for "all-day" events
- Support for concurrent events (either by displaying both, or by having one override another)

### Image Attributions:
- [Discord Logo](https://www.iconfinder.com/icons/4373196/discord_logo_logos_icon) by [Flatart](https://www.freepik.com/flatart)
- [Calendar Icon](https://www.iconfinder.com/icons/285670/calendar_icon) by Paomedia / [CC BY](https://creativecommons.org/licenses/by/3.0/)
- [Wumpus Art](https://www.deviantart.com/inklessrambles/art/Wumpus-797089963) by [inklessrambles](https://www.deviantart.com/inklessrambles)

### Dependencies:
- [PyQT5](https://pypi.org/project/PyQt5/) == 5.15.0
- [requests](https://pypi.org/project/requests/) == 2.24.0
- [schedule](https://pypi.org/project/schedule/) == 0.6.0
