from django.db import models

class Redirect(models.Model):
    url = models.CharField(max_length = 300)
    shortHand = models.CharField(max_length = 15)
