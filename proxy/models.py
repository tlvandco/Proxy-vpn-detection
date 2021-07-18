from django.db import models

# Create your models here.
class Ipinfo(models.Model):
    ip = models.CharField(max_length=15)

    def __str__(self):
        return self.ip