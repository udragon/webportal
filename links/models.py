from django.db import models

# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Category: %s>' % self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Link(models.Model):
    name        = models.CharField(max_length=32, primary_key=True)
    url         = models.CharField(max_length=63)
    icon        = models.CharField(max_length=32)
    category    = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Link: %s>' % self.name


