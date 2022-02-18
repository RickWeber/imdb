from django.db import models

class Item(models.Model):
    last_update = models.DateTimeField('last update')
    data = models.JSONField('json data')

class Person(Item):
    person_id = models.CharField(max_length=9)
    primaryName = models.CharField(max_length=50)

class Title(Item):
    title_id = models.CharField(max_length=9)

class Episode(Item):
    episode_id = models.CharField(max_length=9)
    parent_id = models.ForeignKey(Title, on_delete=models.CASCADE)
    #title_id = models.ForeignKey('Title', on_delete=models.CASCADE)
    season_number = models.IntegerField(default=1)
    episode_number = models.IntegerField(default=1)