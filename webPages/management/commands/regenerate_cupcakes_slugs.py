from django.core.management.base import BaseCommand
from django.utils.text import slugify
from webPages.models import Cupcake

class Command(BaseCommand):
    help = 'Regenera los slugs de todos los cupcakes basados en sus nombres'

    def handle(self, *args, **options):
        cupcakes = Cupcake.objects.all()
        count = 0
        for cupcake in cupcakes:
            cupcake.slug = slugify(cupcake.name)
            cupcake.save()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Se han regenerado correctamente {count} slugs de cupcakes.'))