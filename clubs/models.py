from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError


class Owner(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)
    # club = models.ForeignKey(Club, on_delete=models.CASCADE)

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
    age = models.PositiveIntegerField(default=0) 
    nationality = models.CharField(max_length=100, blank=True)  
    matches_played = models.PositiveIntegerField(default=0)  
    
    def get_absolute_url(self):
        return reverse('club_manager', kwargs={
            'club_slug': self.club.slug,  
            'manager_slug': self.slug
        })
    # this makes the manager name in the title not have manager object added to it
    def __str__(self):
        return self.name
   

class Club(models.Model):
    # attributes for club
    name = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(unique=True, blank=True)
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE, related_name="club")
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, related_name="club")
    form = models.CharField(max_length=5)

     # i used this in the models for generating clean urls, dynamic too i guess
    def get_absolute_url(self):
        return reverse('club_detailed', kwargs={'club_slug': self.slug})
    
    

class Player(models.Model):
    # attributes for individual players
    name = models.CharField(max_length=100, primary_key=True)
    age = models.PositiveIntegerField()
    position = models.CharField(max_length=10)
    avr_rating = models.FloatField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    
    # i used this in the models for generating clean urls, dynamic too i guess
    def get_absolute_url(self):
        return reverse('player_detailed', kwargs={
            'club_slug': self.club.slug,
            'player_slug': self.slug  
        })
    # i didnt add the __str__ method here but i dont know why in the object it actually displays the name, maybe because i addressed it in manager view as a foriegn key?
    
class Criticism(models.Model):
    comment = models.TextField()
    time = models.DateTimeField()
    likes = models.PositiveIntegerField(default=0)

    # inorder to track who has commented, foriegn key to django's default user model 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # i had to add null and blank to ensure that can comment must not neceessarily be tied to all four models
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)

    # to ensure a comment is tid to at least one entity
    def isTied(self):
        if not  (self.player or self.manager or self.owner):
            raise ValidationError("a criticism must be tied to at least one entity")
        # ensures this istied logic runs before each criticism is saved
    def save(self, *args, **kwargs):
        self.isTied()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Criticism by {self.user} on {self.time}"
