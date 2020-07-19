# ![](https://github.com/ethanrasmussen/CalendarConnect/blob/master/art/cc_icon_small.png) CalendarConnect
This program links your Discord status to your calendar! After seeing a [post on Reddit](https://www.reddit.com/r/discordapp/comments/hs0d6l/its_always_bugged_me_that_you_cant_schedule/), I was inspired to find a way to utilize Discord's custom status feature in conjunction with one's schedule. So... I made this! It ended up being a fun project, and a great way to start learning PyQT5! CalendarConnect currently only supports [Teamup](https://www.teamup.com/) calendars (an underrated favorite of mine), but I'm hoping to add support for other popular calendars like Google Calendar & Outlook Calendar in the future.

### Usage:

### Main Limitations (With the current Teamup version):
- Cannot use "All-Day" events within Teamup
- Cannot detect different Teamup sub-calendars
- Local time (on PC) must match timezone of Teamup calendar
- Cannot handle concurrent events

### TODO List (Not in any particular order):
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
