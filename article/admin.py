from django.contrib import admin
from .models import Topics, Rassilka


# Register your models here.

admin.site.register(Topics)
#admin.site.register(Photo)

#class NoteAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Rassilka)
