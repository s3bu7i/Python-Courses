from typing import Any
from django.core.management import BaseCommand,call_command


class Command(BaseCommand):
    help = ''
    
    
    
    def handle(self, *args: Any, **options: Any):
        
        call_command('makemigrations')
        call_command('migrate')

        