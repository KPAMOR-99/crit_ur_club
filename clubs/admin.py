# Register your models here.

from django.contrib import admin
from .models import Owner, Manager, Club, Player

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
      list_display = ('name', 'age')

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'owner', 'form', 'slug')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'club', 'age', 'avr_rating')

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'nationality', 'matches_played')


