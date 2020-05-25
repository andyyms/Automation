from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        new_name = 'new_file_' + str(self.i) + '.txt'
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + '/' + new_name)
            while file_exists:
                self.i += 1
                new_name = 'new_file_' + str(self.i) + '.txt'
                file_exists = os.path.isfile(folder_destination + '/' + new_name)

            src = folder_to_track + '/' + filename
            new_destination = folder_destination + '/' + new_name
            os.rename(src, new_destination)

folder_to_track = '/Users/andyyeung/Desktop/TEST1'
folder_destination = '/Users/andyyeung/Desktop/TEST2'
eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()