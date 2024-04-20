# dump_data.py
import sys
import django
from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Dumps data into a JSON file with UTF-8 encoding'

    def handle(self, *args, **options):
        with open('data.json', 'w', encoding='utf-8') as f:
            call_command('dumpdata', stdout=f) 

