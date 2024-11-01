from django.db import models
from django.contrib.auth.models import User

class Strategy(models.Model):
    # Основные поля стратегии
    title = models.CharField(max_length=255, verbose_name="Название")  # Название стратегии
    description = models.TextField(verbose_name="Описание")  # Описание стратегии
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")  # Цена стратегии
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")  # Дата добавления
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")  # Дата последнего обновления
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Продавец")  # Продавец стратегии

    # Поля для рейтинга и просмотров
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, verbose_name="Рейтинг")  # Средний рейтинг
    views = models.IntegerField(default=0, verbose_name="Просмотры")  # Количество просмотров
    
    # Дополнительные поля (изображение и файл для стратегии)
    image = models.ImageField(upload_to='strategy_images/', blank=True, null=True, verbose_name="Изображение")
    file = models.FileField(upload_to='strategy_files/', blank=True, null=True, verbose_name="Файл стратегии")

    def __str__(self):
        return self.title
