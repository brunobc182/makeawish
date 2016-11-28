from django.contrib import admin
from models import Wish


# Register your models here.

class WishAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('title', 'created_at')
    readonly_fields = ('created_at', )


admin.site.register(Wish, WishAdmin)
