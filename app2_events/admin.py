from django.contrib import admin
from .models import Event, Session, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'date', 'organizer']
    list_filter = ['date']
    search_fields = ['title', 'description', 'location']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'event', 'speaker', 'start_time', 'end_time']
    list_filter = ['event']
    search_fields = ['title', 'speaker']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'registered_at']
    list_filter = ['registered_at']
    search_fields = ['user__username', 'event__title']
