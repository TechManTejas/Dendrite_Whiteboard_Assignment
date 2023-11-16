from django.contrib import admin
from .models import Whiteboard

@admin.register(Whiteboard)
class WhiteboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'description')
    search_fields = ('title', 'host__username')
    filter_horizontal = ('clients', 'invitees')
