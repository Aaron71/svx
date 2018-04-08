from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver


class RaceMatrix(models.Model):
    index  = models.IntegerField(blank=True)
    media_id = models.CharField(max_length=255, blank=True)
    network = models.CharField(max_length=255, blank=True)
    surface = models.CharField(max_length=255, blank=True)
    track = models.CharField(max_length=255, blank=True)
    date_id = models.IntegerField(blank=True)
    event = models.CharField(max_length=255, blank=True)
    video_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return str(self.index)

@receiver(pre_save, sender=RaceMatrix)
def matrix_pre_save(sender, **kwargs):
    instance = kwargs.get("instance")
    print("=++++++++++++++++++++++=")
    print(instance)
    if not instance.index:
        last_matrix = RaceMatrix.objects.last()
        print(last_matrix)
        if not last_matrix:
            instance.index =1
        else:
            instance.index = last_matrix.index + 1





