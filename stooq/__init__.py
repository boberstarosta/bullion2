from .threads import PriceUpdateThread


def start_updating(interval):
    print('Starting price update daemon.')
    thread = PriceUpdateThread(interval)
    thread.start()
