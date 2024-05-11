from django.contrib import admin

from . import models


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'telegram_id']
    list_display_links = None
    list_editable = ['telegram_id']


class PairAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'isUsed']
    list_editable = ['isUsed']
    list_filter = ['isUsed']


class AlarmAdmin(admin.ModelAdmin):
    list_display = ['user', 'pair', 'price']
    list_editable = ['pair', 'price']
    list_filter = ['user', 'pair', 'price']

admin.site.register(models.TelegramUser, TelegramUserAdmin)
admin.site.register(models.Pair, PairAdmin)
admin.site.register(models.Alarm, AlarmAdmin)