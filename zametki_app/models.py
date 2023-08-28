from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    # Тема, которую изучает пользователь
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Темы'
        verbose_name = 'Тема'

    def __str__(self):
        # Возвращает строковое представление модели.
        return self.text


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete = models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Записи'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text[:50] + "..."

# Create your models here.
