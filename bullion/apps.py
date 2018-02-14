from django.apps import AppConfig
import stooq


class BullionConfig(AppConfig):
    name = 'bullion'

    def ready(self):
        print('BullionConfig.ready here!')
        stooq.start_updating(5)
