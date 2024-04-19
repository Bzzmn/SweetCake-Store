from django.contrib import admin
from .models import Torta, ContactForm, Cupcake
import random

# Register your models here.

# RESET VISIT COUNTER
def reset_visit_counts(modeladmin, request, queryset=None):
    modeladmin.model.objects.all().update(visit_count=0)
    modeladmin.message_user(request, "Todos los contadores de visitas han sido reseteados")
    reset_visit_counts.short_description = "Resetear todos los contadores de visitas"
    reset_visit_counts.allowed_permissions = ('change',)


# UPDATE FEATURED MOST VISITED
def update_featured_most_visited(modeladmin, request, queryset):
    modeladmin.model.objects.update(is_featured=False)
    top_items = modeladmin.model.objects.filter(is_private=False).order_by('-visit_count')[:5]
    
    for item in top_items:
        item.is_featured = True
        item.save()

    modeladmin.message_user(request, "Productos destacados actualizados correctamente")
    update_featured_most_visited.short_description = "Actualizar destacados - mas visitados"


# UPDATE FEATURED RANDOM
def update_featured_random(modeladmin, request, queryset):
    modeladmin.model.objects.update(is_featured=False)
    item_count = modeladmin.model.objects.filter(is_private=False).count()
    count_to_fetch = min(5, item_count)
    if item_count > 0:
        random_items = modeladmin.model.objects.filter(is_private=False).order_by('?')[:count_to_fetch]

        for item in random_items:
            item.is_featured = True
            item.save()

        modeladmin.message_user(request, f"{count_to_fetch} productos fueron destacados aleatoriamente.")
    else:
        modeladmin.message_user(request, "No hay suficientes productos para destacar.")

    update_featured_random.short_description = "Actualizar destacados - selección aleatoria"


class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug', 'uuid',)
    list_display = ['name', 'price', 'visit_count', 'is_featured']
    actions = [reset_visit_counts, update_featured_most_visited, update_featured_random]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'reset_visit_counts' in actions:
            actions['reset_visit_counts'][0].allowed = True
        return actions

@admin.register(Torta)
class TortaAdmin(ProductAdmin):
    pass

@admin.register(Cupcake)
class CupcakeAdmin(ProductAdmin):
    pass

admin.site.register(ContactForm)

