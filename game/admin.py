from django.contrib import admin

from .models import Category, Game


admin.site.register(Category)


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image',)


admin.site.register(Game, GameAdmin)
