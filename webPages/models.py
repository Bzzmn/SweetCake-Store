# pylint: disable=no-member

import uuid
from django.db import models
from django.urls import reverse
from slugify import slugify



# Create your models here.

# MODELO ABSTRACTO PRODUCTOS
class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    image_url = models.URLField()
    slug = models.SlugField(unique=True, blank=True)
    is_private = models.BooleanField(default=False)
    visit_count = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Genera un slug solo si es nuevo o si el nombre ha cambiado
        if not self.slug or not self.pk or self.__name_changed():
            self.slug = self.__create_unique_slug()
        super().save(*args, **kwargs)

    def __name_changed(self):
        if self.pk:
            # Usar type(self) para obtener la clase concreta de la instancia
            original = type(self).objects.get(pk=self.pk)
            return original.name != self.name
        return False

    def __create_unique_slug(self):
        # Crea un slug único
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug

    class Meta:
        abstract = True


# MODELO TORTA
class Torta(Product):
    # Campos específicos de tortas si los hay
    def get_absolute_url(self):
        return reverse("torta_detalle", kwargs={"slug": self.slug})


# MODELO CUPCAKE
class Cupcake(Product):
    # Campos específicos de cupcakes si los hay
    def get_absolute_url(self):
        return reverse("cupcake_detalle", kwargs={"slug": self.slug})


# MODELO CONTACT FORM
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
