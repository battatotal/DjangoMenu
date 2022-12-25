from django.db import models
from django.urls import reverse


class JMenu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    ancestor = models.IntegerField(unique=False)
    descendant = models.IntegerField(unique=False)
    depth = models.IntegerField(unique=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('menu', kwargs={'item_slug': self.slug})



class MainMenu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    ancestor = models.IntegerField(unique=False)
    descendant = models.IntegerField(unique=False)
    depth = models.IntegerField(unique=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('menu', kwargs={'item_slug': self.slug})