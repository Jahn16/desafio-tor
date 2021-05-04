from django.db import models

class Ip(models.Model):
    ip_address = models.GenericIPAddressField()
