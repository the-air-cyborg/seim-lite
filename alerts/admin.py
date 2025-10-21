from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'source_ip', 'event_type', 'severity')
    list_filter = ('severity', 'event_type')
    search_fields = ('source_ip', 'event_type', 'description')
    ordering = ('-timestamp',)
