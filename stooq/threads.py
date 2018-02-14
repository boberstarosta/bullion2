import time
from threading import Thread


class PriceUpdateThread(Thread):
    def __init__(self, interval):
        super().__init__(daemon=True)
        self.interval = interval

    def run(self):
        while True:
            print('[PriceUpdateThread] Working...')
            time.sleep(self.interval)
