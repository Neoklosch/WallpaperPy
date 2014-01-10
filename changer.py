#!/usr/bin/env python

import commands, sched, time, os
from random import randint
from settings import Settings

class Changer:
    __scheduler = sched.scheduler(time.time, time.sleep)
    __settings = None

    def __init__(self):
        self.__settings = Settings()

    def change_wallpaper_after_time(self):
        self.change_wallpaper()
        self.__scheduler.enter(self.__settings.interval(), 1, self.change_wallpaper_after_time, ())
        self.__scheduler.run()

    def change_wallpaper(self):
        files = self.get_all_available_wallpapers()
        file_length = len(files)
        if file_length > 1:
            while True:
                selected_file = '\'file://%s\'' % self.get_random_wallpaper(files)
                actual_wallpaper = self.get_actual_wallpaper()
                if selected_file != actual_wallpaper:
                    break

            command = 'gsettings set org.gnome.desktop.background picture-uri %s' % selected_file
            status, output = commands.getstatusoutput(command)
        else:
            print '--- Not enough wallpapers in the folder! Minimum is 2.'

    def get_all_available_wallpapers(self):
        files = []
        for single_file in os.listdir(self.__settings.image_folder()):
            if os.path.isfile(self.__settings.image_folder() + single_file):
                files.append(self.__settings.image_folder() + single_file)

        return files

    def get_random_wallpaper(self, files):
        file_length = len(files)
        selected_file = ''
        if file_length > 1:
            randnum = randint(0, file_length - 1)
            selected_file = files[randnum]

        return selected_file

    def get_actual_wallpaper(self):
        command = 'gsettings get org.gnome.desktop.background picture-uri'
        status, output = commands.getstatusoutput(command)
        return output