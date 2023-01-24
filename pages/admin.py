from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def tumbnail(self, object): # Functie in een class self data invoegen. In object wordt alle teamdata doorgegeven
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    tumbnail.short_description = 'Picture' 

    list_display = ('id', 'tumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'tumbnail', 'first_name',) # Omdat het een tuple moet zij eindigen we met een 
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',) # comma aan het einde omdat het een tuple is en het is er maar eentje

admin.site.register(Team, TeamAdmin)