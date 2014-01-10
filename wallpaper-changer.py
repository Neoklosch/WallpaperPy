#!/usr/bin/env python

import sys
from changer import Changer
from optparse import OptionParser
from daemon import Daemon
from settings import Settings

class ChangerDaemon(Daemon):
    def run(self):
        wallpaper_changer = Changer()
        wallpaper_changer.change_wallpaper_after_time()

def load_args():
        parser = OptionParser("WallpaperChanger [Optionen]")
        parser.add_option("-f", "--folder", dest="image_folder", help="Absolute path of your image folder.")
        parser.add_option("-i", "--interval", dest="interval", help="Time interval to change the wallpapers in seconds. Minimum are 10 seconds.")

        return parser.parse_args()


if __name__ == "__main__":
    (options, args) = load_args()
    settings = Settings()
    settings.set_interval(options.interval)
    settings.set_image_folder(options.image_folder)
    settings.save_settings()

    daemon = ChangerDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) >= 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
