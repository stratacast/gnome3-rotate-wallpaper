# gnome3-rotate-wallpaper
Barebones Python for rotating your wallpapers on GNOME 3

I made this because the GNOME Foundation removed this after version 3.4 (or whichever old version that was), and I finally got peeved and wanted the functionality back. I hope this is of benefit to you too.

## Installing the script
The easiest way to install the script for now, is to put it somewhere in your local directory, and initiate it at boot via a cronjob. 

For example, my script is in ~/.local/bin/rotating-wallpaper.py
I also made the script executable.

Finally, for the cronjob you can simply add a line like:
`@reboot /usr/bin/python3 /path/too/rotating-wallpaper.py`

## Stopping and restarting
There may be times you want to stop and restart the script. I simply just pull up the gnome-system-monitor and do a search for `rotating-wallpaper.py` and it shows the python process. Simply end it. 

To start the process in the background, run: `nohup /path/to/rotating-wallpaper.py > /dev/null 2>&1 &`

Finally, be certain to add the absolute path to `directory = ""` in the script and save the change. You can also adjust the time that is in between pictures by changing the "timer" value, which is done in seconds. So, 30 is 30 seconds, and 120 is 2 minutes. This script also only rotates pictures randomly and in no particular order.

I hope to make this more user-friendly over time, with a Python GUI and all, but this is the basis for now and it works.
