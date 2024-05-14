from django.contrib import admin
from .models import Productos, CambioStock


# Register your models here.

admin.site.register(Productos)
admin.site.register(CambioStock)
