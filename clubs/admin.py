from django.contrib import admin
from .models import Owner, Manager, Club, Player, Criticism


# registered my models here so that i it will be dsplayed in my admin page in my browser
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

@admin.register(Criticism)
class CriticismAdmin(admin.ModelAdmin):
     list_display = ('comment', 'time', 'likes', 'player', 'manager', 'owner')
