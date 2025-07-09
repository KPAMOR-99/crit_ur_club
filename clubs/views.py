from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Club, Manager, Owner, Player


def clubs_home(request):
    all_clubs = Club.objects.all()
    context = {
        'all_clubs': all_clubs
    }

    return render(request, 'clubs/clubs_home.html', context)

def club_detailed(request, club_slug):
    club = get_object_or_404(Club, slug=club_slug)
    manager = club.manager  # Direct access via foreign key
    owner = club.owner     # Direct access via foreign key
    players = Player.objects.filter(club=club)  # All players for this club

    context = {
        'club': club,   
       'manager': manager,
       'owner' : owner,
       'players' : players,
    }
    return render(request, 'clubs/club_detailed.html', context)

def club_manager(request, club_slug, manager_slug):
    club = get_object_or_404(Club, slug= club_slug)
    manager = get_object_or_404(Manager, slug=manager_slug)

    
    context = {
        'club': club,
        'manager':manager
        
    }

    return render(request, 'clubs/club_manager.html', context)


def club_owner(request, club_slug, owner_slug):
    club = get_object_or_404(Club, slug=club_slug)
    owner = get_object_or_404(Owner, slug=owner_slug)
    
    context = {
        'club': club,
        'owner': owner,
       
    }
    return render(request, 'clubs/club_owner.html', context)

def club_players(request, club_slug):
    club = get_object_or_404(Club, slug = club_slug)
    players = Player.objects.filter(club=club)
    context = {
        'club':club,
        'players':players
    }
    return render(request, 'clubs/club_players.html', context)


def  player_detailed(request, club_slug, player_slug):
    club = get_object_or_404(Club, slug=club_slug)
    player = get_object_or_404(Player, slug=player_slug, club=club)

    context = {
        'club': club,
        'player':player
    }
    return render(request, 'clubs/player_detailed.html', context)

