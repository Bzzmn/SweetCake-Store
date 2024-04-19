import uuid
from django.db import models
from slugify import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

#MODELO ABSTRACTO PRODUCTOS 
class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    visit_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

#MODELO TORTA
class Torta(Product):
    # Campos específicos de tortas si los hay
    pass

#MODELO CUPCAKE
class Cupcake(Product):
    # Campos específicos de cupcakes si los hay
    pass

# MODELO CONTACT FORM
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

