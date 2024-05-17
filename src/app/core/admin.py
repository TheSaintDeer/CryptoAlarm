from django.contrib import admin

from . import models


class TelegramChatAdmin(admin.ModelAdmin):
    list_display = ['pk', 'chat_id', 'timezone']
    list_display_links = None
    list_editable = ['timezone']


class PairAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'isUsed']
    list_editable = ['isUsed']
    list_filter = ['isUsed']


class AlarmAdmin(admin.ModelAdmin):
    list_display = ['user', 'pair', 'time']
    list_editable = ['pair', 'time']
    list_filter = ['user', 'pair', 'time']

admin.site.register(models.TelegramChat, TelegramChatAdmin)
admin.site.register(models.Pair, PairAdmin)
admin.site.register(models.Alarm, AlarmAdmin)