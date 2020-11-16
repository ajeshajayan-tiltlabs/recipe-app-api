import time

from django.db.utils import OperationalError
from django.db import connections
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db to start"""
    def handle(self, *args, **options):
        self.stdout.write('wait for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
