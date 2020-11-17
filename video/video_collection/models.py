from django.db import models

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.pk} -- {self.name} -- {self.url} -- {self.notes[:200]}'
