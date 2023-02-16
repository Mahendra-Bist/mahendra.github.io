from django.contrib import admin

# Register your models here.
from .models import contact

# Register your models here.
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Phone','Message')