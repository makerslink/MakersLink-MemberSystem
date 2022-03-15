from __future__ import unicode_literals
from django.contrib import admin
import logging
from django.utils.html import format_html

from .models import StatusLog

# Register your models here.
DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE = 50

class StatusLogAdmin(admin.ModelAdmin):
    list_display = ('app', 'colored_msg', 'traceback', 'create_datetime_format')
    list_display_links = ('colored_msg', )
    list_filter = ('level', 'create_datetime', 'app_name')
    list_per_page = DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE

    def colored_msg(self, instance):
        if instance.level in [logging.NOTSET, logging.INFO]:
            color = 'green'
        elif instance.level in [logging.WARNING, logging.DEBUG]:
            color = 'orange'
        else:
            color = 'red'
        return format_html('<span style="color: {color};">{msg}</span>', color=color, msg=instance.msg)
    colored_msg.short_description = 'Message'

    def traceback(self, instance):
        return format_html('<pre><code>{content}</code></pre>', content=instance.trace if instance.trace else '')

    def app(self, instance):
        if instance.app_name:
            return instance.app_name
        else:
            return ''
    app.short_description = 'App Name'

    def create_datetime_format(self, instance):
        return instance.create_datetime.strftime('%Y-%m-%d %X')
    create_datetime_format.short_description = 'Created at'


admin.site.register(StatusLog, StatusLogAdmin)