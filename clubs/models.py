from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Owner(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('club_owner', kwargs={
            'club_slug': self.club.slug,
            'owner_slug':self.slug,
        })
    def __str__(self):
        return self.name

    

class Manager(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(unique=True, blank=True)
    age = models.IntegerField(default=0) 
    nationality = models.CharField(max_length=100, blank=True)  
    matches_played = models.IntegerField(default=0)  
    
    def get_absolute_url(self):
        return reverse('club_manager', kwargs={
            'club_slug': self.club.slug,  # Assumes 1 club per manager
            'manager_slug': self.slug
        })
    def __str__(self):
        return self.name
   

class Club(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(unique=True, blank=True)
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE, related_name="club")
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, related_name="club")
    form = models.CharField(max_length=5)

    def get_absolute_url(self):
        return reverse('club_detailed', kwargs={'club_slug': self.slug})
    
    

class Player(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    position = models.CharField(max_length=10)
    avr_rating = models.FloatField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('player_detailed', kwargs={
            'club_slug': self.club.slug,
            'player_slug': self.slug  # Now uses the stored slug
        })