from django.db import models

spatial_list = [
    ('Geometry', 'geometry')
]
#TODO refatorar os nomes das classes Class --> Resource; Context --> ResourceAttribute

class Class(models.Model):
    name = models.CharField(max_length=1000, blank=False, null=False, unique=True)
    spatial = models.CharField(max_length=255, choices=spatial_list, blank=False, null=True)

# Create your models here.
class Context(models.Model):
    attribute = models.CharField(max_length=255, blank=False, null=False)
    means = models.CharField(max_length=1000, blank=False, null=False, default="http://schema.org/Thing")
    type = models.CharField(max_length=1000, blank=True, null=True)
    classname = models.ForeignKey(Class, related_name="contexts")
