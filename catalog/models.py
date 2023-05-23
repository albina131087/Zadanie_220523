from django.db import models
from django.urls import reverse

# Create your models here.
# Модель: Фильм. Поля: название, год создания (DateField), страна производитель, жанр, рейтинг (IntegerField).
# Сделать формы для создания, удаления, обновления, списка, информации о конкретном.
class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.DateField()
    country = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', args=[str(self.id)])