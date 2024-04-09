from datetime import datetime

from django.db import models

class News(models.Model):
    Title = models.CharField(max_length=50, verbose_name="Заголовок новости")
    Description = models.TextField(verbose_name="Описание новости")
    Date = models.DateTimeField(verbose_name="Дата созания", default=datetime.now())
    Image = models.ImageField(blank=True, null=True)
    VideoUrl = models.CharField(max_length=50, verbose_name="ccылка на видео")
