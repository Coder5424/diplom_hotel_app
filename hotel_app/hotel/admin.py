from django.contrib import admin
from .models import Room, User, Booking


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register([Room, Booking])
admin.site.register(User, UserAdmin)
