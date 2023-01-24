from django.db import models

# Create your models here.
class DailyNews(models.Model):
    newsTitle = models.TextField()
    details = models.TextField()


    def __str__(self):
        return self.newsTitle