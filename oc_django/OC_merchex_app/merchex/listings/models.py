from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Band(models.Model):
    
    def __str__(self):
        return f'{self.name}'
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        RAP     = 'RAP'
        SYNTH   = 'SP'
        ALTERNATIVE = 'AR'

    name = models.fields.CharField(max_length=50)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=100)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    homepage = models.fields.URLField(null=True, blank=True)
    

class Listing(models.Model):
    def __str__(self):
        return f'{self.title}'
    class Type(models.TextChoices):
        Records         = 'R'
        Clothing        = 'C'
        Posters         = 'P'
        Miscellaneous   = 'M'
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL) 
    title = models.fields.CharField(max_length=50)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True,
                                      validators=[MinValueValidator(0), MaxValueValidator(2023)])
    type = models.fields.CharField(choices=Type.choices, max_length=1)