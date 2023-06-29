from django.contrib import admin

from .models import Event, Session


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'needed_permission')


admin.site.register(Event, EventAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'event')


admin.site.register(Session, SessionAdmin)
