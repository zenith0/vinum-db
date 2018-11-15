from django.db import models

COLOR_CHOICES = (
    ('red', 'Rot'),
    ('white', 'Weiß'),
    ('rose', 'Rose')
)

# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=40)
    grower = models.CharField(max_length=200)
    year = models.IntegerField(default=0, null=True, blank=True)
    color = models.CharField(choices=COLOR_CHOICES, max_length=5)
    front_img = models.ImageField(null=True, blank=True)
    back_img = models.ImageField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    provine = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name