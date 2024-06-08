from datetime import time

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.action(description="Pairs are not used")
def pair_not_used(modeladmin, request, queryset):
    queryset.update(isUsed=False)

@admin.action(description="Pairs are used")
def pair_used(modeladmin, request, queryset):
    queryset.update(isUsed=True)


class TimeListFilter(admin.SimpleListFilter):
    title = _("time alarm")
    parameter_name = "time"

    def lookups(self, request, model_admin):
        return [
            ("AM", _("AM")),
            ("PM", _("PM")),
        ]

    def queryset(self, request, queryset):
        if self.value() == "AM":
            return queryset.filter(
                time__gte=time(0, 0, 0),
                time__lte=time(11, 59, 59),
            )
        if self.value() == "PM":
            return queryset.filter(
                time__gte=time(11, 59, 59),
                time__lte=time(23, 59, 59),
            )

class TelegramChatAdmin(admin.ModelAdmin):
    list_display = ['chat_id', 'timezone']
    list_display_links = None
    list_editable = ['timezone']
    list_filter = ['chat_id', ]
    filter_input_length = {
        "chat_id": 3,
    }


class PairAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'isUsed']
    list_editable = ['isUsed']
    list_filter = ['isUsed', ]
    actions = [pair_not_used, pair_used]


class AlarmAdmin(admin.ModelAdmin):
    list_display = ['user', 'pair', 'time']
    list_editable = ['pair', 'time']
    list_filter = ['pair', TimeListFilter]


admin.site.register(models.TelegramChat, TelegramChatAdmin)
admin.site.register(models.Pair, PairAdmin)
admin.site.register(models.Alarm, AlarmAdmin)