from django.contrib import admin
from .models import *


class LogAdmin(admin.ModelAdmin):
    date_hierarchy = "created_time"
    list_display = ("user", "action", "created_time")


admin.site.register(Log, LogAdmin)
