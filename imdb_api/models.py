from django.db import models

class Person(models.Model):
    person_id = models.CharField(max_length=9)
    primaryName = models.CharField(max_length=50)
    data = None

class Title(models.Model):
    title_id = models.CharField(max_length=9)
    data = None

class Episode(models.Model):
    episode_id = models.CharField(max_length=9)
    parent_id = models.ForeignKey(Title, on_delete=models.CASCADE)
    #title_id = models.ForeignKey('Title', on_delete=models.CASCADE)
    season = models.IntegerField()
    Episode = models.IntegerField()