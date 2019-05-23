from django.contrib import admin
from django.contrib.sessions.models import Session
from core.models import Player
# Register your models here.

class CashValueFilter(admin.SimpleListFilter):
    title = 'Cash Value'
    parameter_name = 'cash_value'

    def lookups(self, request, model_admin):
        filters = []
        for value in Player.CASH_LIST:
            filters.append((value, value))
        return filters

    def queryset(self, request, queryset):
        value = self.value()
        for session in queryset:
            print(queryset)
            if session.get_decoded()['cash'] != value:
                queryset.exclude(session_key=session.session_key)
                print(queryset)
        return queryset

class SessionAdmin(admin.ModelAdmin):
    def cash_value(self, obj):
        return obj.get_decoded()['cash']
    list_display = ['session_key', 'cash_value', 'expire_date']
    list_filter = [CashValueFilter]
admin.site.register(Session, SessionAdmin)