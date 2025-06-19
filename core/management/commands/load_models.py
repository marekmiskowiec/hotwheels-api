import json
from django.core.management.base import BaseCommand
from core.models import HotWheelsModel

class Command(BaseCommand):
    help = 'Load Hot Wheels models from JSON file'

    def handle(self, *args, **kwargs):
        with open('hotwheels.json', 'r') as file:
            data = json.load(file)
            for item in data:
                HotWheelsModel.objects.get_or_create(**item)
            self.stdout.write(self.style.SUCCESS('✅ Successfully loaded Hot Wheels models!'))