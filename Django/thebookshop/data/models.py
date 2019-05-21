from django.db import models
from books.models import Book
from django.urls import reverse_lazy

class Author(models.Model):
    first_name = models.CharField("Имя", null=False, blank=False, max_length=30)
    last_name = models.CharField("Фамилия", null=False, blank=False, max_length=30)
    country = models.CharField("Страна", null=False, blank=False, max_length=20)
    def __str__(self): # печать
        return self.first_name
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Genre(models.Model):
    name = models.CharField("Название", null=False, blank=False, max_length=25)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = 'Жанры'

class Series(models.Model):
    active = models.BooleanField("Активный", default=True)
    name = models.CharField("Название", null=False, blank=False, max_length=30)
    description = models.TextField("Описание", null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

class Publish(models.Model):
    name = models.CharField("Название", null=False, blank=False, max_length=50)
    country = models.CharField("Страна", null=True, blank=True, max_length=20)
    city = models.CharField("Город", null=True, blank=True, max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'

class Binding(models.Model):
    binding_type = models.CharField("Тип", null=False, blank=False, max_length=30)
    def __str__(self):
        return self.binding_type
    class Meta:
        verbose_name = 'Переплет'
        verbose_name_plural = 'Виды переплетов'

class BookFormat(models.Model):
    size = models.CharField("Размер", null=False, blank=False, max_length=30)
    def __str__(self):
        return self.size
    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'


class OrderStatus(models.Model):
    status_type = models.CharField("Статус", max_length=30)

    def __str__(self):
        return self.status_type

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'