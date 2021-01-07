from django.db import models


# Create your models here.
from photoclub.accounts.models import UserProfile


class Photo(models.Model):
    PORTRAIT = 'Portrait'
    LANDSCAPE = 'Landscape'
    PANORAMA = 'Panorama'
    UNKNOWN = 'unknown'
    PHOTO_TYPES = (
        (PORTRAIT, 'Portrait'),
        (LANDSCAPE, 'Landscape'),
        (PANORAMA, 'Panorama'),
        (UNKNOWN, 'unknown'),
    )
    type = models.CharField(max_length=15, choices=PHOTO_TYPES, default=UNKNOWN)
    title = models.CharField(max_length=25, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='photos')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.title}; {self.date};'


class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.photo}'


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
