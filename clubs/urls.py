from django.urls import path

from . import views


# app_name = 'clubs'

urlpatterns = [
    # this provides the structure of the url for each page rendered and the url for clubs app i registered in the urls.py of the main app
            path('', views.clubs_home, name='clubs_home'),
            path('club/<slug:club_slug>/', views.club_detailed, name='club_detailed'),
            path('club/<slug:club_slug>/manager/<slug:manager_slug>/', views.club_manager, name='club_manager'),
            path('club/<slug:club_slug>/players/',views.club_players, name = 'club_players'),
            path('club/<slug:club_slug>/players/<slug:player_slug>',views.player_detailed, name = 'player_detailed'),
            path('club/<slug:club_slug>/<slug:owner_slug>/', views.club_owner, name='club_owner'),
          
]