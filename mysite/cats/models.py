from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Breed(models.Model):
    name = models.CharField(
        max_length=248,
        help_text='Enter a breed',
        validators =[MinLengthValidator(2, "Breed must be greater than 1 character")]
        )

    def __str__(self):
        return self.name


class Cat(models.Model):
    nickname = models.CharField(
        max_length=248,
        validators=[MinLengthValidator(2, "Name must be greater than 1 character")]
        )
    foods = models.CharField(max_length=300)
    weight = models.PositiveIntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname