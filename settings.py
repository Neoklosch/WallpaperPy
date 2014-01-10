#!/usr/bin/env python

import os, shelve

class Settings:
    __settings_file = '/home/markus/.wallpaper-settings'
    __image_folder = '/home/markus/Bilder/'
    # __interval = 60 * 10 # 10 minutes
    __interval = 10 # 10 seconds

    def __init__(self):
        self.load_settings()

    def image_folder(self):
        return self.__image_folder

    def set_image_folder(self, value):
        if (type(value)) == str and value:
            if os.path.isdir(value):
                self.__image_folder = value
                return True
            else:
                print '--- folder does not exists'
                return False
        else:
            print '--- set image folder: incorrect value'
            return False

    def interval(self):
        return self.__interval

    def set_interval(self, value):
        try:
            value = int(value)
        except ValueError:
            print '--- set interval: incorrect value'
            return False

        if value > 10:
            self.__interval = value
            return True
        else:
            print '--- interval is to short'
            return False

    def save_settings(self):
        shelf = shelve.open(self.__settings_file)
        shelf['folder'] = self.__image_folder
        shelf['interval'] = self.__interval
        shelf.close()

    def load_settings(self):
        if os.path.exists(self.__settings_file):
            shelf = shelve.open(self.__settings_file)
            self.__image_folder = shelf['folder']
            self.__interval = shelf['interval']
            shelf.close()
        else:
            print '--- No settings file available'