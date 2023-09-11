
from django.core.management.base import BaseCommand
from Adun.models import PatientRegistration  # Import your PatientRegistration model

class Command(BaseCommand):
    help = 'Delete registered patients'

    def handle(self, *args, **options):
        # Delete all registered patients
        PatientRegistration.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Registered patients deleted successfully'))

