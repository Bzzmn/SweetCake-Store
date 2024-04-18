import uuid
from django.db import models
from slugify import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

#MODELO TORTA

class Torta(models.Model):
    torta_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(max_length=100, blank=True)
    is_private = models.BooleanField()

    def save(self,*args, **kwargs ):
      if not self.slug:
        self.slug = slugify(self.name)
      super(Torta, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Torta)
def add_uuid(sender, instance, **kwargs):
    if not instance.torta_uuid:
        instance.torta_uuid = uuid.uuid4()

#FIN MODELO TORTA

# MODELO CONTACT FORM

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

