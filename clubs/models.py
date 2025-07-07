from django.db import models
from django.utils.text import  slugify
from django.urls import reverse

class Owner(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()

class Manager(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    nationality = models.CharField(max_length=50)
    matches_played = models.IntegerField()
   # form = models.CharField(max_length=5)    i need to make this the same with that of the club


class Club(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(unique=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    form = models.CharField(max_length=5)

    
    def save(self, *args, **kwargs):
        if self.slug == 'temp-slug': self.slug = slugify(self.name)
        super().save(*args, **kwargs)                 
    
    def get_absolute_url(self):
        return reverse('club_detailed', kwargs={'club_slug': self.slug})


class Player(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    position = models.CharField(max_length=10)
    avr_rating = models.FloatField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    @property
    def slug(self):
        return slugify(self.name)
    
    def get_absolute_url(self):  # automatic slug generation to avoid manaually constructing urls in views again
        return reverse('player_detailed', kwargs={
            'club_slug': self.club.slug,
            'player_slug': slugify(self.name)
        })

