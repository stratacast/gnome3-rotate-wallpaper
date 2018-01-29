#!/usr/bin/python3

# This file is part of gnome-rotating-wallpaper.
# Copyright (C) 2018 stratacast

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import subprocess
import imghdr
import os
from os.path import isfile, join
import time
import random

timer = 15

def main():
    #directory = ""
    directory = ""
    photo_list = []
    count = 0

    for filename in os.listdir(directory):
        picture = join(directory, filename)
        if isfile(picture) and imghdr.what(picture):
            photo_list.append(picture)
            count+=1

    last_wallpaper = 0

    while True:
        p_index = last_wallpaper

        while p_index == last_wallpaper:
            p_index = random.randint(1, count) - 1

        photo = photo_list[p_index]
        command = "gsettings set org.gnome.desktop.background picture-uri file:///" + str(photo)
        subprocess.run(command.split())

        time.sleep(timer)


if(__name__ == "__main__"):
    main()
