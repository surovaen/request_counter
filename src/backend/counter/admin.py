from django.contrib import admin
from django.contrib.auth.models import Group, User

from backend.counter.models import Counter


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    readonly_fields = ('count',)

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.unregister(Group)
admin.site.unregister(User)
